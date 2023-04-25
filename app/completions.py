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
bullet_points = [
    "• Bullet point 1",
    "• Bullet point 2",
    "• Bullet point 3",
    "• Bullet point 4",
    "• Bullet point 5",
    "• Bullet point 6",
    "• Bullet point 7",
    "• Bullet point 8",
    "• Bullet point 9",
    "• Bullet point 10",
]

# Modality: Investigator
intro_sentence_investigator = "As an investigator, I have compiled the following data:"
table_investigator = """
| General Investigative Information | Corporate Information | Compliance Information |
|-----------------------------------|------------------------|------------------------|
| • Sentence 1                     | • Sentence 1           | • Sentence 1           |
| • Sentence 2                     | • Sentence 2           | • Sentence 2           |
| • Sentence 3                     | • Sentence 3           | • Sentence 3           |
"""

# Modality: Financial Analyst
intro_sentence_financial = "As a financial analyst, I have analyzed the financial aspects of the prompt:"
table_financial = """
| Assets & Liabilities          | Cashflows & Liquidity      | Key Financial Ratios     |
|-------------------------------|-----------------------------|--------------------------|
| • Sentence 1                 | • Sentence 1                | • Ratio 1                |
| • Sentence 2                 | • Sentence 2                | • Ratio 2                |
| • Sentence 3                 | • Sentence 3                | • Ratio 3                |
"""

def format_business_analyst_response(response_text):
    formatted_response = response_text.replace("•", "\n•")
    return formatted_response

def format_investigator_response(response_text):
    formatted_response = response_text.replace("| ", "").replace(" |", "").replace(" | ", "\n")
    return formatted_response

def format_financial_response(response_text):
    formatted_response = response_text.replace("| ", "").replace(" |", "").replace(" | ", "\n")
    return formatted_response



def generate_gpt4_response(prompt, modality, api_key):
    if modality == "business analyst":
        user_prompt = f"Please generate a response about {prompt} from the perspective of a business analyst. Start with this introduction sentence: '{intro_sentence}' Then list 10 key business analysis insights using bullet points. Format each bullet point as a new paragraph and ensure the content is relevant to the role of a business analyst."
    elif modality == "investigator":
        user_prompt = f"Please generate a response about {prompt} from the perspective of an investigator. Start with this introduction sentence: '{intro_sentence_investigator}' Then create a table with 3 columns: General Investigative Information, Corporate Information, and Compliance Information. Include 3 sentences in each column, and make sure the information is relevant to an investigator's perspective."
    elif modality == "financial analyst":
        user_prompt = f"Please generate a response about {prompt} from the perspective of a financial analyst. Start with this introduction sentence: '{intro_sentence_financial}' Then create a table with 3 columns: Assets & Liabilities, Cashflows & Liquidity, and Key Financial Ratios. Include 3 sentences or data points in each column, and ensure the information is relevant to a financial analyst's perspective."
    else:
        raise ValueError("Modality must be one of 'business analyst', 'investigator', or 'financial analyst'.")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"You are a {modality}."},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.3,  # Decrease temperature to make output more conservative
    )

    formatted_response = response.choices[0]["message"]["content"]
    
    if modality == "business analyst":
        formatted_response = format_business_analyst_response(formatted_response)
    elif modality == "investigator":
        formatted_response = format_investigator_response(formatted_response)
    elif modality == "financial analyst":
        formatted_response = format_financial_response(formatted_response)

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


