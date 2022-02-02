"""this program greets user when he returns"""
import json

filename = 'username.json'
with open(filename) as f:
    greet_user = json.load(f)
    print(f"Welcome back, {greet_user}!")
