import requests
import os
import openai

def get_api_key():
    api_key = os.environ["OPENAI_API_KEY"]
    openai.api_key = api_key    # set api key for the openai library
    return api_key

api_key = get_api_key()

def generate_gpt4_response(prompt, modality, api_key):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"Please provide an answer about {prompt} from the perspective of a {modality}."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,    # temp controls randomness of the model's output, lower temperature = more conservative response
    )

    return response.choices[0]["message"]["content"]

if __name__ == "__main__":
    print("Business Analyst:")
    gpt4_analytical = generate_gpt4_response(prompt, "business analyst", api_key)
    print(gpt4_analytical)

    print("\nInvestigator:")
    gpt4_investigative = generate_gpt4_response(prompt, "investigator", api_key)
    print(gpt4_investigative)

    print("\nFinancial Analyst:")
    gpt4_financial = generate_gpt4_response(prompt, "financial analyst", api_key)
    print(gpt4_financial)
