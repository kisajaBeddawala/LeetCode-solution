# Move Zeroes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0
        while p2 < len(nums):
            if nums[p2] == 0:
                p2 += 1
            else:
                if nums[p1] == 0:
                    temp = nums[p1]
                    nums[p1] = nums[p2]
                    nums[p2] = temp
                p1 += 1
                p2 += 1
        