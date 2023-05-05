import requests
import os

def test_crunchbase_api(api_key):
    url = f"https://api.crunchbase.com/api/v4/entities/organizations?user_key={api_key}&filter[organization_types]=company&filter[name]=Apple"
    response = requests.get(url)

    if response.status_code == 200:
        print("API key is valid and working!")
    else:
        print(f"Error: Received a non-200 status code {response.status_code} from the Crunchbase API. Please check your API key.")

if __name__ == "__main__":
    crunchbase_api_key = os.environ.get('CRUNCHBASE_API_KEY')
    test_crunchbase_api(crunchbase_api_key)
