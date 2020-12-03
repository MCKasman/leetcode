class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int

        Given a 32-bit signed integer, reverse digits of an integer.

        Algorithm
        1. If negative, turn the integer positive and turn back negative after reversing it
        2. Pop last digit of integer by Modulo 10
        3. Divide integer by 10 to get the digit at the next place
        4. Push last digit into variable
        5. Check if reversed output overflows -- 2^31
        """

        is_negative = False

        if(x < 0):
            is_negative = True
            x*=-1

        reverse = 0

        while(x!=0):
            pop = x%10
            x/=10
            reverse = reverse * 10 + pop

        if(is_negative):
            reverse*=-1

        if reverse >= 2**31 or -(2**31) >= reverse:
            return 0

        return reverse
