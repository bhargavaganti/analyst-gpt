import random

from flask import Blueprint, render_template, request, jsonify
from .completions import generate_gpt4_response, get_api_key

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@bp.route('/get_completion', methods=["POST"])
def get_completion():
    try:
        prompt = request.form['prompt']
        modality = request.form['modality']
        api_key = get_api_key()

        # Generate response for the specific modality
        gpt4_response = generate_gpt4_response(prompt, modality, api_key)
        
        return jsonify({"success": True, "response": gpt4_response})
    
    except ValueError as e:
        # jsonify() converts Python dictionary to JSON for the specific modality
        return jsonify({"success": False, "error": str(e)})

@bp.route('/predefined')
def predefined():
    questions = [
        "NVIDIA",
        "AMD",
        "Tesla",
        "BMW",
    ]
    question = random.choice(questions)
    return render_template('index.html', predefined_question=question)
