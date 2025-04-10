import json
import random

try:
    with open("FlashCards.json", "r") as file:
        fc = json.load(file)
except:
    fc = []



    x = random.choice(fc.items())
    a = input(x["w"])
    for x in fc:
        if a in fc.values(x):
            print("EY")
            s += 1

