# 268 Missing Number
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Get the length of the array
        n = len(nums)
        
        # Calculate the expected sum of numbers from 0 to n
        expected_sum = n * (n + 1) // 2
        
        # Calculate the actual sum of the numbers in the array
        actual_sum = sum(nums)
        
        # The missing number is the difference
        return expected_sum - actual_sum

