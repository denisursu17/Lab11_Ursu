with open("source.txt", "r", encoding="utf-8") as source:
    with open("filtered.txt", "w", encoding="utf-8") as target:

        for line in source:
            if len(line.strip()) > 20:
                target.write(line)
