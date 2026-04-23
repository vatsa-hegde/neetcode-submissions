class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        heapq.heapify(hand)
        freq = defaultdict(int)
        for i in hand:
            freq[i] += 1
        while hand:
            ele = heapq.heappop(hand)
            for j in range(ele+1, ele + groupSize):
                # print(ele, j, hand)
                if j in freq and freq[j] > 0:
                    freq[j] -= 1
                    hand.remove(j)
                    heapq.heapify(hand)
                else:
                    return False
        return True
            



