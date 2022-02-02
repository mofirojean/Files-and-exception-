"""reading an entire file in python"""
print("Reading an entire file")
with open('text_files/py_digits.txt') as file_object:
	content = file_object.read()
print(content.strip())

"""Reading a file line by line"""
print("Readingthe file line by line ")
file_name = "text_files/py_digits.txt"
with open(file_name) as file_object:
	for line in file_object:
		print(line.rstrip())

"""making a list of lines from a file"""
print("making a list of lines from a file")
with open(file_name) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

"""working with a file's content"""
print("Producing a single dtring with our values from the text file")
pi_value = ''
for line in lines:
	pi_value += line.rstrip()

print(pi_value)
print(float(pi_value))

"""is your birthday contain in pi"""
print("Is your birthday contained in pi")
filename = 'text_files/pi_million_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line

birthday = input("Enter your birthdayin the form mmddyy: ")

if birthday in pi_string:
	print("Your birthday appears in the first million digitd of pi!")
else:
	print("Your birthdaydoes not appear in the first million digits of pi!")
