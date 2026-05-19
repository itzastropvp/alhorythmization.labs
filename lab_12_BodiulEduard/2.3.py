class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop() if self.stack else None
    def is_empty(self):
        return len(self.stack) == 0

def better(a, b):
    if a["grade"] != b["grade"]:
        return a["grade"] > b["grade"]
    if a["attendance"] != b["attendance"]:
        return a["attendance"] > b["attendance"]
    return a["name"] < b["name"]

def multi_criteria_sort(students):
    stack = Stack()
    for s in students:
        stack.push(s)
    arr = stack.stack
    n = len(arr)
    for i in range(n):
        best = i
        for j in range(i + 1, n):
            if not better(arr[best], arr[j]):
                best = j
        arr[i], arr[best] = arr[best], arr[i]
    return arr
print(multi_criteria_sort([
    {"name": "Alice", "grade": 85, "attendance": 90},
    {"name": "Bob", "grade": 85, "attendance": 95},
    {"name": "Charlie", "grade": 90, "attendance": 80}
]))