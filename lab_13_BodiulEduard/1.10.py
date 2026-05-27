sentences = ["Python is great", "I love programming"]
result = max(len(word) for sentence in sentences for word in sentence.split())
print(result)