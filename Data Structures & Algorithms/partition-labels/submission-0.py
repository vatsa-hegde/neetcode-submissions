class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = {}
        res = []
        for i in s:
            if i in freq:
                freq[i][0] += 1
            else:
                freq[i] = [1,False]
        c = None
        length = 0
        for l in s:
            if freq[l][1]:
                c -= 1
                length += 1
            else:
                freq[l][1] = True
                if c:
                    c+= freq[l][0]
                else:
                    c = freq[l][0]
                c -= 1
                length+=1
            if c == 0:
                res.append(length)
                c = None
                length = 0
        return res


                