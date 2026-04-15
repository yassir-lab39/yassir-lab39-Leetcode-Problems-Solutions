class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        D = {}
        for i in range(len(nums)) :
            if nums[i] in D.keys() :
                D[nums[i]] += 1
            else :
                D[nums[i]] = 1
            if D[nums[i]] > len(nums)//2 :
                return nums[i]    
        
                

        
