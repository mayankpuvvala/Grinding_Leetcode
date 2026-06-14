class Twitter:

    def __init__(self):
        self.users= defaultdict(set)
        self.tweets= defaultdict(list)
        self.order= 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.order, tweetId])
        self.order-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        # get following and user and do heapify till first 10
        res, heap = [], []
        all_users = self.users[userId] | {userId}

        for user in all_users:
            tweets = self.tweets[user]
            if tweets:
                idx= len(tweets)-1
                heapq.heappush(heap, [tweets[idx][0], user, tweets[idx][1], idx]) 
                #[order, userId, tweetId, idx]
        while heap and len(res)<10:
            order, userId, tweetId, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx>0:
                idx-=1
                tweets= self.tweets[userId]
                heapq.heappush(heap, [tweets[idx][0], userId, tweets[idx][1], idx])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)