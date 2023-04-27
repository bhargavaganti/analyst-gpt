import requests
import os
import openai
import re

def get_api_key():
    api_key = os.environ["OPENAI_API_KEY"]
    openai.api_key = api_key    # set api key for the openai library
    return api_key

api_key = get_api_key()

# Modality: Business Analyst
intro_sentence = "As a business analyst, I have identified the following key insights:"
bullet_points = """
• Bullet point 1
• Bullet point 2
• Bullet point 3
• Bullet point 4
• Bullet point 5
• Bullet point 6
• Bullet point 7
• Bullet point 8
• Bullet point 9
• Bullet point 10
"""

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

def extract_template_structure(template):
    placeholders = []
    for line in template.split('\n'):
        placeholders.extend(re.findall(r'(• Bullet point \d+|• Sentence \d+|• Ratio \d+)', line))
    return placeholders

def generate_gpt4_response(prompt, modality, api_key):
    if modality == "business analyst":
        user_prompt = f"Please generate a response about {prompt} from the perspective of a business analyst. Start with this introduction sentence: '{intro_sentence}' Then list 10 key business analysis insights using bullet points. Format each bullet point as a new paragraph and ensure the content is relevant to the role of a business analyst."
        template = bullet_points
    elif modality == "investigator":
        user_prompt = f"Please generate a response about {prompt} from the perspective of an investigator. Start with this introduction sentence: '{intro_sentence_investigator}' Then create a table with 3 columns: General Investigative Information, Corporate Information, and Compliance Information. Include 3 sentences in each column, and make sure the information is relevant to an investigator's perspective."
        template = table_investigator
    elif modality == "financial analyst":
        user_prompt = f"Please generate a response about {prompt} from the perspective of a financial analyst. Start with this introduction sentence: '{intro_sentence_financial}' Then create a table with 3 columns: Assets & Liabilities, Cashflows & Liquidity, and Key Financial Ratios. Include 3 sentences or data points in each column, and ensure the information is relevant to a financial analyst's perspective."
        template = table_financial
    else:
        raise ValueError("Modality must be one of 'business analyst', 'investigator', or 'financial analyst'.")

    placeholders = extract_template_structure(template)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{user_prompt}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
        frequency_penalty=0,
        presence_penalty=0
    )

    formatted_response = response.choices[0].text.strip()

    # Replace the template placeholders with the generated content
    generated_content = formatted_response[len(intro_sentence):].strip()
    response_parts = generated_content.split("•")[1:]
    filled_template = template
    for i, part in enumerate(response_parts):
        filled_template = filled_template.replace(placeholders[i], f"• {part.strip()}")

    final_response = f"{intro_sentence}\n{filled_template}"

    return final_response

if __name__ == "__main__":
    prompt = "Enter company name here ..."
    
    print("Business Analyst:")
    gpt4_analytical = generate_gpt4_response(prompt, "business analyst", api_key)
    print(gpt4_analytical)

    print("\nInvestigator:")
    gpt4_investigative = generate_gpt4_response(prompt, "investigator", api_key)
    print(gpt4_investigative)

    print("\nFinancial Analyst:")
    gpt4_financial = generate_gpt4_response(prompt, "financial analyst", api_key)
    print(gpt4_financial)