# 217 Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def helper(index, seen):
            """
            Recursive helper function to check for duplicates.
            :param index: current index in nums
            :param seen: set of numbers already seen
            :return: True if a duplicate is found, False otherwise
            """
            # Base case: reached the end of the array
            if index == len(nums):
                return False
            
            # If current number is already in 'seen', duplicate found
            if nums[index] in seen:
                return True
            
            # Add current number to 'seen'
            seen.add(nums[index])
            
            # Recurse for next index
            return helper(index + 1, seen)
        
        # Start recursion from index 0 with an empty set
        return helper(0, set())

