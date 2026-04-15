class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = 1
        nb = 0
        for i in range(n) :
            if nums[i] != 0:
                prod = prod*nums[i]
            else :
                j = i
                nb += 1
        if nb > 1 :
            return [0]*n  
        if nb == 1 :
            return [0]*j + [int(prod)] + [0]*(n-j-1)
        answer = []
        for i in range(n) :
            answer.append(int(prod/nums[i]))         
        return answer     

        
