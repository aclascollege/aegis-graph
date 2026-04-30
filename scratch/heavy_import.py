import requests
import json
import time

def massive_import():
    print("🚀 Initiating HEAVY GLOBAL IMPORT (Target: 1000+ Nodes)...")
    all_data = []
    # Fetching 50 pages (1000 records)
    for p in range(1, 51):
        print(f"  Fetching page {p}/50...")
        try:
            r = requests.get(f"https://api.ror.org/organizations?query=university&page={p}", timeout=20)
            if r.status_code == 200:
                items = r.json().get('items', [])
                if not items: break
                for item in items:
                    all_data.append({
                        "ror_id": item.get('id'),
                        "name": item.get('name'),
                        "country": item.get('country', {}).get('country_name'),
                        "established": item.get('established'),
                        "type": "Verified_Institution"
                    })
                # Tight loop but with minimal safety pause
                time.sleep(0.1) 
            else:
                print(f"  Rate limit or error at page {p}")
                break
        except Exception as e:
            print(f"  Connection error: {e}")
            break
            
    with open('data/global_academic_index.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=4)
    print(f"\n✅ COMPLETED: {len(all_data)} REAL universities now integrated into the Sovereign Node.")

if __name__ == "__main__":
    massive_import()
