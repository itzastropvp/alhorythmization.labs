raw_numbers = ["0501234567", "+380501234567", "(050)123-45-67"]
cleaned = [
    "+380" + x[-9:] if x.startswith("380") or x.startswith("0")
    else "+380" + x
    for x in ["".join(c for c in num if c.isdigit()) for num in raw_numbers]
]
print(cleaned)