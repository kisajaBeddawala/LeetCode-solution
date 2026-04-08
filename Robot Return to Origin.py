# Robot Return to Origin

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        left,up = 0,0
        for i in moves:
            if i == "U":
                up += 1
            elif i == "D":
                up -= 1
            elif i == "L":
                left += 1
            elif i == "R":
                left -= 1
                
        if left == 0 and up == 0:
            return True
        else:
            return False

        