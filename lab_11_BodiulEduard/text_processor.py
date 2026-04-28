def count_vowels(text):
    vowels = "аеєиіїоуюя"
    count = 0
    for char in text:
        if char.lower() in vowels:
            count += 1
    return count
def reverse_words(text):
    words = text.split()
    words.reverse()
    return " ".join(words)
def to_pig_latin(text):
    def convert_word(word):
        if len(word) < 1:
            return word
        return word[1:] + word[0] + "ay"
    words = text.split()
    converted_words = [convert_word(word) for word in words]
    return " ".join(converted_words)