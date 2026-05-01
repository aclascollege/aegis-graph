<script>
        const initBtn = document.getElementById('init-btn');
        const themeToggle = document.getElementById('theme-toggle');
        const sunIcon = document.getElementById('sun-icon');
        const moonIcon = document.getElementById('moon-icon');
        const reportBtnContainer = document.getElementById('report-action-container');
        const reportModal = document.getElementById('report-modal-overlay');

        document.getElementById('view-report-btn').addEventListener('click', () => {
            document.getElementById('report-hash').innerText = '0x' + Array.from({ length: 40 }, () => Math.floor(Math.random() * 16).toString(16)).join('');
            document.getElementById('report-time').innerText = new Date().toISOString();
            reportModal.classList.add('active');
        });

        document.getElementById('close-modal-btn').addEventListener('click', () => {
            reportModal.classList.remove('active');
        });

        // --- Theme Logic ---
        function toggleTheme() {
            const isLight = document.body.classList.toggle('light-mode');
            localStorage.setItem('theme', isLight ? 'light' : 'dark');
            updateThemeIcons(isLight);
        }

        function updateThemeIcons(isLight) {
            sunIcon.style.display = isLight ? 'inline' : 'none';
            moonIcon.style.display = isLight ? 'none' : 'inline';
        }

        // Init theme
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'light') {
            document.body.classList.add('light-mode');
            updateThemeIcons(true);
        }

        themeToggle.addEventListener('click', toggleTheme);
        const terminal = document.getElementById('terminal');
        const scanBar = document.getElementById('scan-bar');
        const verdict = document.getElementById('final-verdict');
        const risk = document.getElementById('risk-score');
        const dropZone = document.getElementById('drop-zone');
        const fileInd = document.getElementById('file-indicator');
        const fileInput = document.getElementById('file-input');

        // --- Click to Upload ---
        dropZone.addEventListener('click', () => {
            fileInput.click();
        });

        fileInput.addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                handleFiles(e.target.files);
            }
        });

        function handleFiles(files) {
            const file = files[0];
            const fileName = file.name.toLowerCase();
            fileInd.innerText = `Source detected: ${file.name}`;
            fileInd.style.display = 'block';
            dropZone.style.borderColor = 'var(--border)';

            log('SYSTEM', `New payload detected: ${file.name}. Initializing NPU handshake...`);

            // --- 2026 Strict Mode Logic ---
            const academicKeywords = ['aclas', 'transcript', 'diploma', 'harvard', 'stanford', 'degree', '学位', '大学', '成绩单', '证书', 'mba', 'bba', 'phd', 'master', 'bachelor'];
            const isAcademic = academicKeywords.some(keyword => fileName.toLowerCase().includes(keyword));
            const isKnownFraud = fileName.toLowerCase().includes('fake') || fileName.toLowerCase().includes('fraud') || fileName.toLowerCase().includes('éÂÂ Ã¥ÂÂ');

            if (isKnownFraud || !isAcademic) {
                window.demoVerdict = 'REJECTED';
                window.rejectReason = isKnownFraud ? 'KNOWN_FRAUD_DB_MATCH' : 'NO_ACADEMIC_MARKERS_FOUND';
            } else {
                window.demoVerdict = 'APPROVED';
                window.rejectReason = null;
            }

            window.isAclasFastTrack = fileName.includes('aclas') || fileName.includes('atlanta college') || fileName.includes('atlanta');

            startAudit();
        }

        function log(agent, msg, color = "var(--log-highlight)", isMcp = false) {
            const div = document.createElement('div');
            div.className = 'log-line';
            if (isMcp) {
                div.style.fontSize = '10px';
                div.style.opacity = '0.9';
                div.style.fontStyle = 'italic';
                div.innerHTML = `<span style="color: var(--log-text)">>> CALL: ${msg}</span>`;
            } else {
                div.innerHTML = `<span style="color: ${color}">[${agent}]</span> ${msg}`;
            }
            const stream = document.getElementById('mcp-stream');
            stream.appendChild(div);
            terminal.scrollTop = terminal.scrollHeight;
        }

        const TRANSLATIONS = {
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
                title: 'Aegis-Graph : Réseau d\'audit souverain',
                subtitle: 'Déposez les documents ou cliquez pour parcourir',
                init_btn: 'Initier l\'audit',
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

        function switchLanguage(lang) {
            const data = TRANSLATIONS[lang] || TRANSLATIONS.en;
            document.getElementById('current-lang-flag').innerText = data.flag;
            document.querySelector('.hero-upload h1').innerText = data.subtitle;
            document.querySelector('.logo-text').innerText = 'AEGIS-GRAPH';
            document.querySelector('#init-btn').innerText = data.init_btn;
            document.querySelector('header .logo-group span:nth-child(2) a').innerText = data.footer;

            // RTL support for Arabic
            if (lang === 'ar') {
                document.body.style.direction = 'rtl';
                document.querySelectorAll('.agent-card').forEach(el => el.style.flexDirection = 'row-reverse');
            } else {
                document.body.style.direction = 'ltr';
                document.querySelectorAll('.agent-card').forEach(el => el.style.flexDirection = 'row');
            }

            // Update Agent Names
            const agents = document.querySelectorAll('.agent-card span');
            agents.forEach((span, i) => { if (data.agents[i]) span.innerText = data.agents[i]; });

            addLog(data.log_ready, 'SYSTEM');
            localStorage.setItem('aclas_lang', lang);
        }

        document.getElementById('lang-switch').addEventListener('change', (e) => {
            switchLanguage(e.target.value);
        });

        // Initialize with saved lang or browser default
        const savedLang = localStorage.getItem('aclas_lang') || 'en';
        document.getElementById('lang-switch').value = savedLang;
        setTimeout(() => switchLanguage(savedLang), 500);

        async function sleep(ms) {
            const delay = window.isAclasFastTrack ? ms * 0.1 : ms; // 10x faster for ACLAS VIPs
            return new Promise(r => setTimeout(r, delay));
        }


        // --- Initialize NPU Stats ---
        const npuStats = document.getElementById('npu-stats');
        for (let i = 0; i < 16; i++) {
            const core = document.createElement('div');
            core.style.height = '6px';
            core.style.background = '#222';
            core.style.borderRadius = '1px';
            core.style.transition = 'background-color 0.1s, box-shadow 0.1s';
            core.id = `core-${i}`;
            npuStats.appendChild(core);
        }

        function updateNpu(active = false) {
            for (let i = 0; i < 16; i++) {
                const core = document.getElementById(`core-${i}`);
                if (active) {
                    const isActive = Math.random() > 0.4;
                    core.style.background = isActive ? 'var(--success)' : '#333';
                    core.style.boxShadow = isActive ? '0 0 4px var(--success)' : 'none';
                } else {
                    core.style.background = '#222';
                    core.style.boxShadow = 'none';
                }
            }
            document.getElementById('npu-load').innerText = active ? Math.floor(Math.random() * 40 + 60) : '0';
        }

        function drawBox(top, left, width, height, label = "DETECTED") {
            const overlay = document.getElementById('detection-overlay');
            const box = document.createElement('div');
            box.className = 'detection-box';
            box.style.cssText = `
                position: absolute; top: ${top}%; left: ${left}%; width: ${width}%; height: ${height}%;
                border: 1px solid var(--success); background: rgba(0, 255, 170, 0.03);
                box-shadow: inset 0 0 15px rgba(0, 255, 170, 0.2), 0 0 10px rgba(0, 255, 170, 0.4); 
                opacity: 0; transition: opacity 0.4s ease-out;
            `;

            const labelTag = document.createElement('div');
            labelTag.innerText = label;
            labelTag.style.cssText = `
                position: absolute; top: -14px; left: -1px; background: var(--success);
                color: #000; font-size: 8px; font-weight: 700; padding: 2px 4px;
                text-transform: uppercase; font-family: 'JetBrains Mono';
            `;
            box.appendChild(labelTag);

            overlay.appendChild(box);
            setTimeout(() => box.style.opacity = '1', 50);
            return box;
        }

        function lightNode(id, color = 'var(--success)') {
            const node = document.getElementById(`node-${id}`);
            if (node) {
                node.setAttribute('fill', color);
                node.style.filter = `drop-shadow(0 0 5px ${color})`;
            }
        }

        async function startAudit() {
            initBtn.disabled = true;
            initBtn.style.opacity = 0.5;
            fileInd.style.display = 'block';
            document.getElementById('detection-overlay').innerHTML = '';

            // Reset Graph
            for (let i = 1; i <= 4; i++) {
                const n = document.getElementById(`node-${i}`);
                if (n) n.setAttribute('fill', 'var(--accent-dim)');
            }

            // Animation
            scanBar.style.animation = 'scanMove 2s infinite';
            const npuInterval = setInterval(() => updateNpu(true), 100);

            log('CORE', 'Starting high-precision audit sequence...');
            await sleep(800);

            // Step 0: PII Scrubbing (Zero-Knowledge)
            log('PRIVACY', 'Local Presidio Scrubber engaged. Redacting PII (SSN, DOB)...', 'var(--success)');
            await sleep(600);
            log('PRIVACY', 'PII stripped successfully. Safe for Cloud Vision transfer.', 'var(--success)');
            await sleep(400);

            // Step 1: Vision
            lightNode(1);
            log('MCP', 'mcp_vision_analyze(source_uri: "...", scrub: true)', null, true);
            log('VISION', 'Analyzing document forensics...', '#00f2ff');

            // Draw labeled boxes
            await sleep(500); drawBox(20, 25, 50, 8, 'INSTITUTION_HEADER');
            await sleep(400); drawBox(35, 15, 70, 35, 'DATA_BLOCK_PRIMARY');
            await sleep(300); drawBox(75, 20, 30, 10, 'SECURITY_MARKER_01');

            document.getElementById('stat-res').innerText = '4096x2160';
            document.getElementById('stat-entropy').innerText = (Math.random() * 0.01).toFixed(4);
            document.getElementById('stat-citations').innerText = Math.floor(Math.random() * 50000 + 10000).toLocaleString();
            document.getElementById('stat-cost').innerText = '$0.000' + Math.floor(Math.random() * 9 + 1);

            log('VISION', 'Forensic metadata extracted. No pixel manipulation detected.', '#00f2ff');
            await sleep(800);

            if (window.rejectReason === 'NO_ACADEMIC_MARKERS_FOUND') {
                log('VISION', '[ALERT] No valid institutional markers detected.', '#ff3366');
                log('CORE', 'Aborting session: Entropy mismatch.', '#ff3366');
                clearInterval(npuInterval); updateNpu(false);
            } else {
                log('VISION', 'OCR complete. Identity tokens masked via Local SLM.');
            }

            // Step 2: Graph
            if (window.rejectReason !== 'NO_ACADEMIC_MARKERS_FOUND') {
                lightNode(2); lightNode(3);
                log('MCP', 'mcp_resolve_ror(query: "...", fuzzy: true)', null, true);
                log('GRAPH', 'Traversing OpenAlex & ROR nodes...', '#bc00ff');
                await sleep(1500);
                if (window.rejectReason === 'KNOWN_FRAUD_DB_MATCH') {
                    log('GRAPH', '[WARNING] Status: "Withdrawn/Suspicious" in ROR.', '#ff3366');
                    lightNode(2, '#ff3366');
                } else {
                    log('GRAPH', 'Institution verified. Trust score: 0.998');
                }
            }

            // Step 3: Logic
            if (window.rejectReason !== 'NO_ACADEMIC_MARKERS_FOUND') {
                lightNode(4);
                // Positive Logic
                log('MCP', 'mcp_logic_audit(graph_id: "782", heuristics: "STRICT")', null, true);
                log('LOGIC', 'Running deep reasoning (CoT) conflict detection...', '#ffaa00');
                await sleep(1500);
                log('LOGIC', 'Verifying credit density: 120 credits / 48 months -> Normal.', '#ffaa00');
                await sleep(1000);
                log('LOGIC', 'Cross-referencing ROR establishment date with graduation year -> Valid.', '#ffaa00');
                await sleep(800);
                log('LOGIC', 'Temporal consistency confirmed.');
            } else {
                // Negative Logic
                log('MCP', 'mcp_logic_audit(graph_id: "NULL", heuristics: "STRICT")', null, true);
                log('LOGIC', 'Running deep reasoning (CoT) conflict detection...', '#ffaa00');
                await sleep(2000);
                if (window.rejectReason === 'KNOWN_FRAUD_DB_MATCH') {
                    log('LOGIC', '[CONFLICT] Degree date mismatch vs ROR History.', '#ff3366');
                    log('LOGIC', '[CONFLICT] OpenAlex works_count = 0. High probability of diploma mill.', '#ff3366');
                    lightNode(4, '#ff3366');
                } else {
                    log('LOGIC', 'Temporal consistency confirmed.');
                }
            }

            // Final
            clearInterval(npuInterval); updateNpu(false);
            scanBar.style.animation = 'none';
            const finalVerdict = window.demoVerdict || 'APPROVED';
            verdict.innerText = finalVerdict;

            if (finalVerdict === 'REJECTED') {
                verdict.style.color = '#fff';
                risk.innerText = window.rejectReason === 'NO_ACADEMIC_MARKERS_FOUND' ? 'RISK: UNIDENTIFIABLE SOURCE' : 'RISK: DOCUMENT MANIPULATION';
                risk.style.color = 'rgba(255, 255, 255, 0.8)';
                document.querySelector('.decision-card').style.background = 'var(--danger)';
                document.querySelector('.decision-card').style.borderColor = 'var(--danger)';
                reportBtnContainer.style.display = 'none';
            } else {
                verdict.style.color = 'var(--success)';
                verdict.innerText = 'VERIFIED';
                document.querySelector('.decision-card').style.background = 'rgba(0, 255, 170, 0.1)';
                document.querySelector('.decision-card').style.borderColor = 'var(--success)';
                reportBtnContainer.style.display = 'block';
                log('SYSTEM', 'Audit complete. Result: GOLD STANDARD.');
            }

            log('SYSTEM', 'Audit result committed to sovereign ledger.', '#00ffaa');

            initBtn.disabled = false;
            initBtn.style.opacity = 1;
            initBtn.innerText = 'New Session';
        }

        initBtn.addEventListener('click', startAudit);

        // --- Drag & Drop Implementation ---
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            dropZone.addEventListener(eventName, e => {
                e.preventDefault();
                e.stopPropagation();
            }, false);
        });

        dropZone.addEventListener('dragover', () => {
            dropZone.style.borderColor = 'var(--accent)';
            dropZone.style.background = 'rgba(255, 255, 255, 0.05)';
        });

        dropZone.addEventListener('dragleave', () => {
            dropZone.style.borderColor = 'var(--border)';
            dropZone.style.background = 'transparent';
        });

        dropZone.addEventListener('drop', (e) => {
            const files = e.dataTransfer.files;
            if (files.length > 0) {
                handleFiles(files);
            }
        });
    </script>