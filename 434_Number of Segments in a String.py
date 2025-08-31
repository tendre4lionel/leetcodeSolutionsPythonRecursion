# 434 Number of Segments in a String
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Recursive helper that also tracks previous character
        def helper(index, prev_char):
            # Base case: reached end of string
            if index == len(s):
                return 0

            # Current character
            curr = s[index]

            # Case 1: New segment starts
            if curr != " " and (prev_char == " " or prev_char is None):
                return 1 + helper(index + 1, curr)

            # Case 2: Not starting a new segment, just recurse
            return helper(index + 1, curr)

        # Start recursion with index 0 and no previous char
        return helper(0, None)


"""
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0  # keeps track of number of segments
        in_segment = False  # flag to check if we are currently inside a segment

        # iterate over each character in the string
        for char in s:
            if char != " ":
                # if we see a non-space and we are not already in a segment
                if not in_segment:
                    count += 1         # found the start of a new segment
                    in_segment = True  # mark that we are inside a segment
            else:
                # reset flag when we hit a space
                in_segment = False

        return count

"""