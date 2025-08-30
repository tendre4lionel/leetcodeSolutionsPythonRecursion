# 303 Range Sum Query - Immutable
class NumArray(object):
    def __init__(self, nums):
        """
        Initialize the NumArray object with the integer array nums.
        Precompute a prefix sum array to answer sumRange queries efficiently.
        
        :type nums: List[int]
        """
        # Initialize the prefix sum array with a 0 at the start for convenience.
        # This makes sum from index 0 to i easier to calculate as prefix[i+1] - prefix[0].
        self.prefix = [0]

        # Build the prefix sum array iteratively.
        # Each element in prefix will store the sum of all numbers up to that index in nums.
        for num in nums:
            # Append the sum of the previous prefix sum and the current number.
            self.prefix.append(self.prefix[-1] + num)
            # Example: nums = [1,2,3]
            # Step by step prefix = [0] -> [0,1] -> [0,1,3] -> [0,1,3,6]

    def sumRange(self, left, right):
        """
        Return the sum of the elements of nums between indices left and right inclusive.
        Uses the prefix sum array for O(1) query time.

        :type left: int
        :type right: int
        :rtype: int
        """
        # sumRange(left, right) = sum of nums[left] + ... + nums[right]
        # Using prefix sums, we can compute it in O(1) time:
        # prefix[right + 1] contains sum(nums[0] to nums[right])
        # prefix[left] contains sum(nums[0] to nums[left-1])
        # Their difference is sum(nums[left] to nums[right])
        return self.prefix[right + 1] - self.prefix[left]

        # Example:
        # nums = [1,2,3,4], prefix = [0,1,3,6,10]
        # sumRange(1,3) = prefix[4] - prefix[1] = 10 - 1 = 9
