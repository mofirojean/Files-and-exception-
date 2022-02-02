"""using the json module to store data"""
import json

number = [1, 2, 3, 4, 5, 6]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(number, f)
    