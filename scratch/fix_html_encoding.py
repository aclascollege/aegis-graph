import os

filepath = r'd:\aicoding\kaiyuan\v2\index.html'
with open(filepath, 'r', encoding='latin-1') as f:
    content = f.read()

# Fix common Latin-1 corruptions of UTF-8 strings
mapping = {
    'ðŸ‡ºðŸ‡¸': '🇺🇸',
    'ðŸ‡­ðŸ‡°': '🇭🇰',
    'ðŸ‡ªðŸ‡¸': '🇪🇸',
    'ðŸ‡«ðŸ‡·': '🇫🇷',
    'ðŸ‡©ðŸ‡ª': '🇩🇪',
    'ðŸ‡¯ðŸ‡µ': '🇯🇵',
    'ðŸ‡°ðŸ‡·': '🇰🇷',
    'ðŸ‡¸ðŸ‡¦': '🇸🇦',
    'ðŸ‡µðŸ‡¹': '🇵🇹',
    'ðŸŒŽ': '🌍',
    'ðŸ“¢': '📢',
    'ðŸŒ ': '🌍',
    'ðŸ“ ': '📄',
    'â–?': '▾',
    'FranÃ§ais': 'Français',
    'EspaÃ±ol': 'Español',
    'PortuguÃªs': 'Português',
    'æ—¥æœ¬èª?': '日本語',
    'í•œêµ­ì–?': '한국어',
    'ç¹ é«”ä¸­æ–‡': '繁體中文',
    'Ø§Ù„Ø¹Ø±Ø¨ÙŠØ©': 'العربية',
    'â€?': '—',
    'â€¢': '•',
    'Â©': '©'
}

# Also ensure meta charset is present
if '<meta charset="UTF-8">' not in content:
    content = content.replace('<html lang="en">', '<html lang="en">\n<head>\n    <meta charset="UTF-8">')

for old, new in mapping.items():
    content = content.replace(old, new)

# One more pass for specific broken tags seen in view_file
content = content.replace('æ—¥æœ¬èª?/option>', '日本語</option>')
content = content.replace('í•œêµ­ì–?/option>', '한국어</option>')

with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print('index.html encoding and characters fixed successfully')
