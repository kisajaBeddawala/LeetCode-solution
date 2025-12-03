class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start = 0
        end = len(nums)
        while start < end:
            if nums[start] == val:
                end -= 1
                nums.remove(val)
            else:
                start += 1

        return len(nums)

        