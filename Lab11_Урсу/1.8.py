with open("multiplication_table.txt", "w", encoding="utf-8") as file:
    for i in range(1, 11):
        row = ""

        for j in range(1, 11):
            row += f"{i} × {j} = {i*j} "

        file.write(row + "\n")
