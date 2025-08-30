class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Recursive binary search to find the index to insert target in a sorted array.
        """

        def binary_search(left, right):
            """
            Recursively search in nums[left:right+1] for target.
            """
            # Base case: search space exhausted
            if left > right:
                # Target not found, should be inserted at 'left'
                return left

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid  # Found target
            elif nums[mid] < target:
                # Search in the right half
                return binary_search(mid + 1, right)
            else:
                # Search in the left half
                return binary_search(left, mid - 1)

        # Start recursion on the full array
        return binary_search(0, len(nums) - 1)


# Example usage:
sol = Solution()
nums = [1,3,5,6]
target = 5
print(sol.searchInsert(nums, target))  # Output: 2

target = 2
print(sol.searchInsert(nums, target))  # Output: 1

target = 7
print(sol.searchInsert(nums, target))  # Output: 4

target = 0
print(sol.searchInsert(nums, target))  # Output: 0
