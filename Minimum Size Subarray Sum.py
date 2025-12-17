class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        # Brute Force Approach - O(n^2) Time Complexity
        # this approach times out for large inputs
        
        # min_length = len(nums)
        # if sum(nums) < target:
        #     return 0
        # for i in range(len(nums)):
        #     total = nums[i]
        #     length = 1
        #     if total < target:
        #         for j in range(i+1, len(nums)):
        #             total += nums[j]
        #             length += 1
        #             if total >= target:
        #                 min_length = min(min_length, length)
        #                 break
        #     elif total >= target:
        #         return length

        # return min_length

        left = 0
        right = 0
        min_len = float('inf')
        total = 0
        while right < len(nums):
            total += nums[right]
            while total >= target:
                min_len = min((right-left + 1),min_len)
                total -= nums[left]
                left += 1
        
            right += 1
        if min_len == float('inf'):
            return 0
        else:
            return min_len
        