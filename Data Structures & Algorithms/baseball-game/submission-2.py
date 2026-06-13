class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                top = stack[-1]
                previous = stack[-2]
                stack.append(previous+top)
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)