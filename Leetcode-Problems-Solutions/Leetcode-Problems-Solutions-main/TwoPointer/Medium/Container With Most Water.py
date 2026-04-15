class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        area = min(height[left], height[right])*right
        while left <= right :
            if height[left] < height[right] :
                left += 1   
            else :
                right -= 1
            if area < min(height[left], height[right])*(right-left) :
                area = min(height[left], height[right])*(right-left)
        return area
