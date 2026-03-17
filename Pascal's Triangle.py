# Pascal's Triangle

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        if numRows == 0:
            return ans
        elif numRows == 1:
            ans.append([1])
            return ans
        elif numRows == 2:
            ans.append([1])
            ans.append([1,1])
            return ans
        else:
            ans.append([1])
            ans.append([1,1])
            for i in range(3,numRows+1):
                temp = [1,1]
                index = 1
                for j in range(len(ans[-1])-1):
                    tot = ans[-1][j] + ans[-1][j+1]
                    temp.insert(index,tot)
                    index += 1
                ans.append(temp)
            return ans

        