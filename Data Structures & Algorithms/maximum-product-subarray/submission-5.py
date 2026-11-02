class Solution:
    """
    """
    def maxProduct(self, nums: List[int]) -> int:
        max_product = float('-inf')

        cur_min, cur_max = 1,1
        for n in nums:
            temp = cur_max
            cur_max = max(cur_max * n, cur_min * n , n)
            cur_min = min(temp*n, cur_min*n, n)
            max_product = max(cur_max,max_product)
        return max_product


            
            


        