import random

from flask import Blueprint, render_template, request, jsonify
# dot (.) before completions, tells Python to import completions module from same directory as main.py
from .completions import text_davinci_reponse, generate_gpt4_response, get_api_key

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]
        api_key = get_api_key()
        text_davinci = text_davinci_reponse(prompt, api_key)
        gpt4 = generate_gpt4_response(prompt, api_key)
        return jsonify({"text_davinci": text_davinci, "gpt4": gpt4})
    return render_template("index.html")

@bp.route('/predefined')
def predefined():
    questions = [
        "Is Deutsche Bank solvent?",
        "Is Tesla sanctioned?",
        "Does Apple have large cash reserves?",
        "Is Amazon a technology company?",
        "What is a PE ratio?",
    ]
    question = random.choice(questions)
    return render_template('index.html', predefined_question=question)

