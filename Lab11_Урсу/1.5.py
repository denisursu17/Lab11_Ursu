with open("poem.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

line_count = len(lines)

word_count = 0
for line in lines:
    word_count += len(line.split())

print("Рядків:", line_count)
print("Слів:", word_count)
