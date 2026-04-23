class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recurse(sub,openB, closeB):
            if openB == closeB == n:
                res.append(''.join(sub))
                return
            if openB < n:
                openB +=1
                sub.append('(')
                recurse(sub,openB,closeB)
                sub.pop()
                openB -= 1
            if closeB < openB:
                closeB += 1
                sub.append(')')
                recurse(sub,openB,closeB)
                sub.pop()
                closeB-=1
        
        recurse([],0,0)
        return res