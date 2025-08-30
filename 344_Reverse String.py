# 344 Reverse String
class Solution(object):
    def reverseString(self, s):
        """
        Reverse the list of characters in-place using recursion.
        
        :type s: List[str]
        :rtype: None
        """
        # Recursive helper function
        def helper(left, right):
            # Base case: pointers crossed → stop recursion
            if left >= right:
                return
            
            # Swap characters at left and right
            s[left], s[right] = s[right], s[left]
            
            # Recurse for the next pair
            helper(left + 1, right - 1)
        
        # Start recursion from the ends of the array
        helper(0, len(s) - 1)


# Oneliner s.reverse()
# In Place s[:] = s[::-1]