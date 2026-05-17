class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            print(stack)
            if self.is_number(op):
                stack.append(int(op))
            elif op == "+":
                ans = stack[-1] + stack[-2]
                stack.append(ans)
            elif op == "C":
                stack.pop()
            elif op == "D":
                 stack.append(2 * stack[-1])

        return sum(stack)

    def is_number(self,num):
        try:
            int(num)
            return True
        except ValueError:
            return False
