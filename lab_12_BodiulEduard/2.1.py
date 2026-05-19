class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop() if self.stack else None
    def is_empty(self):
        return len(self.stack) == 0

def rpn_calculator(expression):
    stack = Stack()
    tokens = expression.split()
    for token in tokens:
        if token not in "+-*/":
            stack.push(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.push(a + b)
            elif token == "-":
                stack.push(a - b)
            elif token == "*":
                stack.push(a * b)
            elif token == "/":
                stack.push(a / b)
    result = stack.pop()
    if result.is_integer():
        return int(result)
    return result
print(rpn_calculator("3 4 +"))