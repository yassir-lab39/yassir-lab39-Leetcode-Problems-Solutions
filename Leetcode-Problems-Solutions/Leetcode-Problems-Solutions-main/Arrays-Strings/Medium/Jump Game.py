class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        i = 0
        p = nums[0]
        while i < n :
            if p == 0 :
                return False
            p -= 1
            i += 1
            if i == n-1 :
                return True
            if p < nums[i] :
                p = nums[i]        
                        


        
