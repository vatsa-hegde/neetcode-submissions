class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.pointer1 = 0
        self.pointer2 = 0
        self.turn = True
        
    """
    v1= [1,2]
    v2 = [3,4,5,6]
    p1 = -1
    p2 = -1

    """
    def next(self) -> int:
        res = -1
        if self.pointer1 >= len(self.v1) and self.pointer2 >= len(self.v2):
            return res
        elif self.pointer1 >= len(self.v1):
            res = self.v2[self.pointer2]
            self.pointer2+= 1
        elif self.pointer2 >= len(self.v2):
            res = self.v1[self.pointer1]
            self.pointer1 += 1
        else:
            if self.turn:
                self.turn = False
                res = self.v1[self.pointer1]
                self.pointer1+=1
            else:
                self.turn = True
                res = self.v2[self.pointer2]
                self.pointer2+=1
        return res

        

    def hasNext(self) -> bool:
        if self.pointer1 < len(self.v1) or self.pointer2 < len(self.v2):
            return True
        return False
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
