# 88 Merge Sorted Array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Merge two sorted arrays nums1 and nums2 into nums1 in-place.

        Approach (Recursive):
        --------------------
        - We will fill nums1 from the **end** to avoid overwriting elements.
        - Keep three pointers:
            i = last valid element in nums1 (m-1)
            j = last element in nums2 (n-1)
            k = last position in nums1 (m+n-1)
        - At each step:
            1. Compare nums1[i] and nums2[j]
            2. Place the larger one at nums1[k]
            3. Recurse by moving the corresponding pointer(s)
        - Base case: if nums2 is exhausted (j < 0), stop
                     if nums1 is exhausted (i < 0), copy remaining nums2
        """

        def helper(i, j, k):
            # Base case: if nums2 is exhausted, we are done
            if j < 0:
                return

            # Base case: if nums1 is exhausted, copy remaining nums2 elements
            if i < 0:
                nums1[:j+1] = nums2[:j+1]
                return

            # Recursive case: compare last elements of current slices
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                helper(i-1, j, k-1)
            else:
                nums1[k] = nums2[j]
                helper(i, j-1, k-1)

        # Start recursion from the last valid elements
        helper(m-1, n-1, m+n-1)


# ---------------- Example Usage ----------------
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

sol = Solution()
sol.merge(nums1, m, nums2, n)
print(nums1)  # Output: [1,2,2,3,5,6]
