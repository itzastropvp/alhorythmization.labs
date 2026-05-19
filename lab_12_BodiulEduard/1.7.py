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

def linear_search_count(arr, target):
    stack = Stack()
    for item in reversed(arr):
        stack.push(item)
    index = 0
    comparisons = 0
    while not stack.is_empty():
        comparisons += 1
        value = stack.pop()
        if value == target:
            return (index, comparisons)
        index += 1
    return (-1, comparisons)
print(linear_search_count([10, 20, 30, 40, 50], 30))