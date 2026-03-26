class Queue:

    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, item):

        # 🔴 Bug #1 trigger
        isEnqueueSuccessful = len(self.queue) < self.size
        hasEnqueueBeenCompletedSuccessfully = len(self.queue) != self.size

        if isEnqueueSuccessful and hasEnqueueBeenCompletedSuccessfully:
            self.queue.insert(0, item)

    def dequeue(self):

        # 🔴 Bug #2 trigger
        if self.queue != [] and not(len(self.queue) == 0):
            return self.queue.pop()

    def isEmpty(self):
        return self.queue == []
