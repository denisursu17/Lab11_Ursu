from datetime import datetime

class Calculator:

    def __init__(self):
        self.history = []

    def save(self, expression):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"{time} | {expression}")

    def add(self, a, b):
        result = a + b
        self.save(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.save(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.save(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        result = a / b
        self.save(f"{a} / {b} = {result}")
        return result

    def save_to_file(self):
        with open("history.txt", "w") as file:
            for item in self.history:
                file.write(item + "\n")
