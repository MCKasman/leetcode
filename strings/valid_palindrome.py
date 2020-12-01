class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring           cases.
        
        Algorithm:

        1. Remove spaces
        2. Remove non-alphanumeric characters
        3. Convert all uppercase to lowercase
        4. Reverse string
        5. Compare string
        """

        result = ""

        for i in s:
            if(i.isalnum()):
                result+=i.lower()

        if(result == result[::-1]):
            return True
        else:
            return False
