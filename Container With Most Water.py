# Container With Most Water

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # two pointer approach
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            if height[left] <= height[right]:
                val = (right-left)*height[left]
                max_area = max(max_area,val)
                left += 1
            else:
                val = (right-left)*height[right]
                max_area = max(max_area,val)
                right -= 1
            
        return max_area