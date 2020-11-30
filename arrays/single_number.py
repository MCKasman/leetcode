class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Given a non-empty array of integers nums, every element appears twice except for one.           Find that single one.

        Algorithm

        Use hash table

        1. Iterate through all elements in the array and set up key/value pair.
        2. Return the element which appeared only once.
        """

        hash_table = defaultdict(int)

        for i in nums:
            hash_table[i]+=1

        for i in hash_table:
            if(hash_table[i]==1):
                return i
