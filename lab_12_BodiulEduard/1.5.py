class PriorityQueue:
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

def simple_priority_queue(tasks):
    queue = PriorityQueue()
    result = []
    for task in tasks:
        queue.push(task)
    queue.stack.sort(key=lambda x: x[0])
    for task in queue.stack:
        result.append(task[1])
    return result
print(simple_priority_queue(tuple([(3, "taskC"), (1, "taskA"), (2, "taskB")])))