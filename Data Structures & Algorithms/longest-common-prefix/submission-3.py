class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        res = strs[0]
        for word in strs:
            i = 0
            if len(word) == 0:
                return ""
            print(word, res)
            if len(word) < len(res):
                res = res[:len(word)]
            while i < len(res):
                if res[i] == word[i]:
                    i+=1
                    continue
                res = res[:i]
                break
                
        return res

        

        