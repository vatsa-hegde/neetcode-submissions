class Solution:
    # Bottom up
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        I should look for a number which is greater than the current number. 
        I should start looking from the right. For each number I should go over the next numbers and if the next number is greater then I should add 1 for the current subsequence] 
        If that is not the case I should move to next one
        """

        dp = [1]*(len(nums)+1)
        dp[len(nums)] = 0

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)
