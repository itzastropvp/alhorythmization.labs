with open("multiplication_table.txt", 'w') as f:
    for i in range(1, 11):
        for j in range(1, 11):
            table = f"{i} x {j} = {i*j}   "
            f.write(table)
        f.write("\n")