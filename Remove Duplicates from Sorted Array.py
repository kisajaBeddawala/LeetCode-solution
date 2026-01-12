# Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 1:
            left = 0
            right = 1
            while right < len(nums) and nums[right] != "_": 
                if nums[left] == nums[right]:
                    nums.pop(right)
                    nums.append("_")
                else:
                    left += 1
                    right += 1
            return right
        else:
            return len(nums)


        