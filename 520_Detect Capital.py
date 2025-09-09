# 520 Detect Capital
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # Algorithm (Iterative):
        # 1. Check if all characters are uppercase.
        # 2. Or check if all characters are lowercase.
        # 3. Or check if only the first character is uppercase and rest lowercase.
        # 4. Return True if any condition holds, otherwise False.
        #
        # Time Complexity: O(n), scanning the string
        # Space Complexity: O(1), constant extra memory

        if word.isupper():   # all capitals
            return True
        if word.islower():   # all lowercase
            return True
        if word[0].isupper() and word[1:].islower():  # first capital only
            return True
        return False



class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # Algorithm (Recursive with state):
        # 1. Determine the "pattern" to check based on first letters:
        #    - If first is uppercase and second is uppercase -> expect all uppercase.
        #    - If first is uppercase and second is lowercase -> expect title case.
        #    - If first is lowercase -> expect all lowercase.
        # 2. Use recursion to check each character against the expected pattern.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(n) recursion depth

        n = len(word)
        if n <= 1:
            return True

        # Decide expected pattern
        if word[0].isupper() and n > 1 and word[1].isupper():
            pattern = "all_upper"
        elif word[0].isupper():
            pattern = "title"
        else:
            pattern = "all_lower"

        def helper(i):
            if i == n:
                return True
            if pattern == "all_upper" and not word[i].isupper():
                return False
            if pattern == "all_lower" and not word[i].islower():
                return False
            if pattern == "title" and i > 0 and not word[i].islower():
                return False
            return helper(i + 1)

        return helper(1)





class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # Algorithm (Pure recursion):
        # 1. Directly test the three valid patterns:
        #    - all uppercase
        #    - all lowercase
        #    - first uppercase + rest lowercase
        # 2. Implement each test recursively.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(n) recursion depth

        def all_upper(s, i):
            if i == len(s):
                return True
            return s[i].isupper() and all_upper(s, i + 1)

        def all_lower(s, i):
            if i == len(s):
                return True
            return s[i].islower() and all_lower(s, i + 1)

        def title_case(s, i):
            if i == len(s):
                return True
            if i == 0:
                return s[i].isupper() and title_case(s, i + 1)
            return s[i].islower() and title_case(s, i + 1)

        return all_upper(word, 0) or all_lower(word, 0) or title_case(word, 0)















