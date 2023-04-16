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

if __name__ == "__main__":
    app.run(debug=True)
