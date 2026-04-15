class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1 :
            return len(nums)
        i = -1
        count = 1
        while i > -len(nums) :
            if nums[i]+1 == nums[i-1] :
                count += 1
            i -= 1
        if count == len(nums) :
            return count
        S = set(nums)
        visited = set()
        D = dict()
        for n in nums :
            D[n] = 0
        nb = 1
        nb_max = 1
        for n in nums :
            if n in visited :
                continue
            visited.add(n)
            m = n+1
            while m in S :
                visited.add(m)
                if D[m] != 0 :
                    nb += D[m]
                    m += D[m]
                else :
                    nb += 1
                    m += 1
            D[m] = nb
            if nb_max < nb :
                nb_max = nb
            nb = 1
        return nb_max

        

# nums = [50,49,15,10,9,48]  output : 3
# [1,5,4,3,2]
# i = 0 : 
