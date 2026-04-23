class Trie:
    def __init__(self):
        self.children = {}
        self.eow = False
    
    def addWord(self,word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = Trie()
            cur = cur.children[w]
        cur.eow = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        res, visit = set(),set()
        for word in words:
            root.addWord(word)
        row, col = len(board), len(board[0])

        def dfs(r,c,node, word):
            nonlocal res, row,col,visit,board
            if (c < 0 or c >= col or r < 0 or r >= row or (r,c) in visit or board[r][c] not in node.children):
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.eow:
                res.add(word)
            dfs(r+1,c,node, word)
            dfs(r-1,c,node, word)
            dfs(r, c+1, node,word)
            dfs(r,c-1,node, word)
            visit.remove((r,c))
            return
        
        for r in range(row):
            for c in range(col):
                dfs(r,c,root, "")
        
        return list(res)
            




        