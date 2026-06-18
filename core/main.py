import json
import time 
from pathlib import Path
import random

# Terminal

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "json" / "intents.json", "r", encoding="utf-8") as file:
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

while True:
    msg = input("Voce: ")
    print("gerando respostas...")
    time.sleep(0.8)
    resposta = response(msg)

    print(f"Boitata {resposta}")

    if msg.lower() in ["sair", "tchau"]:
        break
    
