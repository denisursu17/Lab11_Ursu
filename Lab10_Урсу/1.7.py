grades = [45, 85, 90, 67, 33, 78, 92, 100, 55]
passed = filter(lambda x: x >= 60, grades)
converted = map(lambda x: round((x / 100) * 12), passed)
print(list(converted))