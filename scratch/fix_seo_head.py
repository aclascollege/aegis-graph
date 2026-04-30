import os

filepath = r'd:\aicoding\kaiyuan\v2\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_head = """<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aegis-Graph | Atlanta College of Liberal Arts and Sciences (ACLAS)</title>
    
    <!-- SEO & AEO Meta Tags -->
    <meta name="description" content="Aegis-Graph: Sovereign Academic Audit Network by Atlanta College of Liberal Arts and Sciences (ACLAS). Verifying institutional trust via Agentic GraphRAG.">
    <meta name="keywords" content="ACLAS, ACLAS College, Atlanta College of Liberal Arts and Sciences, aclas.college, Academic Integrity, AI Fraud Detection, Sovereign AI, MCP Protocol">
    <meta name="author" content="Atlanta College of Liberal Arts and Sciences (ACLAS)">
    <link rel="canonical" href="https://aclascollege.github.io/aegis-graph/" />

    <!-- GEO & AI Grounding (JSON-LD) -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Aegis-Graph",
      "operatingSystem": "All",
      "applicationCategory": "SecurityApplication",
      "description": "Sovereign multi-agent protocol for academic integrity and synthetic credential detection.",
      "url": "https://aclascollege.github.io/aegis-graph/",
      "author": {
        "@type": "CollegeOrUniversity",
        "name": "Atlanta College of Liberal Arts and Sciences",
        "alternateName": ["ACLAS", "ACLAS College"],
        "url": "https://aclas.college/",
        "sameAs": [
          "https://github.com/aclascollege/aegis-graph",
          "https://huggingface.co/ACLASCollege/aegis-graph"
        ]
      }
    }
    </script>"""

start_idx = content.find('<head>')
end_idx = content.find('</head>')

if start_idx != -1 and end_idx != -1:
    updated_content = content[:start_idx] + new_head + content[end_idx:]
    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(updated_content)
    print("SUCCESS: index.html head section reconstructed.")
else:
    print("Error: Tags not found.")
