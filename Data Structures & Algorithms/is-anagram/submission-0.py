class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for j in t:
            if j not in d:
                return False
            else:
                d[j] -= 1
        val = d.values()
        for k in val:
            if k > 0:
                return False
        return True
        