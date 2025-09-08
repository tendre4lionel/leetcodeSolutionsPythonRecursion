# 496 Next Greater Element I
1️⃣ Iterative Solution (with detailed comments)
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        Iterative approach using a stack to compute next greater elements.
        Time Complexity: O(n + m), n = len(nums2), m = len(nums1)
        Space Complexity: O(n) for stack + hashmap
        """
        next_greater = {}  # Dictionary to store the next greater element for each number in nums2
        stack = []  # Stack to keep numbers for which we haven't found the next greater element yet

        # Loop through each number in nums2
        for num in nums2:
            # While stack is not empty and current number is greater than the top of the stack
            while stack and stack[-1] < num:
                smaller = stack.pop()  # Pop the smaller number
                next_greater[smaller] = num  # The current number is the next greater for the popped number
            # Push current number onto the stack to find its next greater later
            stack.append(num)

        # Any remaining numbers in stack do not have a next greater element
        while stack:
            smaller = stack.pop()
            next_greater[smaller] = -1  # No greater element found

        # Build the result for nums1 using the next_greater dictionary
        result = []
        for num in nums1:
            # For each number in nums1, get its next greater from the dictionary
            result.append(next_greater[num])
        return result

# Example
sol = Solution()
print(sol.nextGreaterElement([4,1,2], [1,3,4,2]))  # Output: [-1, 3, -1]

2️⃣ Recursive with State (Stack + Memo, detailed comments)
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        Recursive approach using a stack to keep track of numbers without a next greater element.
        Time Complexity: O(n + m)
        Space Complexity: O(n) for stack + recursion
        """
        next_greater = {}  # Dictionary to store next greater elements
        stack = []  # Stack to maintain numbers awaiting a greater number

        def helper(index):
            """
            Recursive helper function to process nums2.
            index: current index in nums2
            """
            if index == len(nums2):
                # Base case: reached end of nums2
                # Any remaining numbers in stack have no next greater element
                while stack:
                    next_greater[stack.pop()] = -1
                return

            num = nums2[index]  # Current number in nums2

            # Resolve all numbers in stack smaller than current number
            while stack and stack[-1] < num:
                smaller = stack.pop()
                next_greater[smaller] = num  # Current number is next greater for smaller

            # Push current number to stack to find its next greater later
            stack.append(num)

            # Recurse to the next index
            helper(index + 1)

        # Start recursion from the first index
        helper(0)

        # Build result for nums1 using precomputed next_greater dictionary
        return [next_greater[num] for num in nums1]

# Example
sol = Solution()
print(sol.nextGreaterElement([4,1,2], [1,3,4,2]))  # Output: [-1, 3, -1]

3️⃣ Pure Recursion (Brute Force, detailed comments)
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        Pure recursive approach.
        Time Complexity: O(m * n), m = len(nums1), n = len(nums2)
        Space Complexity: O(n) for recursion depth
        """

        def find_next(index, target):
            """
            Recursive function to find next greater element for target in nums2 starting at index.
            index: current index in nums2
            target: number from nums1 for which we are finding next greater
            """
            if index == len(nums2):
                # Base case: reached the end, no greater element
                return -1
            if nums2[index] > target:
                # Found the next greater element
                return nums2[index]
            # Recurse to the next index
            return find_next(index + 1, target)

        result = []
        for num in nums1:
            # Find the index of num in nums2
            start_index = nums2.index(num) + 1  # Start searching to the right
            # Append the result of recursive search
            result.append(find_next(start_index, num))

        return result

# Example
sol = Solution()
print(sol.nextGreaterElement([4,1,2], [1,3,4,2]))  # Output: [-1, 3, -1]
