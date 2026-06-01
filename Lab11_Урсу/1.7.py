total = 0

with open("numbers.txt", "r") as file:
    while True:
        line = file.readline()

        if not line:
            break

        total += float(line)

print("Сума чисел:", total)
