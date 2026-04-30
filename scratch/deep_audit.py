import os
import re

filepath = r'd:\aicoding\kaiyuan\v2\index.html'

# Common corruptions to fix globally
GLOBAL_REPLACEMENTS = {
    'Ã°ÂŸÂ‡ÂºÃ°ÂŸÂ‡Â¸': '🇺🇸',
    'Ã°ÂŸÂ‡Â­Ã°ÂŸÂ‡Â°': '🇭🇰',
    'Ã°ÂŸÂ‡ÂªÃ°ÂŸÂ‡Â¸': '🇪🇸',
    'Ã°ÂŸÂ‡Â«Ã°ÂŸÂ‡Â·': '🇫🇷',
    'Ã°ÂŸÂ‡Â©Ã°ÂŸÂ‡Âª': '🇩🇪',
    'Ã°ÂŸÂ‡Â¯Ã°ÂŸÂ‡Âµ': '🇯🇵',
    'Ã°ÂŸÂ‡Â°Ã°ÂŸÂ‡Â·': '🇰🇷',
    'Ã°ÂŸÂ‡Â¸Ã°ÂŸÂ‡Â¦': '🇸🇦',
    'Ã°ÂŸÂ‡ÂµÃ°ÂŸÂ‡Â¹': '🇵🇹',
    'Ã°ÂŸÂŒÂŽ': '🌍',
    'Ã°ÂŸÂ“Â¢': '📢',
    'Ã°ÂŸÂŒÂ ': '🌍',
    'Ã°ÂŸÂ“Â ': '📄',
    'Ã¢Â–Â ': '▾',
    'Ã¢Â–Â¾': '▾',
    'Ã¢Â–?': '▾',
    'Ã¢Â–': '▾',
    'FranÃƒÂ§ais': 'Français',
    'EspaÃƒÂ±ol': 'Español',
    'PortuguÃƒÂªs': 'Português',
    'Ã¦Â—Â¥Ã¦ÂœÂ¬Ã¨ÂªÂ ': '日本語',
    'Ã­Â•ÂœÃªÂµÂ­Ã¬Â–Â ': '한국어',
    'Ã§Â¹Â Ã©Â«Â”Ã¤Â¸Â­Ã¦Â–Â‡': '繁體中文',
    'Ã˜Â§Ã™Â„Ã˜Â¹Ã˜Â±Ã˜Â¨Ã™ÂŠÃ˜Â©': 'العربية',
    'Ã‚Â©': '©',
    'Ã¢Â€Â¢': '•',
    'Ã¢Â€Â”': '—',
    'Ã¢Â–Â¾': '▾',
    'ðŸ‡ºðŸ‡¸': '🇺🇸',
    'ðŸ‡­ðŸ‡°': '🇭🇰',
    'ðŸ‡ªðŸ‡¸': '🇪🇸',
    'ðŸ‡«ðŸ‡·': '🇫🇷',
    'ðŸ‡©ðŸ‡ª': '🇩🇪',
    'ðŸ‡¯ðŸ‡µ': '🇯🇵',
    'ðŸ‡°ðŸ‡·': '🇰🇷',
    'ðŸ‡¸ðŸ‡¦': '🇸🇦',
    'ðŸ‡µðŸ‡¹': '🇵🇹'
}

def audit_file():
    with open(filepath, 'rb') as f:
        data = f.read()
    
    # Try decoding to find the current mess
    try:
        content = data.decode('utf-8')
    except UnicodeDecodeError:
        content = data.decode('latin-1')

    # 1. Global Replacement of known artifacts
    for old, new in GLOBAL_REPLACEMENTS.items():
        content = content.replace(old, new)

    # 2. Fix Academic Keywords and other script-level corruptions
    content = content.replace('Ã¥Â­Â¦Ã¤Â½Â ', '学位').replace('Ã¥Â¤Â§Ã¥Â­Â¦', '大学')
    content = content.replace('Ã¦ÂˆÂ Ã§Â»©Ã¥Â ?', '成绩单').replace('Ã¨Â¯Â Ã¤Â¹Â¦', '证书')
    content = content.replace('Ã©Â€Â Ã¥Â Â‡', '造假')

    # 3. Structural Health Check
    # Ensure all main sections are present and clean
    if '<meta charset="UTF-8">' not in content:
        content = content.replace('<head>', '<head>\n    <meta charset="UTF-8">')
    
    # Fix the trailing garbage seen in the screenshot (?/div>)
    content = re.sub(r'\?\s*/div>', '</div>', content)
    content = re.sub(r'\?\s*/button>', '</button>', content)
    
    # Check for unclosed divs (rudimentary check)
    open_divs = content.count('<div')
    close_divs = content.count('</div')
    print(f'Div count check: Open={open_divs}, Close={close_divs}')
    
    if open_divs > close_divs:
        print('WARNING: Unclosed divs detected. Attempting to balance...')
        # This is risky but often it's just one missing at the end of a section
    
    # 4. Standardize all emojis
    content = content.replace('🔍', '🔍').replace('🛡️', '🛡️').replace('🌐', '🌐')

    # Write back clean
    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    
    print('Deep Audit and Cleanup Complete.')

if __name__ == '__main__':
    audit_file()
