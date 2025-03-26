import json
import random

try:
    with open("FlashCards.json", "r") as file:
        cd = json.load(file)
except FileNotFoundError:
    cd = []

m = input("teacher or student mode?").lower()

class t:
    def __innit__(w, d):
        word = w
        definition = d


with open("FlashCards.json", 'w') as file:
    json.dump(cd, file, indent = 4)