class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

        [1,1,2,3] --> [1,2,3,1] --> [1,2,3]

        Algorithm

        1. Check if length is < 2
        2. Traverse through the array, i is left pointer & j is right pointer
        3. If i!=j then increment i and replace element at i with element at j
        4. After done traversing update length of new array with index of pointer i+1
        5. Create new array and update it with old array by looping through by how much the length is
        6. Print results and return length
        """

        length = len(nums)

        if(length < 2):
            print(length, ", nums = ", nums)
            return length

        i = 0

        for j in range(1,length):
            if nums[i]!=nums[j]:
                i+=1
                nums[i] = nums[j]

        length = i+1

        arr = list(range(0,length))

        for x in range(length):
            arr[x] = nums[x]

        print(length, ", nums = ", arr)

        return length
