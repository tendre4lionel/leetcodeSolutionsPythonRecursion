# 414 Third Maximum Number
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Recursive helper to remove duplicates
        def remove_duplicates(idx, seen):
            """
            idx: current index in nums
            seen: set of unique numbers collected
            """
            if idx == len(nums):
                return list(seen)
            seen.add(nums[idx])
            return remove_duplicates(idx + 1, seen)

        # Step 1: get unique numbers
        unique_nums = remove_duplicates(0, set())

        # Recursive helper to find max number
        def find_max(arr):
            if not arr:
                return float('-inf')
            head = arr[0]
            tail_max = find_max(arr[1:])
            return head if head > tail_max else tail_max

        # Step 2: find maximum
        first_max = find_max(unique_nums)

        # Step 3: remove first max and find second max
        unique_nums.remove(first_max)
        if unique_nums:
            second_max = find_max(unique_nums)
            unique_nums.remove(second_max)
        else:
            return first_max  # less than 2 distinct numbers

        # Step 4: find third max if exists
        if unique_nums:
            third_max = find_max(unique_nums)
            return third_max
        else:
            return first_max
