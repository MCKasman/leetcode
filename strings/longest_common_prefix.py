class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str

        Write a function to find the longest common prefix string amongst an array of strings.

        Input: strs = ["flower","flow","flight"]
        Output: "fl"

        Algorithm
        1. Check if string is empty
        2. Find the shortest string to compare the characters with
        3. Enumerate characters of the shortest string
        4. Compare characters of words in string list with enumerated characters
        5. If the characters don't equal each other then return the substring of the shortest string that matches         with the other words
        """
        if not strs:
            return ""

        shortest_str = min(strs,key=len)

        for i,char in enumerate(shortest_str):
            for word in strs:
                if(word[i]!=char):
                    return shortest_str[:i]

        return shortest_str
