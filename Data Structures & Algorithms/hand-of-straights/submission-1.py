class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        freq = defaultdict(int)
        for i in hand:
            freq[i] += 1
        while hand:
            ele = hand.pop(0)
            for j in range(ele+1, ele + groupSize):
                # print(hand, ele)
                if j in freq and freq[j] > 0:
                    freq[j] -= 1
                    hand.remove(j)
                else:
                    return False
        return True
            



