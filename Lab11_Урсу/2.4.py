FILENAME = "passwords.txt"

def encrypt(text):
    result = ""

    for char in text:
        result += chr(ord(char) + 1)

    return result


def decrypt(text):
    result = ""

    for char in text:
        result += chr(ord(char) - 1)

    return result


def add(site, password):
    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(f"{site}:{encrypt(password)}\n")

    print("Додано запис для", site)


def find(site):
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:

            for line in file:
                s, p = line.strip().split(":")

                if s == site:
                    print("Пароль для", site + ":", decrypt(p))
                    return

            print("Запис не знайдено")

    except FileNotFoundError:
        print("Файл не знайдено")


add("google.com", "myPass123")
add("github.com", "dev2024")

find("google.com")
