with open("source.txt", "r", encoding='utf-8') as f:
    source = f.readlines()
    for line in source:
        line1 = line.replace("\n", "")
        line1 = line1.replace(".", "")
        if len(line1) > 20:
            with open("filtered.txt", "a", encoding='utf-8') as f:
                f.write(line)