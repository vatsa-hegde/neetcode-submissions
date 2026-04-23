class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        r = 0
        h = []
        while r < len(nums):
            heapq.heappush(h,(-nums[r], r))
            if r < k-1:
                r+=1
                continue
            m, i = h[0]
            # print(i)
            while r-k+1 > i:
                heapq.heappop(h)
                m, i = h[0]
                # print(i)
            print(r, h)
            res.append(-m)
            r += 1
        return res

                


        

        