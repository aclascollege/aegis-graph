import os

filepath = r'd:\aicoding\kaiyuan\v2\index.html'

# Read the entire file as binary to avoid encoding confusion
with open(filepath, 'rb') as f:
    raw_data = f.read()

# Convert to string, ignoring errors temporarily to find boundaries
text = raw_data.decode('utf-8', errors='ignore')

# 1. Ensure Meta Charset is at the top of head
if '<meta charset="UTF-8">' not in text:
    text = text.replace('<head>', '<head>\n    <meta charset="UTF-8">')

# 2. Reconstruct the Language Selector block with perfect UTF-8
lang_selector_start = '<div class="lang-selector"'
lang_selector_end = '</select>'

new_lang_selector = '''<div class="lang-selector"
                    style="position: relative; display: flex; align-items: center; gap: 8px; border: 1px solid var(--border); padding: 4px 10px; border-radius: 8px; font-size: 11px; font-weight: 600; cursor: pointer; color: var(--accent-dim)">
                    <span id="current-lang-flag">🇺🇸</span>
                    <select id="lang-switch"
                        style="background: none; border: none; color: inherit; font-family: inherit; font-size: inherit; font-weight: inherit; cursor: pointer; outline: none; appearance: none; padding-right: 12px">
                        <option value="en">English</option>
                        <option value="fr">Français</option>
                        <option value="es">Español</option>
                        <option value="de">Deutsch</option>
                        <option value="jp">日本語</option>
                        <option value="kr">한국어</option>
                        <option value="zh">繁體中文</option>
                        <option value="ar">العربية</option>
                        <option value="pt">Português</option>
                    </select>'''

# Find the old block and replace it
# We need to be careful with the corrupted text
import re
# Regex to find the corrupted lang-selector block
pattern = re.compile(r'<div class="lang-selector".*?</select>', re.DOTALL)
text = pattern.sub(new_lang_selector, text)

# 3. Fix the dropdown arrow if corrupted
text = text.replace('â–?', '▾').replace('Ã¢Â–?', '▾')

# 4. Final safety check on characters
# Write back as clean UTF-8
with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
    f.write(text)

print('index.html fully reconstructed with clean UTF-8')
