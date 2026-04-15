class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == [] :
            return [newInterval]
        n = len(intervals)
        for i in range(n) :
            if newInterval[0] < intervals[i][0] :
                intervals.insert(i,newInterval)
                index = i
        if n == len(intervals) :
            intervals.append(newInterval)
        res = [intervals[0]]
        for i in range(len(intervals)) :
            if intervals[i][0] <= res[-1][1] :
                if intervals[i][1] > res[-1][1] :
                    res[-1] = [res[-1][0],intervals[i][1]]
            else :
                res.append(intervals[i])
        return res
