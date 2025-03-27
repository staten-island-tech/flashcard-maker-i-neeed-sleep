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

if m == "teacher mode":
    p = input("input ; to stop, use : to separate word and answer ").split(":")
    while ";" in p == False:
        fc.append(p)
        p = input("next ")




with open("FlashCards.json", 'w') as file:
    json.dump(fc, file, indent = 2)