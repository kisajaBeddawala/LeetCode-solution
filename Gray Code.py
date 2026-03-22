# Gray Code

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        gray = set()
        num = "0" * n
        # print(num)
        while len(ans) < 2**n:
            ans.append(int(num,2))
            gray.add(num)

            # print(ans)

            while num in gray and len(ans) < 2 ** n:
                for idx in range(len(num)):
                    if num[idx] == "0" and (num[:idx]+"1"+num[idx+1:]) not in gray:
                        num = num[:idx]+"1"+num[idx+1:]
                        # print(num)
                        break
                    elif num[idx] == "1" and (num[:idx]+"0"+num[idx+1:]) not in gray:
                        num = num[:idx]+"0"+num[idx+1:]
                        break

        return ans