from translate import Translator

try:
    with open("text.txt", "r", encoding="UTF-8") as file:
        text = file.read()
    print(text)
except FileNotFoundError as err:
