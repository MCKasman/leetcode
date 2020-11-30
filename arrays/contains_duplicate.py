class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        [1,2,3,1] ---> [1,1,2,3]

        1. Sort the array

        2. Check if pointers equal to each other

        2. i==j --> True, done
        """

        length = len(nums)
        nums.sort()
        i = 0

        while(i<length-1):
            if(nums[i]==nums[i+1]):
                return True
            i+=1
        return False
