import requests
import json

class GraphNavigator:
    def __init__(self, local_index_path='data/global_academic_full_index_v2.json'):
        self.local_index_path = local_index_path
        self.api_url = "https://api.ror.org/organizations"
        try:
            with open(local_index_path, 'r', encoding='utf-8') as f:
                self.local_cache = json.load(f)
        except:
            self.local_cache = []

    def verify_institution(self, name):
        # 1. Search Local 5000+ Index
        for item in self.local_cache:
            if name.lower() in item['name'].lower():
                return item

        # 2. Dynamic Fallback to Global ROR Registry (102,000+ Nodes)
        try:
            response = requests.get(f"{self.api_url}?query={name}", timeout=10)
            if response.status_code == 200:
                results = response.json().get('items', [])
                if results:
                    top_result = results[0]
                    return {
                        'ror_id': top_result.get('id'),
                        'name': top_result.get('names', [{}])[0].get('value'),
                        'country': top_result.get('locations', [{}])[0].get('geonames_details', {}).get('country_name'),
                        'status': 'Verified_via_Global_Link'
                    }
        except:
            pass
        return None

if __name__ == "__main__":
    nav = GraphNavigator()
    # Testing for University of Balamand (Lebanon) - Pure Global Search
    res = nav.verify_institution("University of Balamand")
    if res:
        print("MATCH FOUND VIA GLOBAL ROR LINK:")
        print(f"Institution: {res['name']}")
        print(f"ROR ID: {res['ror_id']}")
        print(f"Status: {res['status']}")
