class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word))+ '#' + word
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            l = ''
            while s[i] != '#':
                l += s[i]
                i+=1
                print(l)
            else:
                print(l)
                l = int(l)
                i+=1
                res.append(s[i: i+l])
                i += l            
        return res
                
                

