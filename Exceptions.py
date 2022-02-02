"""ZeroDivisionError handling"""
# try:
#     print(3 / 0)
# except ZeroDivisionError:
#     print("you can't divide by zero!")

"""using exceptions to prevent crash (division calculator)"""
print("Give me two numbers and i will divide them")
print("Enter 'q' to quit")

while True:
    first_number = input("\nEnter first number: ")
    if first_number == 'q':
        break
    second_number = input("Enter second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Invalid input! can't divide a number by Zero!!! ")
    else:
        print(answer)
