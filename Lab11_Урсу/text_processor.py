def count_vowels(text):
    vowels = "аеєиіїоуюяAEIOUYaeiouy"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


def reverse_words(text):
    return " ".join(text.split()[::-1])


def to_pig_latin(text):
    result = []

    for word in text.split():
        result.append(word[1:] + word[0] + "ay")

    return " ".join(result)
