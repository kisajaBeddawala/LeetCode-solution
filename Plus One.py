class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = list(map(str,digits)) #convert each digit to string
        num = "".join(digits) #join all strings to form a number string
        num = int(num) #convert the number string to an integer
        num += 1
        num = str(num) #convert the incremented number back to a string
        return [int(i) for i in num] #convert each character back to an integer and return the list
        