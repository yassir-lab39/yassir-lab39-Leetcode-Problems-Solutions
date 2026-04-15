class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        nb = 0
        sorted_points = sorted(points, key = lambda x : x[0])
        print(sorted_points)
        [i,j] = sorted_points[0]
        for k in range(len(points)) :
            i = max(i,sorted_points[k][0])
            j = min(j,sorted_points[k][1])
            if i > j :
                nb += 1
                i = sorted_points[k][0]
                j = sorted_points[k][1]
        return nb+1

            
