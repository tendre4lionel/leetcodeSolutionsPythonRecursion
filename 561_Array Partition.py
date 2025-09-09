# 561 Array Partition
# Algorithm:
# - Sort the array
# - Iterate through even indices and sum the values
# Complexity:
# - Time: O(n log n) for sorting, O(n) for iteration => O(n log n)
# - Space: O(1) extra space (or O(n) if sorting creates a new array)

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        total = 0
        for i in range(0, len(nums), 2):
            total += nums[i]
        return total

# Example usage:
# sol = Solution()
# print(sol.arrayPairSum([1,4,3,2]))  # Output: 4

# Algorithm:
# - Sort array
# - Use recursion with current index and accumulated sum
# - Base case: index >= len(nums)
# - Add every element at even index to sum
# Complexity:
# - Time: O(n log n) for sorting, O(n) recursion => O(n log n)
# - Space: O(n) recursion stack

class Solution(object):
    def arrayPairSum(self, nums, index=0, total=0):
        """
        :type nums: List[int]
        :rtype: int
        """
        if index == 0:  # only sort once
            nums.sort()
        
        if index >= len(nums):
            return total
        
        # Add element at even index
        total += nums[index]
        
        return self.arrayPairSum(nums, index + 2, total)

# Example usage:
# sol = Solution()
# print(sol.arrayPairSum([1,4,3,2]))  # Output: 4



# Algorithm:
# - Sort array
# - Recursively sum first element of each pair
# Complexity:
# - Time: O(n log n) for sorting, O(n) recursion
# - Space: O(n) recursion stack

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if not nums:
            return 0
        # sum first element + recurse on rest of array skipping next element
        return nums[0] + self.arrayPairSum(nums[2:])

# Example usage:
# sol = Solution()
# print(sol.arrayPairSum([1,4,3,2]))  # Output: 4



