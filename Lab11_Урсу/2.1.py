import text_processor

text = input("Текст: ")

print("Голосних:", text_processor.count_vowels(text))
print("Зворотній порядок слів:",
      text_processor.reverse_words(text))
print("Піг-латин:",
      text_processor.to_pig_latin(text))
