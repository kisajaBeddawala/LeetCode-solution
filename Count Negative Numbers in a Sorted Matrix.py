# Count Negative Numbers in a Sorted Matrix

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Brute Force Approach
        # total = 0
        # for row in grid:
        #     for num in row:
        #         if num < 0:
        #             total += 1
        # return total

        # Binary Search Approach
        total = 0
        for row in grid:
            left = 0
            right = len(row)-1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] < 0:
                    total += (right - mid + 1)
                    right = mid - 1
                elif row[mid] >= 0:
                    left = mid + 1
        return total
                    

        
