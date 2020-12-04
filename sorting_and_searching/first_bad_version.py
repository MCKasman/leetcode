# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int

        Use binary search
        1 2 3 (4) 5
        F F F  T  T

        Algorithm:
        1. Caluclate start, mid, and end indexes
        2. Update start, mid, and end numbers as you check if you don't locate the bad version
        3. Return the bad version, which should be start

        Time Complexity: O(logN)
        Space Complexity: O(1)
        """
        start = 1
        end = n

        while(start<end):
            mid = (start+end)//2
            if(isBadVersion(mid)):
                end = mid
            else:
                start = mid+1
        return start



        
