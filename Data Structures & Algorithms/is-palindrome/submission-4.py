class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        s = s.replace(" ","").lower()
        j = len(s)-1
        nums = [str(i) for i in range(10)]

        while i <= j:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
             
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                print(s[i],s[j])
                return False
        return True
        