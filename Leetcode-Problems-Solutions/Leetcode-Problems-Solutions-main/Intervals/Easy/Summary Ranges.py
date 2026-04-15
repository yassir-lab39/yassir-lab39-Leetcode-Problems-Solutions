class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == [] :
            return []
        a = nums[0]
        b = 0.5
        res = []
        for i in range(1,len(nums)) :
            if nums[i] == nums[i-1]+1 :
                b = nums[i]
            else :
                if b == 0.5 :
                    res.append(str(a))
                else :
                    res.append(str(a)+"->"+str(b))
                    b = 0.5
                a = nums[i]
        if b == 0.5 :
            res.append(str(a))
        else :
            res.append(str(a)+"->"+str(b))
        return res
