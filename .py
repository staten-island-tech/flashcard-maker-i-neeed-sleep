import json
import random

try:
    with open("FlashCards.json", "r") as file:
        fc = json.load(file)
except FileNotFoundError:
    fc = []

class t:
    def __init__(s, w, d):
        s.wrd = w
        s.df = d
    def d(s):
        return{s.wrd:s.df}

m = input("teacher or student mode?").lower()

if "teacher" in m:
    p = input("input ; to stop, use : to separate word and answer ").split(":")
    while p != ";":
        fc.append(p)
        p = input("next ")

print(fc)

