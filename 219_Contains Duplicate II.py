# 219 Contains Duplicate II
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def helper(i, seen):
            """
            Recursive helper to check duplicates within distance k.
            :param i: current index
            :param seen: set of numbers in the current window
            :return: True if duplicate found, False otherwise
            """
            # Base case: reached end of array
            if i == len(nums):
                return False
            
            # If current number is in the set, duplicate within k
            if nums[i] in seen:
                return True
            
            # Add current number to the set
            seen.add(nums[i])
            
            # Maintain window size <= k
            if len(seen) > k:
                seen.remove(nums[i - k])
            
            # Recurse to next index
            return helper(i + 1, seen)
        
        # Start recursion with empty set at index 0
        return helper(0, set())
