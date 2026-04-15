class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        a = False
        if len(nums) < 3:
            return len(nums)  
        if nums[0] != nums[1] :
            j += 1
        if nums[len(nums)-2] == nums[len(nums)-1] :  
            a = True
        for i in range(1,len(nums)-1):
            if nums[i-1] == nums[i] and nums[i] != nums[i+1]:
                nums[j] = nums[i]
                nums[j+1] = nums[i]
                j += 2
            if  nums[i-1] != nums[i] and nums[i] != nums[i+1]: 
                nums[j] = nums[i]
                j += 1 
        if nums[len(nums)-2] != nums[len(nums)-1] :
            nums[j] = nums[len(nums)-1]
            j += 1
        if a == True :   
            nums[j] = nums[len(nums)-1]
            nums[j+1] = nums[len(nums)-1]
            j += 2
        print(nums)    
        return j 
