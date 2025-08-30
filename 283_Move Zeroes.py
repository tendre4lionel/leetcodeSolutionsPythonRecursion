# 283 Move Zeroes
class Solution(object):
    def moveZeroes(self, nums):
        """
        Move all zeros to the end of the array in-place using recursion
        without a separate zero-filling function.
        
        :type nums: List[int]
        :rtype: None
        """
        def move(index, last_non_zero):
            # Base case: finished array
            if index == len(nums):
                return
            
            # If current element is non-zero, swap with last_non_zero position
            if nums[index] != 0:
                nums[last_non_zero], nums[index] = nums[index], nums[last_non_zero]
                last_non_zero += 1
            
            # Recurse to next element
            move(index + 1, last_non_zero)
        
        # Start recursion from index 0
        move(0, 0)
