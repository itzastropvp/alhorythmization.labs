class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None
    def is_empty(self):
        return len(self.stack) == 0

def binary_search_steps(arr, target):
    stack = Stack()
    steps = []
    stack.push((0, len(arr) - 1))
    result = -1
    while not stack.is_empty():
        left, right = stack.pop()
        if left > right:
            continue
        mid = (left + right) // 2
        steps.append(mid)
        if arr[mid] == target:
            result = mid
            break
        elif arr[mid] < target:
            stack.push((mid + 1, right))
        else:
            stack.push((left, mid - 1))
    return (steps, result)
print(binary_search_steps([1, 3, 5, 7, 9, 11], 7))
