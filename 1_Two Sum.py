class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        Recursive solution using a hashmap (dictionary).
        - Time Complexity: O(n) because each element is processed once.
        - Space Complexity: O(n) for storing seen elements in the hashmap.
        """

        def helper(i, seen):
            """
            :param i: current index we are processing
            :param seen: dictionary mapping "value -> index" 
                         for numbers we've already visited
            """

            # BASE CASE:
            # If we reach past the last index, 
            # it means no solution was found (shouldn't happen 
            # because the problem guarantees one solution).
            if i >= len(nums):
                return None  

            # Calculate what number we need to complete the target sum.
            complement = target - nums[i]

            # STEP 1: Check if the "complement" has been seen before.
            # If yes, then nums[i] + nums[seen[complement]] = target,
            # so we return those two indices.
            if complement in seen:
                return [seen[complement], i]

            # STEP 2: Otherwise, store the current number and its index
            # in the hashmap so it can be used by future recursive calls.
            seen[nums[i]] = i

            # STEP 3: Move recursively to the next index (i+1),
            # carrying along the updated hashmap.
            return helper(i + 1, seen)

        # Start recursion at index 0, with an empty hashmap.
        return helper(0, {})


# -------------------
# Example Run
# -------------------
nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))  
# Output: [0, 1] because nums[0] + nums[1] = 9
