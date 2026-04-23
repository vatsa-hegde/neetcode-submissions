class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            if stack:
                val,pos = stack[-1]
            else:
                stack.append((temperatures[i], i))
                continue
            if val > temperatures[i]:
                res[i] = pos - i
            else:
                while stack:
                    v , p = stack.pop()
                    if v > temperatures[i]:
                        res[i] = p - i
                        stack.append((v,p))
                        break
            stack.append((temperatures[i], i))
            
        return res

