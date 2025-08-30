# 136 Single Number
class Solution(object):
    def singleNumber(self, nums):
        """
        Recursive solution to find the single number using XOR.

        Approach:
        - XOR all numbers in the array.
        - Since every number appears twice except one, pairs cancel out.
        - The remaining number is the single one.
        - Linear runtime, constant extra space.
        """

        # Base case: if only one element, return it
        if len(nums) == 1:
            return nums[0]

        # Recursive XOR of first element with the result of the rest
        return nums[0] ^ self.singleNumber(nums[1:])


# ---------------- Example Usage ----------------
sol = Solution()
nums = [4,1,2,1,2]
print(sol.singleNumber(nums))  # Output: 4
