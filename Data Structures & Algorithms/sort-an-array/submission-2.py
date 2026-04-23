class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2

            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])

            return merge(left,right)
        
        def merge(left,right):
            i=j=0
            res = []
            while i< len(left) and j <len(right):
                if left[i] > right[j]:
                    res.append(right[j])
                    j+=1
                else:
                    res.append(left[i])
                    i+=1
            if i < len(left):
                res.extend(left[i:])
            if j < len(right):
                res.extend(right[j:])
            return res
        return mergesort(nums)

        



        