from datetime import datetime

note = input("Введіть запис: ")

now = datetime.now()

with open("diary.txt", "a", encoding="utf-8") as file:
    file.write(f"{now:%Y-%m-%d %H:%M:%S} - {note}\n")
