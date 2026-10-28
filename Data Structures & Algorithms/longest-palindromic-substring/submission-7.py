class Solution:
    """
    a b a b d

    a a a b a a

    """
    # Recursion solution
    # def longestPalindrome(self, s: str) -> str:
    #     if len(s) < 2:
    #         return s
    #     lengthOfLongest = 1
    #     longest = s[0]

    #     def recursion(i,j):
    #         nonlocal lengthOfLongest, longest, s, cache
    #         if i >= len(s) or j >= len(s) or i < 0 or j < 0:
    #             return 
    #         if s[i] == s[j]:
    #             if j-i+1 > lengthOfLongest:
    #                 lengthOfLongest = j-i+1
    #                 longest = s[i:j+1]
    #             recursion(i-1, j+1)
    #     for i in range(len(s)):
    #         recursion(i-1,i+1)
        
    #     for i in range(len(s)-1):
    #         if s[i] == s[i+1]:
    #             if lengthOfLongest < 2:
    #                 lengthOfLongest = 2
    #                 longest = s[i:i+2]
    #             recursion(i-1, i+2)
    #     return longest


    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        longest = s[0]
        lengthOfLongest = 1

        def helper(left,right):
            nonlocal lengthOfLongest, longest,s
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if lengthOfLongest < right - left +1:
                    lengthOfLongest = right - left +1
                    longest = s[left:right+1]
                left -=1
                right +=1

        for i in range(len(s)):
            helper(i-1,i+1)
            if i+1 < len(s) and s[i] == s[i+1]:
                if lengthOfLongest < 2:
                    lengthOfLongest = 2
                    longest = s[i:i+2]
                helper(i-1,i+2)
        
        
        
        return longest
    


            
        