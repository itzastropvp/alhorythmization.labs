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

def stack_size(stack):
    temp_stack = Stack()
    count = 0
    while not stack.is_empty():
        item = stack.pop()
        temp_stack.push(item)
        count += 1
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    return count
s = Stack()
for i in [1, 2, 3, 4, 5]:
    s.push(i)
print(stack_size(s))