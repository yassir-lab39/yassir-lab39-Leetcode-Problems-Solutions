class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = k % len(nums)
        L=[]
        for i in range(0,n):
            L.append(nums[len(nums)-n+i])
        for i in range(0,len(nums)-n):
            L.append(nums[i])   
        nums[0:len(nums)-n] = L[0:len(nums)-n]
        nums[len(nums)-n:len(nums)] = L[len(nums)-n:len(nums)]
        
