import os

docs_path = r'd:\aicoding\kaiyuan\v2\docs'

# Common corruptions to fix in documentation
REPLACEMENTS = {
    'Ã°ÂŸÂ‡ÂºÃ°ÂŸÂ‡Â¸': '🇺🇸',
    'Ã°ÂŸÂ‡Â­Ã°ÂŸÂ‡Â°': '🇭🇰',
    'Ã°ÂŸÂ‡ÂªÃ°ÂŸÂ‡Â¸': '🇪🇸',
    'Ã°ÂŸÂ‡Â«Ã°ÂŸÂ‡Â·': '🇫🇷',
    'Ã°ÂŸÂ‡Â©Ã°ÂŸÂ‡Âª': '🇩🇪',
    'Ã°ÂŸÂ‡Â¯Ã°ÂŸÂ‡Âµ': '🇯🇵',
    'Ã°ÂŸÂ‡Â°Ã°ÂŸÂ‡Â·': '🇰🇷',
    'Ã°ÂŸÂ‡Â¸Ã°ÂŸÂ‡Â¦': '🇸🇦',
    'Ã°ÂŸÂ‡ÂµÃ°ÂŸÂ‡Â¹': '🇵🇹',
    'Ã¢Â€Â”': '—',
    'Ã¢Â€Â¢': '•',
    'Ã‚Â©': '©',
    'FranÃƒÂ§ais': 'Français',
    'EspaÃƒÂ±ol': 'Español',
    'PortuguÃƒÂªs': 'Português',
    'Ã¦Â—Â¥Ã¦ÂœÂ¬Ã¨ÂªÂ ': '日本語',
    'Ã­Â•ÂœÃªÂµÂ­Ã¬Â–Â ': '한국어',
    'Ã§Â¹Â Ã©Â«Â”Ã¤Â¸Â­Ã¦Â–Â‡': '繁體中文',
    'Ã˜Â§Ã™Â„Ã˜Â¹Ã˜Â±Ã˜Â¨Ã™ÂŠÃ˜Â©': 'العربية',
    '\ufffd': '' # Remove replacement characters
}

def purify_docs():
    # Scan docs/ directory
    for root, dirs, files in os.walk(docs_path):
        for file in files:
            if file.endswith('.md'):
                process_file(os.path.join(root, file))
    
    # Scan root directory for specific markdown files
    root_path = r'd:\aicoding\kaiyuan\v2'
    root_md_files = ['README.md', 'WHITEPAPER.md', 'RELEASE_V1.md', 'SECURITY.md']
    for file in root_md_files:
        filepath = os.path.join(root_path, file)
        if os.path.exists(filepath):
            process_file(filepath)

def process_file(filepath):
    print(f"Purifying: {filepath}")
    with open(filepath, 'rb') as f:
        data = f.read()
    
    try:
        content = data.decode('utf-8')
    except UnicodeDecodeError:
        content = data.decode('latin-1')
    
    # Apply replacements
    for old, new in REPLACEMENTS.items():
        content = content.replace(old, new)
    
    # Write back as clean UTF-8
    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)

if __name__ == "__main__":
    purify_docs()
    print("\nAll documentation files have been purified.")
