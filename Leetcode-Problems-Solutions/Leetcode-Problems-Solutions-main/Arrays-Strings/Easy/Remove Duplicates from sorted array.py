class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1 
        nb = 0
        i = 0 
        while i < len(nums) -1: 
            if nums[i] == nums[i+1]:
                nums[i] = 101 
            else:
                nums[nb],nums[i] = nums[i], nums[nb]
                nb += 1 
            i += 1 
        if nb == 0:
            nums[0] = nums[-1]
            return 1 
        if nums[i] != nums[nb-1]:
            nums[nb] = nums[i]
            nb += 1 
        return nb
    
            
                
            
        
        
