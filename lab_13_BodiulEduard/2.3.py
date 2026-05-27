from collections import Counter
def analyze_text(text, n):
    words = text.lower().split()
    cleaned_words = [
        word.strip(".,!?;:")
        for word in words
    ]
    counter = Counter(cleaned_words)
    return counter.most_common(n)
print(analyze_text("Привіт, світ! Світ прекрасний. Привіт усім!", 2))