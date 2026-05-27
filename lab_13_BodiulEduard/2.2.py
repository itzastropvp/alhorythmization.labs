from collections import defaultdict

def group_products(products):
    grouped = defaultdict(list)

    for product in products:
        grouped[product["category"]].append(product["name"])

    return grouped
products = [
    {"name": "iPhone", "category": "Електроніка"},
    {"name": "Банан", "category": "Продукти"},
    {"name": "Ноутбук", "category": "Електроніка"},
    {"name": "Хліб", "category": "Продукти"}
]
print(group_products(products))