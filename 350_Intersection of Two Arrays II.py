# 350 Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # Recursive helper function to find intersection
        def intersect_recursive(list1, list2, result):
            # Base case: if either list is empty, return the accumulated result
            if not list1 or not list2:
                return result
            
            # Take the first element of list1
            first = list1[0]
            
            # Check if this element exists in list2
            if first in list2:
                # If yes, add it to the result
                result.append(first)
                
                # Remove the first occurrence from list2 to avoid duplicates
                list2.remove(first)
            
            # Recursively call the function with the rest of list1
            # The result accumulates in the 'result' list
            return intersect_recursive(list1[1:], list2, result)

        # Start the recursion with an empty result list
        return intersect_recursive(nums1, nums2, [])

# Example usage
solution = Solution()
print(solution.intersect([1,2,2,1], [2,2]))  # Output: [2,2]
print(solution.intersect([4,9,5], [9,4,9,8,4]))  # Output: [4,9] or [9,4]
