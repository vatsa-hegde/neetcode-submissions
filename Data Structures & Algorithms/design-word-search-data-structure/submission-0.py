class Node:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for l in word:
            if l not in cur.children:
                cur.children[l] = Node()
            cur = cur.children[l]
        cur.eow = True 

    def search(self, word: str) -> bool:
        def dfs(j,node):
            cur = node
            nonlocal word
            for i in range(j,len(word)):
                l = word[i]
                if l == ".":
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if l not in cur.children:
                        return False
                    cur = cur.children[l]
            return cur.eow
        return dfs(0,self.root)
            
        
