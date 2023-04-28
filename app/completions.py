import requests
import os
import openai
import re

def get_api_key():
    api_key = os.environ["OPENAI_API_KEY"]
    openai.api_key = api_key    # set api key for the openai library
    return api_key

api_key = get_api_key()

# Validate entered company name
def validate_company_name(company_name):
    if not re.match(r'^[a-zA-Z0-9\s.,\-]+$', company_name):
        raise ValueError("Invalid company name. The name should only contain letters, digits, spaces, and common punctuation marks like periods, commas, and hyphens.")
    return company_name

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
• Bullet point 10spec
"""

# Modality: Investigator
intro_sentence_investigator = "As an investigator, I have compiled the following data:"
table_investigator = """
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
• Bullet point 11
• Bullet point 12
"""

# Modality: Financial Analyst
intro_sentence_financial = "As a financial analyst, I have analyzed the financial aspects of the prompt:"
table_financial = """
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
• Bullet point 11
• Bullet point 12
"""

def extract_template_structure(template):
    placeholders = []
    for line in template.split('\n'):
        placeholders.extend(re.findall(r'(• Bullet point \d+|• Sentence \d+|• Ratio \d+)', line))
    return placeholders

def generate_gpt4_response(prompt, modality, api_key):
    # Validate the company name
    validate_company_name(prompt) 
    
    if modality == "business analyst":
        intro_sentence = f"This preliminary business analysis of {prompt} has identified the following key insights:"
        user_prompt = f"Please generate a response about {prompt} from the perspective of a business analyst. Start with this introduction sentence: '{intro_sentence}' Then list 10 key business analysis insights using bullet points. Do not number the bullet points. Format each bullet point as a new paragraph and ensure the content is relevant to the role of a business analyst."
        template = bullet_points
    elif modality == "investigator":
        intro_sentence = f"This preliminary investigation of {prompt} has examined general investigative, corporate, and compliance information, and compiled the following results:"
        user_prompt = f"Please generate a response about {prompt} from the perspective of an investigator. Start with this introduction sentence: '{intro_sentence}'.  Create a first subheading 'General Investigative Information'. List 3 key general investigative insights using bullet points for {prompt}. Create a second subheading 'Corporate Information'. List 3 insights regarding corporate information using bullet points for {prompt}. Create a third subheading 'Compliance Information'. List 3 insights regarding compliance information using bullet points for {prompt}. Do not number the bullet points. Format each bullet point as a new paragraph and ensure the content is relevant to the role of an investigator"
        template = table_investigator
    elif modality == "financial analyst":
        intro_sentence = f"This preliminary financial analysis of {prompt} reports upon its assets and liabilities, cashflows and liquidity, and provides 3 key ratios for the company:"
        user_prompt = f"Please generate a response about {prompt} from the perspective of an financial analyst. Start with this introduction sentence: '{intro_sentence}'.  Create a first subheading 'Assets & Liabilities'. List 3 key Assets and Liabilities insights using bullet points for {prompt}. Create a second subheading 'Cashflows & Liquidity'. List 3 insights regarding cashflows and liquidity information using bullet points for {prompt}. Create a third subheading 'Key Financial Ratios'. List 3 key financial ratios with the relevant values using bullet points for {prompt}. Do not number the bullet points. Format each bullet point as a new paragraph and ensure the content is relevant to the role of an financial analyst"
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
    for i, part in enumerate(response_parts[:min(len(placeholders), len(response_parts))]):
        filled_template = filled_template.replace(placeholders[i], f"• {part.strip()}")

    final_response = f"{intro_sentence}\n{filled_template}"

    return final_response