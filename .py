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
        return{s.w:s.d}

m = input("teacher or student mode?").lower()

if "teacher" in m:
    p = t(input("input ; to stop, use : to separate word and answer ").split(":"))
    while p != ";":
        fc.append(p.re())
        p = input("next ")

print(fc)