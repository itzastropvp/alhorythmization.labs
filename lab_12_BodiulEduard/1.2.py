class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return len(self.stack) == 0
    def push(self, text):
        self.stack.append(text)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

stack = Stack()
def reversed_text(text):
    text = text.lower()
    text = text.replace(" ", "")
    for char in text:
        stack.push(char)
    result = ""
    while not stack.is_empty():
        result += stack.pop()
    return result == text
print(reversed_text("hello"))