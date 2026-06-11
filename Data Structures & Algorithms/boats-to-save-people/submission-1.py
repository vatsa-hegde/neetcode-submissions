class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        visited= [False for _ in people]
        diff = defaultdict(list)
        for i in range(len(people)):
            diff[people[i]].append(i)
        res = 0
        
        for i in range(len(people)):
            if not visited[i]:
                remaining = limit - people[i]
                visited[i] = True
                res += 1
                for j in range(remaining,0,-1):
                    if j in diff:
                        idx = None
                        while len(diff[j]) > 0:
                            print(j, people[i])
                            idx = diff[j].pop(0)
                            if not visited[idx]:
                                break
                            idx = None
                        if idx:
                            visited[idx] = True
                            break
                
                

        return res
