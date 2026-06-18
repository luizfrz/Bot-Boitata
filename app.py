
from flask import Flask, render_template, request, jsonify 
from pathlib import Path
import json
import random

app = Flask(__name__)

BASE_DIR = Path(__file__).parent

with open(BASE_DIR / "intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

def inter_Int(msg):
    msg = msg.lower()

    for intent, dados in intents.items():
        for pattern in dados["patterns"]:
            if pattern.lower() in msg:
                return intent

    return None

def response(msg):
    intent = inter_Int(msg)

    if intent:
        return random.choice(intents[intent]["responses"])
    return "Desculpe, não entendi sua pergunta."

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
    app.run(debug=True)