class Solution(object):
    def summaryRanges(self, nums):
        """
        Fully recursive solution without f-strings or loops.
        """

        # Helper function to process ranges recursively
        def helper(index, result):
            # Base case: if index is beyond last element
            if index >= len(nums):
                return result

            start = nums[index]
            end = start

            # Recursive function to extend current consecutive range
            def extend_range(i, current_end):
                # Stop if next index is beyond array
                if i + 1 >= len(nums):
                    return current_end, i + 1
                # If next number is consecutive, extend range
                if nums[i + 1] == current_end + 1:
                    return extend_range(i + 1, nums[i + 1])
                # Otherwise, return current end and next index
                return current_end, i + 1

            # Get the end of current range and next start index
            end, next_index = extend_range(index, start)

            # Format the range using classic string formatting
            if start == end:
                range_str = "{}".format(start)
            else:
                range_str = "{}->{}".format(start, end)

            # Append current range to result
            result.append(range_str)

            # Recurse on next index
            return helper(next_index, result)

        # Start recursion with index 0 and empty list
        return helper(0, [])


# ---------------- Example Usage ----------------
sol = Solution()
nums = [0,1,2,4,5,7]
print(sol.summaryRanges(nums))  # Output: ["0->2","4->5","7"]

nums = [0,2,3,4,6,8,9]
print(sol.summaryRanges(nums))  # Output: ["0","2->4","6","8->9"]
