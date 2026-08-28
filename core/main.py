import json
import time 
from pathlib import Path
import random

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "json" / "intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)
    
def inter_Int(msg):
    msg = msg.lower()

    for intent, data in intents.items():
        for pattern in data["patterns"]:
            if pattern.lower() in msg:
                return intent

    return None

def response(msg):
    intent = inter_Int(msg)

    if intent:
        return random.choice(intents[intent]["responses"])

    return "não existe essa resposta..."

while True:
    msg = input("Voce: ")
    generate = [ 
        "Gerando uma resposta...",
        "Estou gerando uma resposta...",
        "Buscando  uma resposta",
        "Espere um momento... estou gerando",
        "Ok, aqui esta sua resposta..."
    ]

    print(random.choice(generate))
    time.sleep(0.3)
    resposta = response(msg)

    print(f"Boitata: {resposta}")

    if msg.lower() in ["sair", "tchau"]:
        exit
    
