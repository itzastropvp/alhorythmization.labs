def text_statistics(text):
    words = 0
    chars = 0
    r = 0
    for word in text.split():
        words += 1
        for char in word:
            chars += 1
    for i in text:
        if i == "!" or i == "?" or i == "." or i == ",":
            r += 1
    print(f"Символів: {chars}, слів: {words}, речень: {r}")
text_statistics("Привіт! Як справи?")