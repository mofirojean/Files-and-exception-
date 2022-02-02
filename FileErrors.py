"""handling file error"""


def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as file_object:
            file = file_object.read()
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    # counting the number of words
    else:
        words = file.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = ['alice.txt', 'little_women.txt', 'moby_dick.txt','siddhartha.txt']
for filename in filenames:
    count_words(filename)
