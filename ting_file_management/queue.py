class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return self.size()

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self._data.pop(0)

    def search(self, index):
        if index < 0:
            raise IndexError()
        try:
            return self._data[index]
        except IndexError:
            raise IndexError()

    def is_empty(self):
        return not self.size()

    def size(self):
        return len(self._data)
