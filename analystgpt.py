import requests
import os
import openai
 
def get_api_key():
    api_key = os.environ["OPENAI_API_KEY"]
    openai.api_key = api_key    # set the api key for the openai library
    return api_key

api_key = get_api_key()

prompt = "JP Morgan"

def generate_report(prompt, api_key):
    url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    data = {
        "prompt": f"Create a consultant-type report based on the following prompt: {prompt}",
        "max_tokens": 1000,
        "n": 1,
        "stop": None,
        "temperature": 0.7,
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        print(response.content)  # obtain and print error messages

    response.raise_for_status()

    generated_text = response.json()["choices"][0]["text"].strip()
    return generated_text

if __name__ == "__main__":
    report = generate_report(prompt, api_key)
    print(report)


