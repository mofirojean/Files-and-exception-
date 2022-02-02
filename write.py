filename = 'text.txt'

with open(filename, 'w') as file_object:
    file_object.write(input("Enter a name: "))
