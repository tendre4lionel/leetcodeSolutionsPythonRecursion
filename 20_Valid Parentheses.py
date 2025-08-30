class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        Recursive solution using a stack passed through recursion.
        """

        # Mapping of closing brackets to corresponding opening brackets
        mapping = {')': '(', '}': '{', ']': '['}

        def helper(index, stack):
            """
            Recursively checks the string from position 'index' using 'stack'.
            
            Args:
                index (int): current position in the string
                stack (list): stack of unmatched opening brackets

            Returns:
                bool: True if substring from index to end is valid
            """

            # Base case: reached end of string
            if index == len(s):
                # String is valid only if no unmatched brackets remain
                return len(stack) == 0

            char = s[index]

            if char in mapping:
                # Current char is a closing bracket
                if not stack or stack[-1] != mapping[char]:
                    # Either stack is empty (nothing to match) 
                    # or top of stack doesn't match current closing bracket
                    return False
                stack.pop()  # Pop matched opening bracket
                # Recurse to next character
                return helper(index + 1, stack)
            else:
                # Current char is an opening bracket
                stack.append(char)  # Push it onto stack
                # Recurse to next character
                return helper(index + 1, stack)

        # Start recursion from index 0 with an empty stack
        return helper(0, [])


# Example usage:
sol = Solution()
tests = ["()", "()[]{}", "(]", "([)]", "{[]}", ""]
for t in tests:
    print(f"{t}: {sol.isValid(t)}")
