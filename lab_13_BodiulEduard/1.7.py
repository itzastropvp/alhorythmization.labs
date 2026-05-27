word_list = ["Apple", "banana", "Apricot", "blueberry", "avocado"]
letter = 'a'
result = {
    word for word in word_list
    if word.lower().startswith(letter.lower())
}
print(result)