class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = {}
        for index,num in enumerate(nums):
            remain = target - num

            # check if remain is already in visited
            if remain in visited:
                return [visited[remain],index]

            visited[num] = index  # when remain not in visited, store num and its index in visited
   