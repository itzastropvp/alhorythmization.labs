class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop() if self.stack else None
    def is_empty(self):
        return len(self.stack) == 0

def bubble_sort_optimized_stack(arr):
    stack = Stack()
    for x in arr:
        stack.push(x)
    n = len(arr)
    iterations = 0
    for i in range(n):
        swapped = False
        iterations += 1
        for j in range(0, n - i - 1):
            if stack.stack[j] > stack.stack[j + 1]:
                stack.stack[j], stack.stack[j + 1] = stack.stack[j + 1], stack.stack[j]
                swapped = True
        if not swapped:
            break
    return (stack.stack, iterations)
print(bubble_sort_optimized_stack([5, 3, 8, 1, 2]))