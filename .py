import json
import random

try:
    with open("FlashCards.json", "r") as file:
        fc = json.load(file)
except:
    fc = []


m = "student"
s = 0
a = ""

if "teacher" in m:
    p = input("input ; to stop, use : to separate word and answer ")
    while p != ";":
        p = p.split(":")
        fc.append({"w":p[0],"d":p[1]})
        p = input("next ")

if "student" in m:
    aaaa = open("./FlashCard.json", encoding="utf8")
    fc = json.load(aaaa)
    while ";" in a == False:
        x = random.choice(fc)
        a = input(f"{x["w"]}(input ; to stop)")
        if a in x["d"]:
            print("Correct. ")
            s += 1
        else:
            s = 0
            print("Incorrect. ")
        if s%5 == 0:
            print(f"You have a streak of {s}")

with open("FlashCard.json", "w") as file:
     json.dump(fc, file, indent=2)