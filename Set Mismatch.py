# Set Mismatch

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        for i in nums:
            if i in seen:
                duplicate = i  # we have one duplicate, so we can break out of the loop once we find it
                break
            else:
                seen.add(i)

        length = len(nums)
        total = length * (length + 1) / 2  # sum of numbers 1 to n
        dif = total - sum(nums)
        missing = duplicate + dif

        return [duplicate,missing]

        