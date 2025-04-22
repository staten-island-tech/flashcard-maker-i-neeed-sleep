import json
import random

aaaa = open("./FlashCard.json", encoding="utf8")
fc = json.load(aaaa)
pfc = fc

try:
    with open("FlashCards.json", "r") as file:
        fc = json.load(file)
except:
    fc = []

m = input("teacher or student mode?")
s = 0
a = ""

if "teacher" in m:
    p = input("input ; to stop, use : to separate word and answer ")
    while p != ";":
        p = p.split(":")
        fc.append({"w":p[0],"d":p[1]})
        p = input("next ")
    fc += pfc
    with open("FlashCard.json", "w") as file:
        json.dump(fc, file, indent=2)

if "student" in m:
    while a != ";":
        x = random.choice(pfc)
        a = input(f"{x["w"]}(input ; to stop)")
        if a != ";":
            if a == x["d"]:
                print("Correct. ")
                s += 1
            else:
                s = 0
                print("Incorrect. ")
            if s%5 == 0:
                print(f"You have a streak of {s}")