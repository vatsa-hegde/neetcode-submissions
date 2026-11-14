class Solution:
    def reverse(self, x: int) -> int:
        """
        01101
        13
        31
        11111
        """

        num = abs(x)

        res = int(str(num)[::-1])

        if res > (1 << 31)-1:
            return 0
        return res if x > 0 else -res
    

        