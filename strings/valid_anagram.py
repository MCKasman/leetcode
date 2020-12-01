class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        Algorithm 1:

        Use hash table

        1. Create hash map for both strings
        2. Check if hash tables are equal to each other

        Algorithm 2:

        1. Turn strings to array
        2. Sort both arrays
        3. Check if they both equal each other
        """

#         hash_table1 = collections.Counter(s)
#         hash_table2 = collections.Counter(t)

#         if(hash_table1 == hash_table2):
#             return True
#         else:
#             return False

        if(len(s)!=len(t)):
            return False

        s = list(s)
        t = list(t)

        s.sort()
        t.sort()

        if(s==t):
            return True
        else:
            return False
