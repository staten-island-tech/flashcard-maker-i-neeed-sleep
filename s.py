import json
import random

try:
    with open("FlashCards.json", "r") as file:
        fc = json.load(file)
except:
    fc = []

s = 0

m = input("teacher or student mode?").lower()

