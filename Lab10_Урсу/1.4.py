is_palindrome = lambda s: (
    (s.lower().replace(" ", "")) == (s.lower().replace(" ", "")[::-1])
)
print(is_palindrome("Python"))
