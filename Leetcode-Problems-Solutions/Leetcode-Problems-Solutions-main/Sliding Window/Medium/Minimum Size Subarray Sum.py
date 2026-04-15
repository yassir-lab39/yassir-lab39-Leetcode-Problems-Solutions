class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = nums[0]
        i, j = 0, 1
        nb = 0
        while i < len(nums) :
            while s < target and j < len(nums) :
                s += nums[j]
                j += 1
            if s >= target :
                if nb == 0 or nb > j-i :
                    nb = j-i
            s -= nums[i]
            i += 1
        return nb
