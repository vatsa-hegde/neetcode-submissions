class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        mint = float('-inf')
        arr = sorted(list(zip(position, speed)),key=lambda x: x[0],reverse=True)
        print(arr)
        for pos, s in arr:
            distance = target - pos
            t = distance/s
            print(t,mint, res)
            if t > mint:
                res+=1
                mint = t
            
        return res


