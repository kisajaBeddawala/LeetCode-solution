# Maximum Subarray

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane's Algorithm
        current_sum = nums[0]
        max_sum = nums[0]
        for i in range(1,len(nums)):
            if current_sum + nums[i] <= nums[i]:
                current_sum = nums[i]
            else:
                current_sum += nums[i]
            
            max_sum = max(max_sum, current_sum)

        return max_sum

        