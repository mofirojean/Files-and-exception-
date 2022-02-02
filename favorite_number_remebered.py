"""combine taking and also reading the fav number"""
import json

filename = 'fav_number.json'
try:
    with open(filename) as f:
        fav = json.load(f)
except FileNotFoundError:
    favorite_num = input("Whats your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(favorite_num, f)
        print("I just stored your fav number")
else:
    print(f"I know your favorite number, It's {fav}")