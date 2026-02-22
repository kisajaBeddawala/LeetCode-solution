# Binary Gap

class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        # get binary num
        bNum = bin(n)[2:]

        ind = bNum.find('1')
        dis = 0
        maxDis = 0
        for index,n in enumerate(bNum):
            if n == '1':
                dis = index - ind
                ind = index
                maxDis = max(dis,maxDis)
        return maxDis
            



        