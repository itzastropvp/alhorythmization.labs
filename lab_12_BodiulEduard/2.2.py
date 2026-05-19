class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0) if self.queue else None
    def is_empty(self):
        return len(self.queue) == 0

def queue_with_timeout(customers, service_time):
    customers.sort(key=lambda x: x[0])
    queue = Queue()
    time = 0
    i = 0
    served = 0
    lost = 0
    while i < len(customers) or not queue.is_empty():
        while i < len(customers) and customers[i][0] <= time:
            queue.enqueue(customers[i])
            i += 1
        if queue.is_empty():
            time = customers[i][0]
            continue
        arrival, max_wait = queue.dequeue()
        if time - arrival > max_wait:
            lost += 1
            continue
        served += 1
        time += service_time
    return (served, lost)
print(queue_with_timeout([(0, 5), (2, 3), (4, 2)], 2))