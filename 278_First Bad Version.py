# 278 First Bad Version
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Recursive binary search helper
        def search(left, right):
            # Base case: when left == right, we've found the first bad version
            if left == right:
                return left
            
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                # First bad version is in the left half (including mid)
                return search(left, mid)
            else:
                # First bad version is in the right half (excluding mid)
                return search(mid + 1, right)
        
        return search(1, n)
