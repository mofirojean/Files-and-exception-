# reads two file cats and dogs
def read_txt(animals):
    try:
        with open(animals, encoding='utf-8') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        pass
# print(f"file {animals} not found")


animals = ['cts.txt', 'dogs.txt']
for animal in animals:
    read_txt(animal)
