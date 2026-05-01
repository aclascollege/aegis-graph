import os
import re

def purify():
    path = 'index.html'
    if not os.path.exists(path):
        return

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Map of specific corruptions found in the source
    corrections = {
        '馃嚭馃嚫': '🇺🇸',
        'Fran莽ais': 'Français',
        'Espa帽ol': 'Español',
        '鏃ユ湰瑾?': '日本語',
        '頃滉淡鞏?': '한국어',
        '绻侀珨涓枃': '繁體中文',
        '丕賱毓乇亘賷丞': 'العربية',
        'Portugu锚s': 'Português',
        '鈻?': '▾',
        '碟韬': '',
        '鈹?': '—',
        '鈭?': '✓'
    }

    for bad, good in corrections.items():
        if bad in content:
            content = content.replace(bad, good)

    # 2. Fix Header Container Layout
    old_header = '<div style="display: flex; gap: 16px; align-items: center">'
    new_header = '<div class="header-actions" style="display: flex; gap: 12px; align-items: center; min-height: 40px">'
    
    if old_header in content:
        content = content.replace(old_header, new_header)
    else:
        content = re.sub(r'<div style="display:\s*flex;\s*gap:\s*16px;\s*align-items:\s*center">', new_header, content)

    # 3. Final sanitization
    content = content.replace('\ufeff', '')

    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    
    print("PURIFICATION SUCCESSFUL")

if __name__ == "__main__":
    purify()
