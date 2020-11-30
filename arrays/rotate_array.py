class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.

        Given an array, rotate the array to the right by k steps, where k is non-negative.

        i.e. When k = 3 for [1,2,3,4,5,6,7]

        Algorithm

        1. Reverse array

        [1,2,3,4,5,6,7] --> [7,6,5,4,3,2,1]

        2. Reverse first k elements

        [7,6,5,4,3,2,1] --> [5,6,7,4,3,2,1]

        3. Reverse n-k elements

        [5,6,7,1,2,3,4] --> [5,6,7,1,2,3,4]

        """
        length = len(nums)
        k%=length

        self.reverse(nums, 0, length-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, length-1)

    def reverse(self, nums, start, end):
        while(start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
