import random

from flask import Blueprint, render_template, request, jsonify
from .completions import generate_gpt4_response, get_api_key

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        modality = request.form.get("modality")
        api_key = get_api_key()

        # Generate response for the specific modality
        gpt4_response = generate_gpt4_response(prompt, modality, api_key)

        # jsonify() converts Python dictionary to JSON for the specific modality
        return jsonify({f"gpt4_{modality.lower()}": gpt4_response})

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

