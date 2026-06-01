import random
import string

for i in range(5):
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits)
    ]

    all_chars = string.ascii_letters + string.digits

    while len(password) < 8:
        password.append(random.choice(all_chars))

    random.shuffle(password)

    print(f"{i+1}. {''.join(password)}")
