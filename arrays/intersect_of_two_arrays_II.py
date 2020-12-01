class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        Given two arrays, write a function to compute their intersection.

        Algorithm

        Use hashmap

        1. If length of first array is smaller than second array swap them
        2. Count frequency of elements in the array and store them into hashmap
        3. If element in second array is present in the hashmap and the frequency is not zero, then decrease the frequency by 1 and insert the element into resultant array
        4. Return resultant array
        """
        hash_map = defaultdict(int)
        result = []

        if(len(nums1) < len(nums2)):
            nums1, nums2 = nums2, nums1

        for i in nums1:
            if i not in hash_map:
                hash_map[i]=1
            else:
                hash_map[i]+=1

        for i in nums2:
            if i in hash_map and hash_map[i]:
                hash_map[i]-=1
                result.append(i)

        return result
