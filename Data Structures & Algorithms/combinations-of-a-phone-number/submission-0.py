class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps = {
            '2' : ['a','b','c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','v','u'], 
            '9' : ['w','x','y','z'],
        }
        res = []
        n = len(digits)
        if n < 1:
            return []
        def recurse(ans, dig):
            if len(dig) == 0:
                res.append(ans)
                return
            for i in maps[dig[0]]:
                recurse(ans+i, dig[1:])
        recurse("",digits)
        return res



            
        