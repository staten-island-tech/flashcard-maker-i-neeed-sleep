import json
import random

try:
    with open("FlashCards.json", "r") as file:
        fc = json.load(file)
except:
    fc = []


m = input("teacher or student mode?").lower()
s = 0

if "teacher" in m:
    p = input("input ; to stop, use : to separate word and answer ")
    while p != ";":
        p = p.split(":")
        fc.append({"w":p[0],"d":p[1]})
        p = input("next ")

if "student" in m:
    x = random.choice(fc)
    a = input()

with open("FlashCard.json", "w") as file:
     json.dump(fc, file, indent=2)