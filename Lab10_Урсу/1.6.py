words = ["cat", "elephant", "dog", "house", "algorithm"]
result = list(filter(lambda w: len(w) > 4, words))
print(result)