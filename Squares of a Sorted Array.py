# Squares of a Sorted Array

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        start = 0
        end = len(nums)-1
        result = [0]*len(nums)
        c = end

        while start <= end:
            if nums[start]**2 < nums[end]**2:
                result[c] = nums[end]**2
                end -= 1
            else:
                result[c] = nums[start]**2
                start += 1 
            c -= 1
        return result   
                