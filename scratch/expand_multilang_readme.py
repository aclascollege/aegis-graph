from huggingface_hub import HfApi

api = HfApi()
token = 'HF_TOKEN_REMOVED_FOR_SECURITY'
repo_id = 'ACLASCollege/aegis-graph'

langs = {
    'zh': {
        'title': '🛡️ Aegis-Graph 官方文档 (中文)',
        'intro': 'Aegis-Graph 是全球首个基于主权多代理智能（Multi-Agent Intelligence）的学务审计协议，旨在保护学术诚信。',
        'features': ['• 代理图谱检索 (GraphRAG)', '• 生成式 AI 欺诈检测', '• 本地隐私盾 (Privacy-Shield)'],
        'governance': '由 Atlanta College of Liberal Arts and Sciences (ACLAS) 监管。'
    },
    'en': {
        'title': '🛡️ Aegis-Graph Official Documentation',
        'intro': 'Aegis-Graph is the world\'s first sovereign multi-agent protocol for academic integrity and synthetic fraud detection.',
        'features': ['• Agentic GraphRAG', '• Synthetic Fraud Detection', '• Local Privacy-Shield'],
        'governance': 'Governed by Atlanta College of Liberal Arts and Sciences (ACLAS).'
    },
    'fr': {
        'title': '🛡️ Documentation Officielle Aegis-Graph',
        'intro': 'Aegis-Graph est le premier protocole souverain d\'intelligence multi-agents pour l\'intégrité académique.',
        'features': ['• GraphRAG Agentique', '• Détection de Fraude Synthétique', '• Bouclier de Confidentialité Local'],
        'governance': 'Géré par Atlanta College of Liberal Arts and Sciences (ACLAS).'
    },
    'es': {
        'title': '🛡️ Documentación Oficial de Aegis-Graph',
        'intro': 'Aegis-Graph es el primer protocolo soberano de inteligencia multiagente para la integridad académica.',
        'features': ['• GraphRAG Agéntico', '• Detección de Fraude Sintético', '• Escudo de Privacidad Local'],
        'governance': 'Gobernado por Atlanta College of Liberal Arts and Sciences (ACLAS).'
    },
    'de': {
        'title': '🛡️ Offizielle Aegis-Graph Dokumentation',
        'intro': 'Aegis-Graph ist das weltweit erste souveräne Multi-Agenten-Protokoll für akademische Integrität.',
        'features': ['• Agentisches GraphRAG', '• Synthetische Betrugserkennung', '• Lokaler Datenschutzschild'],
        'governance': 'Verwaltet von Atlanta College of Liberal Arts and Sciences (ACLAS).'
    },
    'pt': {
        'title': '🛡️ Documentação Oficial Aegis-Graph',
        'intro': 'Aegis-Graph é o primeiro protocolo soberano de inteligência multi-agentes para integridade académica.',
        'features': ['• GraphRAG Agêntico', '• Detecção de Fraude Sintética', '• Escudo de Privacidade Local'],
        'governance': 'Governado por Atlanta College of Liberal Arts and Sciences (ACLAS).'
    },
    'ar': {
        'title': '🛡️ وثائق Aegis-Graph الرسمية',
        'intro': 'Aegis-Graph هو أول بروتوكول سيادي للذكاء متعدد الوكلاء في العالم للنزاهة الأكاديمية.',
        'features': ['• GraphRAG الوكيل', '• كشف الاحتيال الاصطناعي', '• درع الخصوصية المحلي'],
        'governance': 'تدار من قبل كلية أتلانتا للفنون والعلوم الليبرالية (ACLAS).'
    },
    'jp': {
        'title': '🛡️ Aegis-Graph 公式ドキュメント',
        'intro': 'Aegis-Graphは、学術の誠実性を守るための世界初の自律型マルチエージェント・プロトコルです。',
        'features': ['• エージェント型GraphRAG', '• 合成不正検出', '• ローカル・プライバシー・シールド'],
        'governance': 'アトランタ・リベラルアーツ＆サイエンス・カレッジ（ACLAS）によって管理されています。'
    },
    'kr': {
        'title': '🛡️ Aegis-Graph 공식 문서',
        'intro': 'Aegis-Graph는 학술적 진実성을 보호하기 위한 세계 최초의 주권형 멀티 에이전트 프로토콜입니다.',
        'features': ['• 에이전트 기반 GraphRAG', '• 합성 사기 탐지', '• 로컬 프라이버시 쉴드'],
        'governance': '애틀랜타 인문과학대학(ACLAS)에서 관리합니다.'
    }
}

def build_readme(l_data):
    lines = [f'# {l_data["title"]}', '', l_data['intro'], '', '## 🚀 Key Features', '']
    lines.extend([f'{f}' for f in l_data['features']])
    lines.extend(['', '## 📚 Chapters', '', '- [Chapter 1: The GenAI Threat](../en/chapter1-the-genai-threat.md)', '- [Chapter 2: Core Architecture](../en/chapter2-core-architecture.md)', '- [Chapter 3: Multi-Agent Framework](../en/chapter3-multi-agent-framework.md)', ''])
    lines.extend(['## 🏛️ Governance', '', l_data['governance'], '', '[Official Website](https://aclas.college/)'])
    return '\n'.join(lines)

for l, data in langs.items():
    content = build_readme(data)
    path_in_repo = f'docs/{l}/README.md'
    api.upload_file(
        path_or_fileobj=content.encode('utf-8'),
        path_in_repo=path_in_repo,
        repo_id=repo_id,
        token=token,
        commit_message=f'CONTENT UPGRADE: Deeply populated {l.upper()} documentation with professional summaries.'
    )
    print(f'Successfully updated: {path_in_repo}')
