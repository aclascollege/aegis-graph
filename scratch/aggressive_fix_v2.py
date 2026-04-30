import os

filepath = r'd:\aicoding\kaiyuan\v2\index.html'

with open(filepath, 'rb') as f:
    data = f.read()

# Hex-based replacements for Latin-1/UTF-8 corrupted bytes
replacements = [
    (b'\xc3\xa2\xc2\x80\xc2\x94', '—'.encode('utf-8')),
    (b'\xc3\xa2\xc2\x80\xc2\xa2', '•'.encode('utf-8')),
    (b'a\x3f\x3f\x61', '—'.encode('utf-8')),
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
    (b'Portugu\xef\xbf\xbds', 'Português'.encode('utf-8')),
    (b'\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd', '🔍'.encode('utf-8')),
]

for old, new in replacements:
    data = data.replace(old, new)

# Final write
with open(filepath, 'wb') as f:
    f.write(data)

print('Aggressive Hex Reconstruction (Take 2) Complete.')
