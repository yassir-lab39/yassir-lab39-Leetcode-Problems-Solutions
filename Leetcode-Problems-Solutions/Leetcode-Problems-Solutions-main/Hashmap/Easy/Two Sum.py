class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = dict()
        for i in range(len(nums)) :
            if nums[i] in D :
                if 2*nums[i] == target :
                    return [D[nums[i]],i]
            else :
                D[nums[i]] = i
            if target-nums[i] in D and D[target-nums[i]] != i :
                return [i,D[target-nums[i]]]
        return False
