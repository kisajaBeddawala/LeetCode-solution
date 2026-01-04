# Permutations

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # perm = itertools.permutations(nums)
        # res = []
        # for i in perm:
        #     res.append(list(i))
        # return res

        # Backtracking approach
        res = []
        def backtrack(path):
            if len(path) == len(nums):
                res.append(list(path))
                return 
            
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()
        backtrack([])
        return res
            


        