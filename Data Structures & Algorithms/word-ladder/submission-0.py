class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        patterns = collections.defaultdict(list)
        visit = set([beginWord])
        res = 1
        q = deque([beginWord])
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + '*' + w[i+1:]
                patterns[pattern].append(w)
        
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j  in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for p in patterns[pattern]:
                        if p not in visit:
                            visit.add(p)
                            q.append(p)           
            res+=1
        return 0