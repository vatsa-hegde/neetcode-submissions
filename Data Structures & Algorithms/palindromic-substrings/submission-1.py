class Solution:
    """
    a b c

    """
    def countSubstrings(self, s: str) -> int:
        numberOfPalindromes = 0

        for i in range(len(s)):
            left, right = i,i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                numberOfPalindromes += 1
                left -= 1
                right += 1
            
            left, right = i, i+1
            while left >=0 and right < len(s) and s[left] == s[right]:
                numberOfPalindromes += 1
                left -= 1
                right += 1
        
        return numberOfPalindromes

        