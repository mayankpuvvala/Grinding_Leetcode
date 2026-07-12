class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        def in_sec(time):
            h,m,s= map(int, time.split(":"))
            return h*3600+m*60+s

        start, end= in_sec(startTime), in_sec(endTime)
        return end-start % (24* 60* 60) #24hrs= 24* 60 mins* 60 secs
