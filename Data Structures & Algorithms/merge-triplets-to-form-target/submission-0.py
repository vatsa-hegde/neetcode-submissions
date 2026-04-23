class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0,0,0]
        for i in range(len(triplets)):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue
            res[0] = max(triplets[i][0],res[0])
            res[1] = max(triplets[i][1],res[1])
            res[2] = max(triplets[i][2],res[2])
        if res == target:
            return True
        return False

