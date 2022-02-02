filename = 'text.txt'

"""The loop responds info of those who answer the question"""
i = 1
while i <= 3:
    user_name = input("Enter your name: ")
    responds = input("Why do you like programming: ")
    with open(filename, 'a') as file_object:
        file_object.write("\n")
        file_object.write(f"{user_name} : {responds}")

    print(f"{user_name} : {responds}")
    i += 1
