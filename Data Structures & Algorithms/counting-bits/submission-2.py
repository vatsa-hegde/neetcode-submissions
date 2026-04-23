class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        sig = 0

        for i in range(1,n+1):
            if i == 2:
                sig = 2
            if i > 0 and i == sig *2:
                sig = i
            dp[i] = 1+dp[i-sig]
        return dp


