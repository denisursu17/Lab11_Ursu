from datetime import date

year = int(input("Рік: "))
month = int(input("Місяць: "))
day = int(input("День: "))

birth = date(year, month, day)
today = date.today()

age = today.year - birth.year
if (today.month, today.day) < (birth.month, birth.day):
    age -= 1

days = [
    "понеділок",
    "вівторок",
    "середа",
    "четвер",
    "п'ятниця",
    "субота",
    "неділя"
]

print("Вік:", age, "років")
print("День народження:", days[birth.weekday()])

next_birthday = date(today.year, month, day)

if next_birthday < today:
    next_birthday = date(today.year + 1, month, day)

delta = (next_birthday - today).days

print("Днів до наступного дня народження:", delta)
