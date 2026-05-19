class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return len(self.stack) == 0
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

def sort_even_numbers(numbers):
    stack = Stack()
    for item in numbers:
        if item % 2 == 0:
            stack.push(item)
    return stack.stack
print(sort_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))