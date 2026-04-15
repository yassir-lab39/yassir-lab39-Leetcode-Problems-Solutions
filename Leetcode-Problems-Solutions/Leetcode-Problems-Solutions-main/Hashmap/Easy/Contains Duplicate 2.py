class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        D = dict()
        for i in range(len(nums)) :
            if nums[i] not in D :
                D[nums[i]] = i
            else :
                if i-D[nums[i]] <= k :
                    return True
                D[nums[i]] = i
        return False
