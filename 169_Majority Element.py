# 169 Majority Element
class Solution(object):
    def majorityElement(self, nums):
        """
        Fully recursive solution without any loops.
        """

        # Base case: single element
        if len(nums) == 1:
            return nums[0]

        # Divide array into two halves
        mid = len(nums) // 2
        left_major = self.majorityElement(nums[:mid])
        right_major = self.majorityElement(nums[mid:])

        # If both halves agree
        if left_major == right_major:
            return left_major

        # Recursive function to count occurrences of target
        def count(nums, target, index=0):
            if index == len(nums):
                return 0
            return (1 if nums[index] == target else 0) + count(nums, target, index + 1)

        # Count occurrences recursively
        left_count = count(nums, left_major)
        right_count = count(nums, right_major)

        return left_major if left_count > right_count else right_major


# ---------------- Example Usage ----------------
sol = Solution()
nums = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums))  # Output: 2
