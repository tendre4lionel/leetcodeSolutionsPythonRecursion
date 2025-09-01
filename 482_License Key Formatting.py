# 482 License Key Formatting

class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        Fully recursive slicing solution.
        :type s: str
        :type k: int
        :rtype: str
        """

        # Remove dashes and convert to uppercase
        cleaned = s.replace("-", "").upper()

        # Base case: if cleaned string is empty
        if not cleaned:
            return ""

        # Length of the first group
        first_group_len = len(cleaned) % k or k

        # First group is the leftmost substring
        first_group = cleaned[:first_group_len]

        # Recursive function to process remaining groups
        def build_groups(start):
            # Base case: if we've reached the end
            if start >= len(cleaned):
                return ""

            # Current group of size k
            group = cleaned[start:start + k]

            # Recursively build the next groups
            rest = build_groups(start + k)

            # If rest is empty, just return group
            if not rest:
                return group

            # Otherwise, attach dash and rest
            return group + "-" + rest

        # Combine first group with recursive result
        rest = build_groups(first_group_len)
        if rest:
            return first_group + "-" + rest
        return first_group


# Example usage
sol = Solution()
print(sol.licenseKeyFormatting("5F3Z-2e-9-w", 4))   # "5F3Z-2E9W"
print(sol.licenseKeyFormatting("2-5g-3-J", 2))      # "2-5G-3J"
print(sol.licenseKeyFormatting("--a-a-a-a--", 2))  # "AA-AA"


"""
class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        Iteratively reformat the license key.
        :type s: str
        :type k: int
        :rtype: str
        """

        # Remove all dashes and convert to uppercase
        cleaned = s.replace("-", "").upper()

        result = []  # To build the reformatted string
        count = 0    # Counter for characters in the current group

        # Process the string from end to start
        for char in reversed(cleaned):
            result.append(char)
            count += 1

            # If we have reached k characters, insert a dash for the next group
            if count == k:
                result.append("-")
                count = 0

        # If the last character added is a dash, remove it
        if result and result[-1] == "-":
            result.pop()

        # Reverse the list to get the correct order and join to string
        return "".join(reversed(result))


# Example usage
sol = Solution()
print(sol.licenseKeyFormatting("5F3Z-2e-9-w", 4))   # "5F3Z-2E9W"
print(sol.licenseKeyFormatting("2-5g-3-J", 2))      # "2-5G-3J"
print(sol.licenseKeyFormatting("--a-a-a-a--", 2))  # "AA-AA"
"""

"""
class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        Optimized iterative reformatting using slicing.
        :type s: str
        :type k: int
        :rtype: str
        """

        # Remove dashes and convert to uppercase
        cleaned = s.replace("-", "").upper()

        # Find the length of the first group
        first_group_len = len(cleaned) % k or k

        # Start with the first group
        groups = [cleaned[:first_group_len]]

        # Add the remaining groups of size k
        for i in range(first_group_len, len(cleaned), k):
            groups.append(cleaned[i:i+k])

        # Join all groups with dashes
        return "-".join(groups)


# Example usage
sol = Solution()
print(sol.licenseKeyFormatting("5F3Z-2e-9-w", 4))   # "5F3Z-2E9W"
print(sol.licenseKeyFormatting("2-5g-3-J", 2))      # "2-5G-3J"
print(sol.licenseKeyFormatting("--a-a-a-a--", 2))  # "AA-AA"
"""




