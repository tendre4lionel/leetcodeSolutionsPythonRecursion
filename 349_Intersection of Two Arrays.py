# 349 Intersection of Two Arrays
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        Find the intersection of two arrays (unique elements only).
        
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # Convert both lists into sets (removes duplicates automatically)
        set1 = set(nums1)
        set2 = set(nums2)

        # Intersection of sets gives the common unique elements
        result = set1 & set2   # or set1.intersection(set2)

        # Convert the set back into a list
        return list(result)


"""
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        Find the intersection of two arrays using recursion.
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # Recursive helper function
        def helper(index, result):
            # Base case: all elements of nums1 processed
            if index == len(nums1):
                return result

            num = nums1[index]

            # If num is in nums2 and not already in result, add it
            if num in nums2 and num not in result:
                result.append(num)

            # Recurse on the next index
            return helper(index + 1, result)

        # Start recursion from index 0 with empty result
        return helper(0, [])

"""