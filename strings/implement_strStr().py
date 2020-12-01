class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int

        Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

        Algorithm

        1. Traverse through all substrings in string (every substring of N characters)
        2. Find out which substring matches the needle
        3. Return the haystack index
        """

        length = len(haystack)

        if(needle == ""):
            return 0

        if(len(needle)>len(haystack)):
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if(haystack[i:i+len(needle)] == needle):
                return i

        return -1
