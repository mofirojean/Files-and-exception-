"""prompts user for a favorite number and the displace a statement"""
import json
"""prompt user"""
fav_number = input("Whats your favorite number? ")

"""storing the number"""
filename = "fav_number.json"
with open(filename, 'w') as f:
    json.dump(fav_number, f)
    print("We just stored your favorite number")

