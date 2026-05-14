class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res+= str(len(s)) + "#" + s 
        return res

    def decode(self, s: str) -> List[str]:
        # if len(s) == 0:
        #     return [s]
        res = []
        i = 0
        while i < len(s):
            num = 0
            while s[i] != '#':
                print(s[i])
                num = 10*num + int(s[i])
                i+=1
            res.append(s[i+1:i+1+num])
            i += num+1
        return res

