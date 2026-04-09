def calculate_discount(price, discount_percent, is_member):
    if is_member:
        discount_percent += 5
    total = price * (1 - discount_percent / 100)
    print(total)
calculate_discount(750, 15, False)