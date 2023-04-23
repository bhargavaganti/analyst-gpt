import random

from flask import Blueprint, render_template, request, jsonify
# dot (.) before completions, tells Python to import completions module from same directory as main.py
from .completions import generate_gpt4_response, get_api_key

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        api_key = get_api_key()

        # 3 separate modalities
        gpt4_analytical = generate_gpt4_response(prompt, "business analyst", api_key)
        gpt4_investigative = generate_gpt4_response(prompt, "investigator", api_key)
        gpt4_financial = generate_gpt4_response(prompt, "financial analyst", api_key)
        
        # jsonify() converts Python dictionary to JSON for 3 separate modalities
        return jsonify({
            "gpt4_analytical": gpt4_analytical,
            "gpt4_investigative": gpt4_investigative,
            "gpt4_financial": gpt4_financial
        })
    
    return render_template("index.html")


@bp.route('/predefined')
def predefined():
    questions = [
        "Is Tesla sanctioned",
        "Does Apple have large cash reserves",
        "Does Alibaba have Cayman Island registered subsidiaries",
        "Is Amazon a technology company or a retail company",
    ]
    question = random.choice(questions)
    return render_template('index.html', predefined_question=question)



