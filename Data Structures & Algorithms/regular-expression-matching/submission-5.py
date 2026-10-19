class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        nnn
        n*

        s[i] == p[j] or p[j] == "."

        if next char is *
        then either zero occurance or have one and go one with the same 
        merge the result
        I have to come from right

        

        [
        F F F F
        F F F F
        F F T F
        F F F T
        ]
        lp = 3
        ls = 3
        i j 
        2 1

        xyz
        .*z
        match = true

        """

        dp = [False] * (len(p)+1)
        dp[len(p)] = True

        for i in range(len(s), -1, -1):
            newDp = [False] * (len(p)+1)
            newDp[len(p)] = (i == len(s))
            for j in range(len(p)-1, -1,-1):
                match = (i < len(s) and (s[i] == p[j] or p[j] == "."))

                if (j+1) < len(p) and p[j+1] == "*":
                    newDp[j] = newDp[j+2]
                    if match:
                        newDp[j] |= dp[j] 
                elif match:
                    newDp[j] = dp[j+1]
            dp = newDp
        return dp[0]



        
        