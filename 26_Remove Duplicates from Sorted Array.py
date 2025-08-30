class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Fully recursive solution to remove duplicates in a sorted array.
        Modifies nums in-place and returns the number of unique elements.
        """

        def helper(index, write_index):
            """
            Recursively process the array.
            
            index: current index being read
            write_index: position to write the next unique element
            """
            # Base case: reached end of the array
            if index == len(nums):
                return write_index  # Number of unique elements

            # If it's the first element or different from previous, write it
            if index == 0 or nums[index] != nums[index - 1]:
                nums[write_index] = nums[index]  # Write current unique element
                write_index += 1  # Move write_index forward

            # Recurse for the next element
            return helper(index + 1, write_index)

        # Start recursion from index 0, write_index 0
        return helper(0, 0)


# Example usage:
sol = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
k = sol.removeDuplicates(nums)
print(f"Number of unique elements: {k}")
print(f"Array after removing duplicates: {nums[:k]}")
