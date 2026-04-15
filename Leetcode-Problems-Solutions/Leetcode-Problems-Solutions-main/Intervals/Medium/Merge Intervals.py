class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda x : x[0])
        res = [sorted_intervals[0]]
        for i in range(len(sorted_intervals)) :
            if sorted_intervals[i][0] <= res[-1][1] :
                if sorted_intervals[i][1] > res[-1][1] :
                    res[-1] = [res[-1][0],sorted_intervals[i][1]]
            else :
                res.append(sorted_intervals[i])
        return res

        
