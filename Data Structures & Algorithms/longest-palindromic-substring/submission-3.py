class Solution:
    """
    a b a b d

    a a a b a a

    """
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        lengthOfLongest = 1
        longest = s[0]

        def recursion(i,j):
            nonlocal lengthOfLongest, longest, s
            if i >= len(s) or j >= len(s) or i < 0 or j < 0:
                return
            
            if s[i] == s[j]:
                if j-i+1 > lengthOfLongest:
                    lengthOfLongest = j-i+1
                    longest = s[i:j+1]
                recursion(i-1, j+1)
        for i in range(len(s)):
            recursion(i-1,i+1)
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                if lengthOfLongest < 2:
                    lengthOfLongest = 2
                    longest = s[i:i+2]
                recursion(i-1, i+2)
        return longest
            
        