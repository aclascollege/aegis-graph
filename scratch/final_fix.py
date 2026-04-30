import os

filepath = r'd:\aicoding\kaiyuan\v2\index.html'
with open(filepath, 'rb') as f:
    data = f.read()

# 1. Restore Header
header_start = data.find(b'<header>')
header_end = data.find(b'</header>') + len(b'</header>')

if header_start != -1 and header_end != -1:
    new_header = '''<header>
            <div class="logo-group">
                <span class="logo-text">AEGIS-GRAPH</span>
                <span style="font-size: 10px; color: #ccc; font-weight: 600; margin-left: 8px">BY <a
                        href="https://aclas.college/" target="_blank"
                        style="color: inherit; text-decoration: none; border-bottom: 1px solid #444">ATLANTA COLLEGE OF
                        LIBERAL ARTS AND SCIENCES (ACLAS COLLEGE)</a></span>
                <span class="version-tag">STABLE_v1.0</span>
            </div>
            <div style="display: flex; gap: 16px; align-items: center">
                <!-- Language Switcher -->
                <div class="lang-selector"
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
                    </select>
                    <div style="position: absolute; right: 8px; top: 50%; transform: translateY(-50%); pointer-events: none; opacity: 0.5">▾</div>
                </div>

                <button id="theme-toggle" title="Toggle Theme"
                    style="background: none; border: none; color: var(--foreground); cursor: pointer; opacity: 0.8; padding: 4px;">
                    <svg id="sun-icon" style="display: none" width="20" height="20" viewBox="0 0 24 24" fill="none"
                        stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="12" cy="12" r="5"></circle>
                        <line x1="12" y1="1" x2="12" y2="3"></line>
                        <line x1="12" y1="21" x2="12" y2="23"></line>
                        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                        <line x1="1" y1="12" x2="3" y2="12"></line>
                        <line x1="21" y1="12" x2="23" y2="12"></line>
                        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
                    </svg>
                    <svg id="moon-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
                    </svg>
                </button>
                <a href="https://atlanta-college-of-liberal-arts.gitbook.io/atlanta-college-of-liberal-arts-and-sciences/"
                    target="_blank"
                    style="color: var(--accent-dim); text-decoration: none; font-size: 11px; font-weight: 600; border: 1px solid var(--border); padding: 6px 12px; border-radius: 6px; transition: all 0.2s; display: flex; align-items: center; gap: 6px">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                        stroke-linecap="round" stroke-linejoin="round">
                        <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                        <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
                    </svg>
                    DOCS
                </a>
                <a href="https://github.com/aclascollege/aegis-graph" target="_blank" title="View on GitHub"
                    style="color: var(--foreground); opacity: 0.8; transition: opacity 0.2s">
                    <svg height="24" viewBox="0 0 16 16" width="24" fill="currentColor">
                        <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
                    </svg>
                </a>
                <span style="font-size: 11px; color: #aaa; font-weight: 600" class="desktop-only">NETWORK STATUS: <span
                        style="color: var(--success)">SECURE</span></span>
                <button class="btn-primary" id="init-btn">Initiate Audit</button>
            </div>
        </header>'''
    data = data[:header_start] + new_header.encode('utf-8') + data[header_end:]

with open(filepath, 'wb') as f:
    f.write(data)
print('Header and Translations block fully restored via binary seek.')
