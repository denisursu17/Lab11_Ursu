students = []
subject_sums = [0] * 5

with open("grades.csv", "r", encoding="utf-8") as file:
    for line in file:
        data = line.strip().split(",")

        name = data[0]
        surname = data[1]

        grades = list(map(int, data[2:]))

        average = sum(grades) / len(grades)

        students.append((name, surname, average))

        for i in range(5):
            subject_sums[i] += grades[i]

best = max(students, key=lambda x: x[2])

with open("report.txt", "w", encoding="utf-8") as file:

    file.write("СЕРЕДНІ БАЛИ СТУДЕНТІВ:\n")

    for student in students:
        file.write(
            f"{student[0]} {student[1]}: {student[2]:.1f}\n"
        )

    file.write(
        f"\nКРАЩИЙ СТУДЕНТ: {best[0]} {best[1]} ({best[2]:.1f})\n"
    )

    file.write("\nСЕРЕДНІ БАЛИ З ПРЕДМЕТІВ:\n")

    count = len(students)

    for i in range(5):
        file.write(
            f"Предмет {i+1}: {subject_sums[i]/count:.1f}\n"
        )
