class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop() if self.stack else None
    def is_empty(self):
        return len(self.stack) == 0

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr

def merge_stacks(parts):
    stack = Stack()
    for part in parts:
        for x in part:
            stack.push(x)
    return insertion_sort(stack.stack)

def hybrid_sort(arr, threshold=10):
    stack = Stack()
    stack.push(arr)
    data = stack.pop()
    parts = []
    for i in range(0, len(data), threshold):
        part = data[i:i + threshold]
        if len(part) <= threshold:
            part = insertion_sort(part)
        else:
            part = selection_sort(part)
        parts.append(part)
    return merge_stacks(parts)
print(hybrid_sort([9, 7, 5, 11, 12, 2, 14, 3, 10, 6], 4))