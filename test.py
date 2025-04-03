import json
import random

try:
    with open("FlashCards.json", "r") as file:
        fc = json.load(file)
except FileNotFoundError:
    fc = []

class t:
    def __init__(s, w, d):
        s.w = w
        s.d = d
    def re(s):
        return f"{s.w}:{s.d}"


e = input("ee ")

e = t(e)

fc.append(e.re)

print(fc)