"""this program storee users imformation as they input it"""
import json
"""refactoring"""


def get_stored_user():
    """get stored username is available"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_user_name():
    """Prompts user for their name"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """greet the user by name"""
    username = get_stored_user()
    question = input("Are you the correct user? ")
    if question.lower() == 'yes':
        if username:
            print(f"Welcome back, {username}!")
        else:
            username = get_user_name()
            print(f"We'll remember you when you come back, {username}!")
    elif question.lower() == "no":
        get_user_name()


greet_user()
