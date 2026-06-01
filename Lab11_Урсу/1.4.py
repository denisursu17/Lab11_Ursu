import random

counts = [0] * 6

for _ in range(1000):
    roll = random.randint(1, 6)
    counts[roll - 1] += 1

for i in range(6):
    percent = counts[i] / 1000 * 100
    print(f"Грань {i+1}: {percent:.1f}%")
