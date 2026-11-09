class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        result = [0]*len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                old_idx, old_temp = stack.pop()
                result[old_idx] = idx - old_idx
            stack.append((idx,temp))
        return result

                
