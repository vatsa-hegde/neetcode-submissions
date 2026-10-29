class Solution:
    """
    1 2 3 4
    [ABCD,LCD, AWD]

    1 1 2 3
    [AABC, KBC, ALC, AAW, KW]
    """
    def numDecodings(self, s: str) -> int:
        cache = {}
        def recursion(i):
            nonlocal s
            if i in cache:
                return cache[i]
            if i == len(s):
                return 1 
            if s[i] == '0':
                return 0
            cache[i] = recursion(i+1)
            if (i+1) < len(s) and ( s[i] == '1' or (s[i] == '2' and int(s[i+1]) < 7 )):
                cache[i] += recursion(i+2)
            return cache[i]
        return recursion(0)






        