import time
class Twitter:

    def __init__(self):
        self.posts = {}
        self.followers = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].append((time.time(),tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feeds = []
        if userId in self.posts:
            feeds+=self.posts[userId]
        if userId in self.followers:
            for f in self.followers[userId]:
                feeds+= self.posts[f]
        final_feeds = [y for x,y in heapq.nlargest(10,feeds)]
        return final_feeds

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or (followerId in self.followers and followeeId not in self.followers[followerId]):
            return
        self.followers[followerId].remove(followeeId)
        
