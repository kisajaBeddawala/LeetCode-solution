# Letter Combinations of a Phone Number

import itertools


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nums = {
            "1":"",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        text = []
        for i in digits:
            text.append(list(nums[i]))

        # print(text)

        com = list(itertools.product(*text))
        
        ans = []
        for element in com:
            ans.append("".join(element))
        
        # print(ans)
        return ans