# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

# Note that division between two integers should truncate toward zero.

# It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        op = set(['+', '-', '*', '/'])

        for t in tokens:
            if t not in op:
                stack.append(int(t))
            else:
                first = int(stack.pop())
                second = int(stack.pop())

                if t == '+':
                    stack.append(first + second)
                elif t == '-':
                    stack.append(second - first)
                elif t == '*':
                    stack.append(first * second)
                elif t == '/':
                    stack.append(second / first)

        return int(stack[-1])
