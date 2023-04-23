import requests
import os
import openai

def get_api_key():
    api_key = os.environ["OPENAI_API_KEY"]
    openai.api_key = api_key    # set the api key for the openai library
    return api_key

api_key = get_api_key()
prompt = "JP Morgan"

def generate_gpt4_response(prompt, api_key):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt}
        ],
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0]["message"]["content"]

if __name__ == "__main__":
    print("\Business Analyst:")
    gpt4 = generate_gpt4_response(prompt, api_key)
    print(gpt4)