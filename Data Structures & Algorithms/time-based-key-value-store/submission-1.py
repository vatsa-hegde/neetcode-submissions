class TimeMap:

    def __init__(self):
        self.d = {}


        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append((value,timestamp))
        else:
            self.d[key] = [(value,timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        val = self.d.get(key,None)
        if not val:
            return ""
        l = 0
        r = len(val)-1
        res = ""
        while l <= r:
            if val[l][1] > timestamp:
                return res
            mid = (l+r)//2
            if val[mid][1] == timestamp:
                return val[mid][0]
            elif val[mid][1] > timestamp:
                r = mid-1
            else:
                res = val[mid][0]
                l = mid+1
        return res


        
