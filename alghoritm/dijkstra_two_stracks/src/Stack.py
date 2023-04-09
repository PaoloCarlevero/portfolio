class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    @property
    def top(self):
        return self.stack[-1]

    @property
    def size(self):
        return len(self.stak)

    @property
    def is_empty(self):
        return len(self.stack) == 0

    @property
    def is_full(self):
        return len(self.stack) > 0