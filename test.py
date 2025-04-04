import json
import random

try:
    with open("FlashCards.json", "r") as file:
        fc = json.load(file)
except FileNotFoundError:
    fc = []

class t:
    def __init__(self, x=[]):
        w = x[0]
        d = x[-1]      
        self.w = w
        self.d = d

    def display_info(self):
         return f"{self.w} {self.d}"

    def re(self):
        return {"Wrd": self.w, "Def": self.d}

fc = []

e = t([input("ee ").split(":")])
print(e.re())

e = t('tired','sleep')

print(e.re())