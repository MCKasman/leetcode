class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        
        Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

        Algorithm:
        1. Get length nums 2, iterate from starting to ending index
        2. Replace the elements at nums 1 indexes with elements of nums2
        3. Sort nums1 again
        4. Return nums1

        Time Complexity: O(NlogN)
        Space Complexity: O(N)
        """
        if(m == 0):
            nums1_ptr = 0
        else:
            nums1_ptr = m

        nums2_ptr = 0

        while(nums2_ptr < n):
            nums1[nums1_ptr] = nums2[nums2_ptr]
            nums1_ptr+=1
            nums2_ptr+=1

        nums1.sort()

        return nums1
