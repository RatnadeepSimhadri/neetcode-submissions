from abc import ABC, abstractmethod

class Solution:
    class Operation(ABC):
        @abstractmethod
        def execute(self,stack: List[int]):
            pass
    
    class Additive(Operation):
        def execute(self,stack: List[int]):
            stack.append(stack[-1] + stack[-2])
    
    class Double(Operation):
        def execute(self, stack: List[int]):
            stack.append(2 * stack[-1])

    class Clear(Operation):
        def execute(self, stack: List[int]):
            stack.pop()


    def calPoints(self, operations: List[str]) -> int:
        stack = []
        op_map = {
            "+": Solution.Additive(),
            "D": Solution.Double(),
            "C": Solution.Clear()
        }
        for op in operations:
            if op in op_map:
                op_map[op].execute(stack)
            else:
                stack.append(int(op))

        return sum(stack)

    
    
