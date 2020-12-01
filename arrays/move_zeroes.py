class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Given an array nums, write a function to move all 0's to the end of it while                   maintaining the relative order of the non-zero elements.

        [0,1,0,3,12] --> [1,0,0,3,12] --> [1,3,0,0,12] --> [1,3,12,0,0]
        
        [2,1] --> [2,1]

        Algorithm
        1. Left pointer is i and right pointer is j, i&j start at index 0 so non-zero numbers         swap with themselves
        2. If j!=0, elements at i and j are swapped, i increments
        3. Return array
        """
        length = len(nums)
        i = 0
        j = 0

        while(j<length):
            if(nums[j]!=0):
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
            j+=1

        return nums
