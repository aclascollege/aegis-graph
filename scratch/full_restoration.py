import os
import re

filepath = r'd:\aicoding\kaiyuan\v2\index.html'

with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# 1. Fix the Header and Language Selector structure
header_pattern = re.compile(r'<header>.*?</header>', re.DOTALL)
correct_header = '''<header>
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

content = header_pattern.sub(correct_header, content)

# 2. Fix the TRANSLATIONS object
translations_pattern = re.compile(r'const TRANSLATIONS = \{.*?\}\};', re.DOTALL)
correct_translations = '''const TRANSLATIONS = {
            en: {
                flag: '🇺🇸',
                title: 'Aegis-Graph: Sovereign Audit Network',
                subtitle: 'Drop credentials or click to browse',
                init_btn: 'Initiate Audit',
                docs: 'DOCS',
                pillars: ['Sovereign Trust', 'Agentic GraphRAG', 'Zero-Knowledge Privacy'],
                agents: ['Vision Forensics', 'Graph Navigator', 'Logic Auditor'],
                log_init: 'Initializing Aegis-Graph protocol...',
                log_ready: 'System Ready. Please upload a document for verification.',
                footer: 'BY ATLANTA COLLEGE OF LIBERAL ARTS AND SCIENCES (ACLAS COLLEGE)'
            },
            fr: {
                flag: '🇫🇷',
                title: 'Aegis-Graph : Réseau d\\'audit souverain',
                subtitle: 'Déposez les documents ou cliquez pour parcourir',
                init_btn: 'Initier l\\'audit',
                docs: 'DOCS',
                pillars: ['Confiance souveraine', 'GraphRAG agentique', 'Confidentialité ZK'],
                agents: ['Expertise Vision', 'Navigateur de Graphe', 'Auditeur Logique'],
                log_init: 'Initialisation du protocole Aegis-Graph...',
                log_ready: 'Système prêt. Veuillez télécharger un document.',
                footer: 'PAR ATLANTA COLLEGE OF LIBERAL ARTS AND SCIENCES (ACLAS COLLEGE)'
            },
            es: {
                flag: '🇪🇸',
                title: 'Aegis-Graph: Red de Auditoría Soberana',
                subtitle: 'Suelte los documentos o haga clic para buscar',
                init_btn: 'Iniciar Auditoría',
                docs: 'DOCS',
                pillars: ['Confianza Soberana', 'GraphRAG Agéntico', 'Privacidad ZK'],
                agents: ['Forense de Visión', 'Navegador de Grafos', 'Auditor Lógico'],
                log_init: 'Iniciando protocolo Aegis-Graph...',
                log_ready: 'Sistema listo. Cargue un documento.',
                footer: 'POR ATLANTA COLLEGE OF LIBERAL ARTS AND SCIENCES (ACLAS COLLEGE)'
            },
            de: {
                flag: '🇩🇪',
                title: 'Aegis-Graph: Souveränes Prüfnetzwerk',
                subtitle: 'Unterlagen ablegen oder zum Durchsuchen klicken',
                init_btn: 'Prüfung einleiten',
                docs: 'DOCS',
                pillars: ['Souveränes Vertrauen', 'Agentisches GraphRAG', 'ZK-Datenschutz'],
                agents: ['Vision Forensik', 'Graph-Navigator', 'Logik-Auditor'],
                log_init: 'Initialisierung des Aegis-Graph-Protokolls...',
                log_ready: 'System bereit. Bitte Dokument hochladen.',
                footer: 'VON ATLANTA COLLEGE OF LIBERAL ARTS AND SCIENCES (ACLAS COLLEGE)'
            },
            jp: {
                flag: '🇯🇵',
                title: 'Aegis-Graph: 主権的監査ネットワーク',
                subtitle: '認証情報をドロップするか、クリックして参照',
                init_btn: '監査を開始',
                docs: 'ドキュメント',
                pillars: ['主権的な信頼', 'エージェント型GraphRAG', 'ゼロ知識プライバシー'],
                agents: ['視覚フォレンジック', 'グラフナビゲーター', 'ロジック監査人'],
                log_init: 'Aegis-Graphプロトコルを初期化中...',
                log_ready: 'システム準備完了。ドキュメントをアップロードしてください。',
                footer: 'アトランタ・リベラルアーツ・サイエンス大学 (ACLAS COLLEGE) 提供'
            },
            kr: {
                flag: '🇰🇷',
                title: 'Aegis-Graph: 주권 감사 네트워크',
                subtitle: '자격 증명을 드롭하거나 클릭하여 탐색',
                init_btn: '감사 시작',
                docs: '문서',
                pillars: ['주권적 신뢰', '에이전트 기반 GraphRAG', '영지식 프라이버시'],
                agents: ['시각 포렌식', '그래프 네비게이터', '논리 감사관'],
                log_init: 'Aegis-Graph 프로토콜 초기화 중...',
                log_ready: '시스템 준비 완료. 문서를 업로드해 주세요.',
                footer: '아틀란타 자유인문과학대학 (ACLAS COLLEGE) 제공'
            },
            zh: {
                flag: '🇭🇰',
                title: 'Aegis-Graph: 主權審計網絡',
                subtitle: '拖放憑證或點擊瀏覽',
                init_btn: '啟動審計',
                docs: '文檔',
                pillars: ['主權信任', '代理式 GraphRAG', '零知識隱私'],
                agents: ['視覺取證', '圖譜導航器', '邏輯審計師'],
                log_init: '正在初始化 Aegis-Graph 協議...',
                log_ready: '系統就緒。請上傳文件进行驗證。',
                footer: '由亞特蘭大文理學院 (ACLAS COLLEGE) 開發'
            },
            ar: {
                flag: '🇸🇦',
                title: 'Aegis-Graph: شبكة التدقيق السيادي',
                subtitle: 'قم بإسقاط المستندات أو انقر للتصفح',
                init_btn: 'بدء التدقيق',
                docs: 'المستندات',
                pillars: ['الثقة السيادية', 'وكيل GraphRAG', 'الخصوصية الصفرية'],
                agents: ['الطب الشرعي البصري', 'ملاح الرسوم البيانية', 'مدقق المنطق'],
                log_init: 'تهيئة بروتوكول Aegis-Graph...',
                log_ready: 'النظام جاهز. يرجى تحميل المستند.',
                footer: 'بواسطة كلية أتلانタ للفنون الليبرالية والعلوم (ACLAS COLLEGE)'
            },
            pt: {
                flag: '🇵🇹',
                title: 'Aegis-Graph: Rede de Auditoria Soberana',
                subtitle: 'Solte as credenciais ou clique para procurar',
                init_btn: 'Iniciar Auditoria',
                docs: 'DOCS',
                pillars: ['Confiança Soberana', 'GraphRAG Agêntico', 'Privacidade ZK'],
                agents: ['Forense de Visão', 'Navegador de Grafos', 'Auditor Lógico'],
                log_init: 'Iniciando o protocolo Aegis-Graph...',
                log_ready: 'Sistema pronto. Carregue um documento.',
                footer: 'POR ATLANTA COLLEGE OF LIBERAL ARTS AND SCIENCES (ACLAS COLLEGE)'
            }
        };'''

content = translations_pattern.sub(correct_translations, content)

# 3. Fix academic keywords encoding artifacts in handleFiles
keywords_pattern = re.compile(r'const academicKeywords = \[.*?\];', re.DOTALL)
correct_keywords = "const academicKeywords = ['aclas', 'transcript', 'diploma', 'harvard', 'stanford', 'degree', '学位', '大学', '成绩单', '证书', 'mba', 'bba', 'phd', 'master', 'bachelor'];"
content = keywords_pattern.sub(correct_keywords, content)

# Final save
with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print('Final Full-Block Restoration Successful!')
