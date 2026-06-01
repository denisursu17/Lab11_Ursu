import string

with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

for symbol in string.punctuation + "—«»":
    text = text.replace(symbol, " ")

words = text.split()

longest = max(words, key=len)

print(f'Найдовше слово: "{longest}" ({len(longest)} символів)')
