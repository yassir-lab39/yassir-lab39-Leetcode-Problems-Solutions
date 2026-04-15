class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        if nums == [0]*len(nums) :
            return [[0, 0, 0]]
        for i in range(len(nums)-2) :
            if i > 0 and nums[i] == nums[i-1] :
                continue
            j, k = i+1, len(nums)-1
            while j < k :
                if nums[i]+nums[j]+nums[k] > 0 :
                    k -= 1
                elif  nums[i]+nums[j]+nums[k] < 0 :
                    j += 1
                else :
                    L = [nums[i], nums[j], nums[k]]
                    res.append(L)
                    j += 1
                    k -= 1
        unique_lst = [list(x) for x in dict.fromkeys(map(tuple, res))]
        return unique_lst
                
