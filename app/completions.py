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
        intro_sentence = "As a business analyst, I have identified the following key insights:"
        user_prompt = f"Please generate a response about {prompt} from the perspective of a business analyst. Start with this introduction sentence: '{intro_sentence}' Then list 10 key business analysis insights using bullet points. Format each bullet point as a new paragraph and ensure the content is relevant to the role of a business analyst."
        template = bullet_points
    elif modality == "investigator":
        intro_sentence = "As an investigator, I have compiled the following data:"
        user_prompt = f"Please generate a response about {prompt} from the perspective of an investigator. Start with this introduction sentence: '{intro_sentence}' Then create a table with 3 columns: General Investigative Information, Corporate Information, and Compliance Information. Include 3 sentences in each column, and make sure the information is relevant to an investigator's perspective."
        template = table_investigator
    elif modality == "financial analyst":
        intro_sentence = "As a financial analyst, I have analyzed the financial aspects of the prompt:"
        user_prompt = f"Please generate a response about {prompt} from the perspective of a financial analyst. Start with this introduction sentence: '{intro_sentence}' Then create a table with 3 columns: Assets & Liabilities, Cashflows & Liquidity, and Key Financial Ratios. Include 3 sentences or data points in each column, and ensure the information is relevant to a financial analyst's perspective."
        template = table_financial
    else:
        raise ValueError("Modality must be one of 'business analyst', 'investigator', or 'financial analyst'.")

    placeholders = extract_template_structure(template)

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

    formatted_response = response.choices[0]["message"]["content"]  # works for v0.2.11

    # Replace the template placeholders with the generated content
    generated_content = formatted_response[len(intro_sentence):].strip()
    
    # Split the generated content based on the line breaks
    response_parts = generated_content.split("\n")
    
    # Remove any empty lines
    response_parts = [part.strip() for part in response_parts if part.strip()]
    
    filled_template = template
    for i, part in enumerate(response_parts):
        filled_template = filled_template.replace(placeholders[i], f"• {part.strip()}")

    final_response = f"{intro_sentence}\n{filled_template}"

    return final_response