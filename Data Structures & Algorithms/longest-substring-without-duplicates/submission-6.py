class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s) 
        track = {}
        res = 0

        left = right = 0

        while left < len(s) and right < len(s) and left <= right:
            if s[right] in track and track[s[right]] >= left:
                if res < right-left:
                    res = right-left
                left = track[s[right]]+1
            track[s[right]] = right
            right+=1
        if right-left >res:
            return right-left
        return res
