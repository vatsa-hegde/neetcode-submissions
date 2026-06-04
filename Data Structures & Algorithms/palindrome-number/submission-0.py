class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = []
        while x > 0:
            temp.append(x % 10)
            x = x//10
        print(temp)
        l = 0
        r = len(temp)-1
        while r < len(temp) and l <= r:
            if temp[l] == temp[r]:
                l+=1
                r-=1
            else:
                return False
        return True
        