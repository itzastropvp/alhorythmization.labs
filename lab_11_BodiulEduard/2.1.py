import text_processor
text = "Python це цікаво"
vowels = text_processor.count_vowels(text)
reverse = text_processor.reverse_words(text)
pig_latin = text_processor.to_pig_latin(text)
print(f"Голосних: {vowels}")
print(f"Зворотній порядок: {reverse}")
print(f"Піг-латин: {pig_latin}")