class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        nb = 1
        if n == 1 :
            return 0
        while i < n :
            if i + nums[i] >= n-1 :
                return nb
            maxi = 0
            maxi_id = 0
            for j in range(i+1,i+1+nums[i]) :
                if maxi < nums[j] + j - i :
                    maxi = nums[j] + j - i
                    maxi_id = j
            i = maxi_id
            nb += 1
        return nb            

