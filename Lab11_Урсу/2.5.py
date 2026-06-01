try:
    numbers = []

    with open("file1.txt") as file1:
        for line in file1:
            numbers.append(int(line))

    with open("file2.txt") as file2:
        for line in file2:
            numbers.append(int(line))

    result = sorted(set(numbers))

    with open("merged.txt", "w") as file:
        for number in result:
            file.write(str(number) + "\n")

    print("Файл merged.txt створено")

except FileNotFoundError:
    print("Один із файлів не знайдено")

except ValueError:
    print("Некоректні дані у файлі")
