import subprocess
import re
import os

def reconstruct():
    print("STARTING: High-Fidelity UI Reconstruction...")
    
    # 1. Fetch raw GOOD data from Git
    try:
        raw_data = subprocess.check_output(['git', 'show', '2e495b1:index.html'])
        content = raw_data.decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching git history: {e}")
        return

    # 2. Extract Parts
    style_match = re.search(r'<style>.*?</style>', content, re.DOTALL)
    body_match = re.search(r'<body>(.*?)</body>', content, re.DOTALL)
    script_matches = re.findall(r'<script>.*?</script>', content, re.DOTALL)
    
    if not style_match or not body_match:
        print("CRITICAL ERROR: Failed to locate core UI blocks in history.")
        return

    css = style_match.group(0)
    body = body_match.group(1)
    # The longest script is usually the dashboard logic
    main_js = max(script_matches, key=len) if script_matches else ""

    # 3. Inject 102K Data & SEO
    body = body.replace('4,000+', '102,000+ (Dynamic Global)')
    
    # 4. Assemble the Final Masterpiece
    final_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aegis-Graph | Atlanta College of Liberal Arts and Sciences (ACLAS)</title>
    <meta name="description" content="Aegis-Graph: Sovereign Academic Audit Network by Atlanta College of Liberal Arts and Sciences (ACLAS). Verifying institutional trust via Agentic GraphRAG.">
    {css}
</head>
<body>
    {body}
    {main_js}
    <!-- CACHE_BUSTER_RECON_V3 -->
</body>
</html>"""

    # 5. Write with LOCK-TIGHT UTF-8
    with open('index.html', 'w', encoding='utf-8', newline='\n') as f:
        f.write(final_html)
    
    print(f"SUCCESS: Reconstruction complete. Size: {len(final_html)} chars.")

if __name__ == "__main__":
    reconstruct()
