class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        temp = [[] for _ in range(len(nums)+1)]
        for key,val in d.items():
            temp[val].append(key)
        res = []
        for i in range(len(nums), 0 , -1):
            if k == 0:
                break
            while(k>0 and len(temp[i])>0):
                res.append(temp[i].pop())
                k-=1
        return res

        