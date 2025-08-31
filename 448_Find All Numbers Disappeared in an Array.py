# 448 Find All Numbers Disappeared in an Array
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def mark(i):
            # Base case: when i reaches the end of the list
            if i == len(nums):
                return

            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

            # Recurse for next index
            mark(i + 1)

        # Step 1: recursively mark numbers
        mark(0)

        # Step 2: collect missing numbers
        def collect(i, result):
            if i == len(nums):
                return result

            if nums[i] > 0:
                result.append(i + 1)

            return collect(i + 1, result)

        return collect(0, [])



"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Step 1: Mark seen numbers
        for num in nums:
            index = abs(num) - 1  # map number to index
            if nums[index] > 0:   # only negate once
                nums[index] = -nums[index]

        # Step 2: Collect missing numbers (indices still positive)
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)  # convert index back to number

        return result

"""