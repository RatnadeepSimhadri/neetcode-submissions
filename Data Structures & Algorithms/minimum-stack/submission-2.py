class MinStack:

    def __init__(self):
        self.min_tracker = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_tracker:
            self.min_tracker.append(val)
        elif val <= self.min_tracker[-1]:
            self.min_tracker.append(val)

    def pop(self) -> None:
        elem = self.stack.pop()
        if elem == self.min_tracker[-1]:
            self.min_tracker.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_tracker[-1]
        
