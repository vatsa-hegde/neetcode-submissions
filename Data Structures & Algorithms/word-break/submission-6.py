class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Approach
        Go over each letter, keep track of the current word, see if it makes sense
        If it is in dict, reset the current word in one case and send a case where you do not reset to check other possibilities
        when the last letter comes check if that makes sense, If it does then return true
        else return false. 
        """
        if len(s) == 0 or len(wordDict) == 0:
            return False
        dictionary = set(wordDict)
        cache = {}
        def  dfs(i, j):
            nonlocal dictionary, s,cache

            if j == len(s)-1:
                if s[i:j+1] in dictionary:
                    return True
                return False
            if (i,j) in cache:
                return cache[(i,j)]
            cache[(i,j)] = dfs(i,j+1)
            if s[i:j+1] in dictionary:
                cache[(i,j)] |= dfs(j+1,j+1)
            return cache[(i,j)]
        return dfs(0,0)

        