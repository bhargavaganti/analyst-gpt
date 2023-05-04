import os
import re
import requests

def validate_company_name(company_name):
    if not re.match(r'^[a-zA-Z0-9\s.,\-]+$', company_name):
        raise ValueError("Invalid company name. The name should only contain letters, digits, spaces, and common punctuation marks like periods, commas, and hyphens.")
    
    crunchbase_api_key = os.environ.get('CRUNCHBASE_API_KEY')
    search_url = f'https://api.crunchbase.com/api/v4/searches/organizations?query={company_name}&user_key={crunchbase_api_key}'
    
    try:
        response = requests.get(search_url)

        if response.status_code == 200:
            response_data = response.json()
            if response_data['data']['paging']['total_items'] == 0:
                raise ValueError("Company not found. Please provide a valid company name.")
        else:
            raise Exception(f"Error: Received a non-200 status code {response.status_code} from the Crunchbase API.")

    except Exception as e:
        raise Exception(f"Error while validating company name: {str(e)}")

    return company_name


