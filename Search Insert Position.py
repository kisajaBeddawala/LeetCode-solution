class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # use binary search to find the target or the insert position
        start = 0
        end = len(nums)-1

        while end >= start:
            mid = start + ((end - start) // 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return start  #if not found, start will be the insert position
        