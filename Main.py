class MyCircularQueue:
    def __init__(self, size: int):
        # Write code here
        self.queue = [0] * size
        self.size = size
        self.front, self.rear = -1, -1

    def enqueue(self, value: int) -> bool:
        # Write code here
        if not self.is_full():
            self.rear = (self.rear - 1) % self.size
            self.queue[self.rear] = value


    def dequeue(self) -> bool:
        # Write code here
        if not self.is_empty():
            value = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return value

    def get_front(self) -> int:
        # Write code here
        return self.front

    def get_rear(self):
        # Write code here
        return self.rear
    
    def is_empty(self):
        # Write code here
        return self.front == -1

    def is_full(self):
        # Write code here
        return (self.front == 0 and self.rear == (self.size - 1)) or (self.front == self.rear + 1)


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
data = []
for item in input().split(','):
    item = item.strip()
    if item == '-':
        data.append([])
    else:
        data.append([int(item)])
obj = MyCircularQueue(data[0][0])
result = []
for i in range(len(operations)):
    if i == 0:
        result.append(None)
    elif operations[i] == "enqueue":
        result.append(obj.enqueue(data[i][0]))
    elif operations[i] == "get_rear":
        result.append(obj.get_rear())
    elif operations[i] == "get_front":
        result.append(obj.get_front())
    elif operations[i] == "dequeue":
        result.append(obj.dequeue())
    elif operations[i] == "is_full":
        result.append(obj.is_full())
    elif operations[i] == "is_empty":
        result.append(obj.is_empty())

print(result)
