class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.child = []

    def __eq__(self,other):
        if not isinstance(other, TreeNode):
            return False
        return self.val == other.val

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            node = TreeNode(letter)
            if node in cur.child:
                cur = cur.child[cur.child.index(node)]
                continue
            cur.child.append(node)
            cur = node
        cur.child.append('#')


    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            node = TreeNode(letter)
            if node in cur.child:
                cur = cur.child[cur.child.index(node)]
            else:
                return False
        if '#' in cur.child:
            return True
        return False
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            node = TreeNode(letter)
            if node in cur.child:
                cur = cur.child[cur.child.index(node)]
            else:
                return False
        return True
        
        