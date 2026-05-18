def reverse_number(n):
    if n < 10:
        return n
    return int(str(n % 10) + str(reverse_number(n // 10)))
print(reverse_number(1234))