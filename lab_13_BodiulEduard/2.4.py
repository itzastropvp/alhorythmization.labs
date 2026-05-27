def factorial_gen(max_n):
    result = 1
    yield 1 
    for i in range(1, max_n + 1):
        result *= i
        yield result
print(list(factorial_gen(5)))