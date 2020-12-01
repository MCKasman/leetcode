class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        Given a non-empty array of decimal digits representing a non-negative integer, increment one to the               integer.

        [1,2,4] --> [1,2,5]

        [1,2,9] --> [1,3,0]

        [1,2,3,9,9,9] --> [1,2,4,0,0,0]
        
        [9,9,9] --> [1,0,0,0]

        1. Increment LSB by 1 and return digit if the LSB isn't 9
        2. If LSB and prior digits are 9, make the 9's 0
        3. If [9,9,9], increase array and make first index 1 --> [1,0,0,0]
        """
        length = len(digits)
        i = length-1

        while(i>=0):
            if(digits[i]<9):
                digits[i]+=1
                return digits
            digits[i] = 0
            i-=1

        new_array = [0]*(length+1)
        new_array[0] = 1

        return new_array
