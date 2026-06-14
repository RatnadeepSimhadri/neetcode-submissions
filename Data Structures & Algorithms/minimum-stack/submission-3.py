class MinStack:

    def __init__(self):
       self.og_stack = []
       self.min_stack = [] 

    def push(self, val: int) -> None:
        self.og_stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
            return
            
        if val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        popped = self.og_stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.og_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
