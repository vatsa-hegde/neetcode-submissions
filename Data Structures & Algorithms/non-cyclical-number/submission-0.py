"""

"""
class Solution:
    def isHappy(self, n: int) -> bool:
        viewed = set()

        while n != 1:
            temp = str(n)
            n = 0
            for l in temp:
                n += int(l) * int(l)
            if n in viewed:
                break
            viewed.add(n)
        
        if n == 1:
            return True
        return False
            


        