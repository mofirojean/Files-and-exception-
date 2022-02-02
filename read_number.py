"""this file reads back the fav number for the user"""
import json

filename = 'fav_number.json'
with open(filename) as f:
    fav = json.load(f)
    print(f"I know your favorite number, it's {fav}")
