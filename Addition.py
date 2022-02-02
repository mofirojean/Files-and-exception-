# add two numbers and returns an error for wrong input
print("Addition calculator")
while True:
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
    except ValueError:
        print("Invalid input you must enter an  Integer")
    else:
        addition = first_number + second_number
        print(addition)