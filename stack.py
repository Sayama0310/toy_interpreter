class Stack:
    """
    スタッククラス
    """

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)
