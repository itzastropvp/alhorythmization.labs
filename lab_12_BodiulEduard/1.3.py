class SimpleQueue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item) # Додаємо в кінець
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.pop(0)

def process_requests(requests):
    queue = SimpleQueue()
    result = []
    for req in requests:
        queue.enqueue(req)
    while not queue.is_empty():
        result.append(queue.dequeue())
    return result
print(process_requests(["заявка1", "заявка2", "заявка3"]))