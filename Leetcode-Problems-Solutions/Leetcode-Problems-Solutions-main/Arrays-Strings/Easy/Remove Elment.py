class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = []
        for i in range(0,len(nums)):
            if nums[i] != val:
                L = L + [nums[i]]
        nums[0:len(L)] = L 
        nums[len(L):len(nums)] = (len(nums)-len(L))*["_"]
        return len(L)
                
