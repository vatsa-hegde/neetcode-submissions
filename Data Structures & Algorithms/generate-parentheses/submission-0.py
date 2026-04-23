class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def generate(openc, closec):
            if openc == closec == n:
                res.append(''.join(stack))
            
            if openc < n:
                stack.append('(')
                openc += 1
                generate(openc,closec)
                openc -= 1
                stack.pop()
            
            if closec < openc:
                stack.append(')')
                closec += 1
                generate(openc,closec)
                closec -= 1
                stack.pop()
        
        generate(0,0)
        return res