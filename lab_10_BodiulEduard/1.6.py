words = ["cat", "elephant", "dog", "house", "algorithm"]
words4 = filter(lambda x: len(x) > 4, words)
print(list(words4))