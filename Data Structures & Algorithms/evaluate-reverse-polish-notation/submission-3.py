import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+','-','*','/']
        for i in tokens:
            if i in operators:
                a, b = stack.pop(), stack.pop()
                print(a,b, i)
                if i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(b-a)
                elif i == '*':
                    stack.append(b*a)
                else:
                    stack.append(int(float(b)/a))
            else:
                stack.append(int(i))
        return int(stack.pop())


        