class heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, data):
        self.heap.append(data)
        size += 1
        self.arrange(self.size)

    def arrange(self, k):
        while k //2 > 0:
            if self.heap[k] < self.heap[2*k-1]:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k/= 2