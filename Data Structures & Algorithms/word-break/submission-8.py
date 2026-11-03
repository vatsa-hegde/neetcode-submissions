class Solution:
    # Top Down
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Approach
        Go over each letter, keep track of the current word, see if it makes sense
        If it is in dict, reset the current word in one case and send a case where you do not reset to check other possibilities
        when the last letter comes check if that makes sense, If it does then return true
        else return false. 
        """
        # if len(s) == 0 or len(wordDict) == 0:
        #     return False
        # dictionary = set(wordDict)
        # cache = {}
        # def  dfs(i, j):
        #     nonlocal dictionary, s,cache

        #     if j == len(s)-1:
        #         if s[i:j+1] in dictionary:
        #             return True
        #         return False
        #     if (i,j) in cache:
        #         return cache[(i,j)]
        #     cache[(i,j)] = dfs(i,j+1)
        #     if s[i:j+1] in dictionary:
        #         cache[(i,j)] |= dfs(j+1,j+1)
        #     return cache[(i,j)]
        # return dfs(0,0)
    
    # bottom up
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Approach
        come from the last, be checking whether there is a word
        if there is a word, then check whether j+1 also has a starting word where j is the last character of the current word. If it is true then write true continue. otherwise  continue to next
        I should have the answer at dp[0]
        """
        dp = [False] *(len(s)+1)
        dp[len(s)] = True
        endOfWord = len(s)
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        print(dp)
        return dp[0]

        """
        aaaaaaa
        dp = T f f f T f f T
        """




        