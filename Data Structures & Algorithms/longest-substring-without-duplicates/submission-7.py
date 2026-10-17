class Solution:
    def lengthOfLongestSubstring(self, s: string) -> int:
        res = 0
        left = right = 0
        d = {}

        while right < len(s):
            if s[right] in d:
                if d[s[right]] >= left:
                    left = d[s[right]]+1
            d[s[right]] = right
            if right - left+1 > res:
                res = right - left + 1
            right += 1
        return res
            
            


            