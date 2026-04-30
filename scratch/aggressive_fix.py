import os
import re

filepath = r'd:\aicoding\kaiyuan\v2\index.html'

with open(filepath, 'rb') as f:
    data = f.read()

# Aggressive Hex-based cleaning
# We define the correct blocks for the most sensitive areas
replacements = [
    # General cleanup
    (b'Ã¢Â€Â”', '—'.encode('utf-8')),
    (b'Ã¢Â€Â¢', '•'.encode('utf-8')),
    (b'a\?\?a', '—'.encode('utf-8')),
    (b'L\xef\xbf\xbdgico', 'Lógico'.encode('utf-8')),
    (b'Vis\xef\xbf\xbd o', 'Visão'.encode('utf-8')),
    (b'Vis\xef\xbf\xbdo', 'Visão'.encode('utf-8')),
    (b'Visi\xef\xbf\xbdn', 'Visión'.encode('utf-8')),
    (b'Auditor\xef\xbf\xbd a', 'Auditoría'.encode('utf-8')),
    (b'Auditor\xef\xbf\xbdia', 'Auditoría'.encode('utf-8')),
    (b'Confidencialit\xef\xbf\xbd', 'Confidencialité'.encode('utf-8')),
    (b'Pr\xef\xbf\xbd fung', 'Prüfung'.encode('utf-8')),
    (b'Pr\xef\xbf\xbdfung', 'Prüfung'.encode('utf-8')),
    (b'Souver\xef\xbf\xbd nes', 'Souveränes'.encode('utf-8')),
    (b'Souver\xef\xbf\xbdnes', 'Souveränes'.encode('utf-8')),
    (b'Fran\xef\xbf\xbd ais', 'Français'.encode('utf-8')),
    (b'Fran\xef\xbf\xbdais', 'Français'.encode('utf-8')),
    (b'Espa\xef\xbf\xbd ol', 'Español'.encode('utf-8')),
    (b'Espa\xef\xbf\xbdol', 'Español'.encode('utf-8')),
    (b'Portugu\xef\xbf\xbd s', 'Português'.encode('utf-8')),
    (b'Portugu\xef\xbf\xbd s', 'Português'.encode('utf-8')),
    (b'Portugu\xef\xbf\xbd s', 'Português'.encode('utf-8')),
    (b'Portugu\xef\xbf\xbds', 'Português'.encode('utf-8')),
]

for old, new in replacements:
    data = data.replace(old, new)

# Fix the specific corrupted script line 1109
bad_logic = b"fileName.toLowerCase().includes('\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd')"
good_logic = b"fileName.toLowerCase().includes('造假')"
data = data.replace(bad_logic, good_logic)

# Fix the upload icon (line 914 area)
data = data.replace(b'<div class="upload-icon">\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd</div>', b'<div class="upload-icon">🔍</div>')

# Ensure UTF-8 with NO BOM
with open(filepath, 'wb') as f:
    f.write(data)

print('Aggressive Hex Reconstruction Complete.')
