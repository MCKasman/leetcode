class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int

        Given a string, find the first non-repeating character in it and return its index. If         it doesn't exist, return -1.

        Algorithm
        
        1. Create a Hash Map and count the frequency of the character
        2. Enumerate string
        2. Return the character with 1 frequency
        """
        # build hash map
        count = collections.Counter(s)

        # find the index
        for index, char, in enumerate(s):
            if(count[char] == 1):
                return index

        return -1
