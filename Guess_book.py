filename = 'text.txt'

"""The loop records info of those who visit the site"""
i = 1
while i <= 1:
    user_name = input("Enter your name: ")
    user_entry = f"{user_name} just entered your site."
    with open(filename, 'a') as file_object:
        file_object.write("\n")
        file_object.write(user_entry)

    print(f"{user_name} you are welcome to nicopad")
    i += 1
