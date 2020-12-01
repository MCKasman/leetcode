class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Given an array of integers nums and an integer target, return indices of the two               numbers such that they add up to target.
        
        Input: nums = [2,7,11,15], target = 9

        Output: [0,1]
        Output: Because nums[0] + nums[1] == 9, we return [0, 1].

        Algorithm

        Use hash map

        1. Create hash map that maps values of the array, array value (key) & index (value)
        2. Calculate complement number, complement = target - nums[i]
        3. Get the complement value from hash map
        4. Return indexes

        """

        length = len(nums)
        hash_map = defaultdict(int)

        for i in range(length):
            complement = target - nums[i]

            if(complement in hash_map):
                return [hash_map[complement], i]

            else:
                hash_map[nums[i]] = i
