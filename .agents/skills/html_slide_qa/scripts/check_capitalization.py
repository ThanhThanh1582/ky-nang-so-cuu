import os
import re
import sys
from html.parser import HTMLParser

# Block tags that define structure
BLOCK_TAGS = {
    'div', 'section', 'ul', 'ol', 'li', 'p', 
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 
    'td', 'th', 'table', 'thead', 'tbody', 'tr', 
    'aside', 'main', 'header', 'footer', 'article', 'nav', 'blockquote'
}

# Tags that we want to enforce capitalization on (if they are leaf blocks)
CHECK_TAGS = {'li', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'td', 'th', 'div'}

# Tags we completely ignore (their content doesn't get checked or extracted)
IGNORE_TAGS = {'script', 'style', 'canvas', 'svg', 'code', 'pre'}

class SlideTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.current_slide_id = "Unknown"
        self.stack = []  # Tracks block tags: list of dicts {'tag': tag, 'text': '', 'has_block_child': False, 'line_no': line}
        self.violations = []
        self.extracted_texts = []
        self.ignore_depth = 0

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # Check if we are inside an ignored tag
        if tag in IGNORE_TAGS:
            self.ignore_depth += 1
            return
            
        if self.ignore_depth > 0:
            return

        # Track slide boundaries
        if (tag == 'section' or tag == 'div') and 'class' in attrs_dict:
            classes = attrs_dict['class'].split()
            if 'slide' in classes or 'slide-frame' in classes:
                full_id = attrs_dict.get('id', 'Unknown')
                if full_id.startswith('slide-'):
                    self.current_slide_id = full_id[6:]
                else:
                    self.current_slide_id = full_id

        # If it's a block tag, manage the stack
        if tag in BLOCK_TAGS:
            if self.stack:
                # Mark parent as having a block child
                self.stack[-1]['has_block_child'] = True
            
            line_no, _ = self.getpos()
            self.stack.append({
                'tag': tag,
                'text': '',
                'has_block_child': False,
                'line_no': line_no,
                'slide_id': self.current_slide_id
            })

    def handle_endtag(self, tag):
        if tag in IGNORE_TAGS:
            self.ignore_depth = max(0, self.ignore_depth - 1)
            return

        if self.ignore_depth > 0:
            return

        if tag in BLOCK_TAGS and self.stack:
            # Find the matching tag in the stack
            # Pop elements until we find the matching tag (handles unclosed tags gracefully)
            popped_elements = []
            while self.stack:
                el = self.stack.pop()
                popped_elements.append(el)
                if el['tag'] == tag:
                    break
            
            if popped_elements:
                target = popped_elements[-1]
                # If we popped multiple elements due to mismatched tags, we only check the matching one
                # If it's one of check tags and had no block children, check and save it
                if target['tag'] in CHECK_TAGS and not target['has_block_child']:
                    self.process_leaf_block(target)

    def handle_data(self, data):
        if self.ignore_depth > 0:
            return

        if self.stack:
            # Accumulate text for the current block
            self.stack[-1]['text'] += data

    def process_leaf_block(self, block):
        cleaned_text = block['text'].strip()
        # Clean up excessive whitespace and newlines
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
        if not cleaned_text:
            return

        # Record for spelling/grammar checks
        self.extracted_texts.append({
            'slide_id': block['slide_id'],
            'line_no': block['line_no'],
            'tag': block['tag'],
            'text': cleaned_text
        })

        # Check capitalization
        # Find first alphabetic character (supporting Vietnamese unicode characters)
        match = re.search(r'[a-zA-ZÀ-ỹ]', cleaned_text)
        if match:
            first_char = match.group(0)
            if first_char.islower():
                self.violations.append({
                    'slide_id': block['slide_id'],
                    'line_no': block['line_no'],
                    'tag': block['tag'],
                    'text': cleaned_text,
                    'first_char': first_char
                })

def main():
    # Look for index.html or command line argument
    html_path = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
    if not os.path.exists(html_path):
        print(f"Error: {html_path} not found.")
        sys.exit(1)
        
    print(f"Reading and parsing {html_path}...")
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    extractor = SlideTextExtractor()
    extractor.feed(content)

    # 1. Write the extracted text to a temporary report file for the LLM to inspect
    os.makedirs('.agents', exist_ok=True)
    temp_report_path = '.agents/temp_slide_text.txt'
    
    with open(temp_report_path, 'w', encoding='utf-8') as f:
        f.write("=== EXTRACTED SLIDE TEXTS FOR SPELLING AND GRAMMAR AUDIT ===\n")
        f.write("Format: [Slide ID] [Line #] <tag>: Text\n\n")
        for item in extractor.extracted_texts:
            f.write(f"[{item['slide_id']}] [Line {item['line_no']}] <{item['tag']}>: {item['text']}\n")

    print(f"Extracted text saved to {temp_report_path}")

    # 2. Report Capitalization Violations
    if extractor.violations:
        print(f"\n[VIOLATION] Found {len(extractor.violations)} capitalization errors:")
        for v in extractor.violations:
            print(f"  - Slide [{v['slide_id']}], Line {v['line_no']} <{v['tag']}>: Starts with lowercase '{v['first_char']}'")
            print(f"    Text: \"{v['text']}\"")
        # Exit with code 1 to indicate violations found
        sys.exit(1)
    else:
        print("\n[SUCCESS] No capitalization violations found!")
        sys.exit(0)

if __name__ == '__main__':
    main()
