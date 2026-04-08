# Median of Two Sorted Arrays

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        left = 0
        right = 0
        m = len(nums1)
        n = len(nums2)
        array = []
        while right < n and left < m:
            if nums1[left] > nums2[right]:
                array.append(nums2[right])
                right += 1
            else:
                array.append(nums1[left])
                left += 1

        while left < m:
            array.append(nums1[left])
            left += 1

        while right < n:
            array.append(nums2[right])
            right += 1

        # print(array)

        if (n+m) % 2 == 0:
            num = (array[((n+m)/2) - 1] + array[(n+m)/2]) / 2.0
            print(num)
            return num
        else:
            return array[(n+m) // 2]
            
        