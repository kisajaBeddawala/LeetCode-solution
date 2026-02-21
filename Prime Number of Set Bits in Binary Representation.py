# Prime Number of Set Bits in Binary Representation

class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        tot = 0
        for i in range(left,right+1):
            # convert to binary number
            bNum = bin(i)[2:]

            # get count of 1s in binary number
            c = 0
            for j in bNum:
                if j == "1":
                    c += 1

            # check if number is prime
            if c != 0 and c != 1:
                if c == 2:
                    tot += 1
                else:
                    remain = 0
                    for k in range(2,c):
                        if c % k == 0:
                            remain += 1
                        if remain > 1:
                            break
                    if remain == 0:
                        tot += 1

        return tot

            
        