class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = [(len(word),word) for word in wordDict]
        minLen = n
        for l,word in wordDict:
            if l < minLen:
                minLen = l
        mem = [None for _ in range(n)]
        def backtrack(i):
            if i == n:
                return True
            elif n-i < minLen:
                mem[i] = False
                return mem[i]
            if mem[i] != None:
                return mem[i] 
            for l,word in wordDict:
                if i+l <= n and s[i:i+l] == word:
                    mem[i] = backtrack(i+l) or (mem[i] if mem[i] is not None else False)
            if mem[i] == None:
                mem[i] = False
                
            return mem[i]
        return backtrack(0)

        