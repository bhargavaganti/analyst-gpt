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
        gpt4 = generate_gpt4_response(prompt, api_key)
        return jsonify({"gpt4": gpt4})
    return render_template("index.html")

@bp.route('/predefined')
def predefined():
    questions = [
        "Example question: Is Deutsche Bank solvent?",
        "Example question: Is Tesla sanctioned?",
        "Example question: Does Apple have large cash reserves?",
        "Example question: Does Alibaba have Cayman Island registered subsidiaries?",
        "Example question: How strong is Microsoft balance sheet?",
    ]
    question = random.choice(questions)
    return render_template('index.html', predefined_question=question)



