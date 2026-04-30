import requests
import json
import time

def import_global_universities():
    print("🌍 Starting Massive Global University Import (Real Data)...")
    base_url = "https://api.ror.org/organizations?query=university&page="
    all_nodes = []
    
    # We will fetch multiple pages to get a significant volume (e.g., 200+ top global nodes)
    for page in range(1, 11): 
        print(f"  Fetching page {page} from ROR...")
        try:
            response = requests.get(f"{base_url}{page}", timeout=15)
            if response.status_code == 200:
                items = response.json().get('items', [])
                for item in items:
                    node = {
                        "ror_id": item.get('id'),
                        "name": item.get('name'),
                        "country": item.get('country', {}).get('country_name'),
                        "established": item.get('established'),
                        "type": "Verified_Institution",
                        "website": item.get('links', [None])[0] if item.get('links') else None
                    }
                    all_nodes.append(node)
                # Polite rate limiting
                time.sleep(0.5)
            else:
                print(f"  Failed to fetch page {page}")
        except Exception as e:
            print(f"  Error on page {page}: {e}")
            break

    # Save to a dedicated Global Index file
    output_path = 'data/global_academic_index.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_nodes, f, indent=4)
    
    print(f"\n✅ SUCCESS: Imported {len(all_nodes)} real global institutions into the Sovereign Node index.")

if __name__ == "__main__":
    import_global_universities()
