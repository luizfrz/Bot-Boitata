from flask import Flask, render_template, request, jsonify 
from pathlib import Path
from rapidfuzz import fuzz
import json
import random
import os

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR  / "json" / "intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

def inter_Int(msg):
    better_Intent = None
    more_Score = 0

    for intent, dados in intents.items():
        for pattern in dados["patterns"]:
            score = fuzz.ratio(msg.lower(), pattern.lower())

            if score > more_Score:
                more_Score = score
                better_Intent = intent
            
            if more_Score >= 70:
                return better_Intent

    return None
    

def response(msg):
    intent = inter_Int(msg)

    if intent:
        return random.choice(intents[intent]["responses"])
    return "ainda nao existe uma resposta definida para isso..."

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"]) 
def chat():
    msgr = request.json["message"]
    return jsonify(
        {
            "response":response(msgr)
        }
    )
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)