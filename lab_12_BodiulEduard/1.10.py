class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop() if self.stack else None
    def is_empty(self):
        return len(self.stack) == 0

def find_min_max(arr):
    stack = Stack()
    for x in arr:
        stack.push(x)
    if stack.is_empty():
        return None
    first = stack.pop()
    min_val = first
    max_val = first
    while not stack.is_empty():
        value = stack.pop()
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value
    return (min_val, max_val)
print(find_min_max([7, 2, 9, 1, 5]))