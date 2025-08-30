class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        Fully recursive solution to remove all occurrences of val in-place.
        Returns the number of elements not equal to val.
        """

        def helper(index, write_index):
            """
            Recursively processes nums starting at 'index'.
            
            index: current position being read
            write_index: next position to write a non-val element
            """
            # Base case: reached the end of the array
            if index == len(nums):
                return write_index  # Number of elements not equal to val

            if nums[index] != val:
                # If current element is not val, write it at write_index
                nums[write_index] = nums[index]
                write_index += 1  # Move write_index forward

            # Recurse to the next element
            return helper(index + 1, write_index)

        # Start recursion from index 0, write_index 0
        return helper(0, 0)


# Example usage:
sol = Solution()
nums = [3,2,2,3,4,3,5]
val = 3
k = sol.removeElement(nums, val)
print(f"Number of elements not equal to {val}: {k}")
print(f"Array after removal: {nums[:k]}")
