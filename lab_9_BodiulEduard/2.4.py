def calculate_weight_cost(weight):
    cost = 0
    if weight <= 5:
        cost = 50
    elif weight <= 10:
        cost = 80
    elif weight > 10:
        cost = 80 + ((weight - 10)*10)
    return cost
def calculate_delivery(distance, weight, is_express=False):
    weight_cost = calculate_weight_cost(weight)
    if is_express:
        total = (distance*2)
    else:
        total = distance + weight_cost
    print(total)
    return total
calculate_delivery(50, 4)