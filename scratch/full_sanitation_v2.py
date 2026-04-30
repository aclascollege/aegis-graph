import os
import re

filepath = r'd:\aicoding\kaiyuan\v2\index.html'

with open(filepath, 'rb') as f:
    data = f.read()

# Use string for easier replacement, then encode back to utf-8
try:
    content = data.decode('utf-8')
except UnicodeDecodeError:
    content = data.decode('latin-1')

# 1. Standard HTML Head & Header
head_start_marker = '<!DOCTYPE html>'
head_end_marker = '<!-- JSON-LD Structured Data'

header_block = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
<meta name="description"
    content="Aegis-Graph is the world's first sovereign academic audit network using Agentic GraphRAG and Multi-Agent Intelligence to verify credentials. Engineered by Atlanta College of Liberal Arts and Sciences (ACLAS College).">
<meta name="keywords"
    content="Aegis-Graph, ACLAS College, Atlanta College of Liberal Arts and Sciences, Accredited College, Legitimate University, Authorized Degrees, Academic Integrity, GraphRAG, AI Fraud Detection, MCP Protocol, Sovereign AI">
<meta name="author" content="Atlanta College of Liberal Arts and Sciences (ACLAS)">

<!-- AI Engine Optimization (llm.txt) -->
<link rel="help" href="llm.txt">

<!-- Open Graph / Facebook -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://aclascollege.github.io/aegis-graph/">
<meta property="og:title" content="Aegis-Graph | Sovereign Academic Audit Network">
<meta property="og:description"
    content="Revolutionizing Academic Integrity through Agentic GraphRAG and Multi-Agent Intelligence. Powered by ACLAS College.">'''

head_start_idx = content.find(head_start_marker)
head_end_idx = content.find(head_end_marker)

if head_start_idx != -1 and head_end_idx != -1:
    content = header_block + content[head_end_idx:]

# 2. Fix the TRANSLATIONS object
trans_start_marker = 'const TRANSLATIONS = {'
trans_end_marker = '        function switchLanguage'

correct_trans = '''const TRANSLATIONS = {
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
                footer: 'بواسطة كلية أتلانتا للفنون الليبرالية والعلوم (ACLAS COLLEGE)'
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
        };

'''

trans_start_idx = content.find(trans_start_marker)
trans_end_idx = content.find(trans_end_marker)

if trans_start_idx != -1 and trans_end_idx != -1:
    content = content[:trans_start_idx] + correct_trans + content[trans_end_idx:]

# 3. Global character fixes
content = content.replace('\ufffd', '') # Remove all replacement characters
content = content.replace('GraphRAG—a', 'GraphRAG—a') # Ensure em-dash
content = content.replace('agents—to', 'agents—to')

# Fix Upload Icon
content = re.sub(r'<div class="upload-icon">.*?</div>', '<div class="upload-icon">🔍</div>', content)

with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)

print('Full-File Sanitation (Take 2) Complete.')
