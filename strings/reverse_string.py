class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        
        Algorthim 1
        1. User reverse() function ----------- s.reverse()

        Algorithm 2
        1. Get start and end indexes
        2. Increment start and decrement end indexes while swapping element values
        """

        length = len(s)
        start = 0
        end = length-1

        while(start<end):
            s[start], s[end] = s[end], s[start]
            start+=1
            end-=1

        return s
