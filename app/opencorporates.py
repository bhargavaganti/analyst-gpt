'''
import re
import requests

def validate_company_name(company_name):
    if not re.match(r'^[a-zA-Z0-9\s.,\-]+$', company_name):
        raise ValueError("Invalid company name. The name should only contain letters, digits, spaces, and common punctuation marks like periods, commas, and hyphens.")
    
    opencorporates_api_key = 'your_opencorporates_api_key'
    search_url = f'https://api.opencorporates.com/v0.4/companies/search?q={company_name}&api_token={opencorporates_api_key}'
    
    try:
        response = requests.get(search_url)
        response_data = response.json()

        if response.status_code != 200:
            raise Exception("Error while accessing the OpenCorporates API")

        if response_data['results']['total_count'] == 0:
            raise ValueError("Company not found. Please provide a valid company name.")
    except Exception as e:
        raise Exception(f"Error while validating company name: {str(e)}")

    return company_name
'''
