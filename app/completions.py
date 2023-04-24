import requests
import os
import openai

def get_api_key():
    api_key = os.environ["OPENAI_API_KEY"]
    openai.api_key = api_key    # set api key for the openai library
    return api_key

api_key = get_api_key()

# Modality: Business Analyst
intro_sentence = "As a business analyst, I have identified the following key insights:"

# Modality: Investigator
intro_sentence_investigator = "As an investigator, I have compiled the following data:"

# Modality: Financial Analyst
intro_sentence_financial = "As a financial analyst, I have analyzed the financial aspects of the prompt:"

def generate_gpt4_response(prompt, modality, api_key):
    if modality == "business analyst":
        user_prompt = f"Please generate a response about {prompt} from the perspective of a business analyst. Start with this introduction sentence: '{intro_sentence}' Then list 10 key business analysis insights using bullet points with each bullet point shown as a new paragraph."
    elif modality == "investigator":
        user_prompt = f"Please generate a response about {prompt} from the perspective of an investigator. Start with this introduction sentence: '{intro_sentence_investigator}' Then create a table with 3 columns: General Investigative Information, Corporate Information, and Compliance Information. Include 3 sentences in each column."
    elif modality == "financial analyst":
        user_prompt = f"Please generate a response about {prompt} from the perspective of a financial analyst. Start with this introduction sentence: '{intro_sentence_financial}' Then create a table with 3 columns: Assets & Liabilities, Cashflows & Liquidity, and Key Financial Ratios. Include 3 sentences or data points in each column."
    else:
        user_prompt = f"Please provide an answer about {prompt} from the perspective of a {modality}."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.3,  # Decrease temperature to make output more conservative
    )

    formatted_response = response.choices[0]["message"]["content"]
    return formatted_response


if __name__ == "__main__":
    prompt = "your prompt here"
    
    print("Business Analyst:")
    gpt4_analytical = generate_gpt4_response(prompt, "business analyst", api_key)
    print(gpt4_analytical)

    print("\nInvestigator:")
    gpt4_investigative = generate_gpt4_response(prompt, "investigator", api_key)
    print(gpt4_investigative)

    print("\nFinancial Analyst:")
    gpt4_financial = generate_gpt4_response(prompt, "financial analyst", api_key)
    print(gpt4_financial)


