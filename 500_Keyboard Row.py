# 500 Keyboard Row
1️⃣ Iterative Solution
Algorithm

Define sets for the 3 keyboard rows.

For each word in the input:

Convert to lowercase.

Create a set of unique characters.

Check if this set is a subset of any row.

If yes, keep the word.

Return collected words.

class Solution(object):
    def findWords_iterative(self, words):
        """
        Iterative approach.
        :type words: List[str]
        :rtype: List[str]
        """

        # Define rows as sets (fast membership checking)
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []  # store valid words

        # Process each word in the list
        for word in words:
            lower_word = word.lower()  # normalize to lowercase

            # Convert to set of unique letters
            letters = set(lower_word)

            # Check subset condition: all letters must be in one row
            if letters <= row1 or letters <= row2 or letters <= row3:
                result.append(word)  # keep original casing

        return result

2️⃣ Recursive with State (Memoization)
class Solution(object):
    def findWords_memoization(self, words):
        """
        Recursive with memoization approach.
        :type words: List[str]
        :rtype: List[str]
        """

        # Define keyboard rows
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        rows = [row1, row2, row3]

        memo = {}  # cache to avoid recomputation

        def canBeTyped(word, row):
            """
            Recursive helper: check if word fits entirely in row.
            """

            # Base case: if word is empty, success
            if word == "":
                return True

            # Take first character in lowercase
            first = word[0].lower()

            # If not in row, fail
            if first not in row:
                return False

            # Recurse on remainder of word
            return canBeTyped(word[1:], row)

        result = []

        # Check each word in words list
        for word in words:
            # Use memoized result if available
            if word in memo:
                if memo[word]:  # if true, keep word
                    result.append(word)
                continue

            # Otherwise compute by testing each row
            fits = False
            for row in rows:
                if canBeTyped(word, row):
                    fits = True
                    break

            memo[word] = fits  # store result in memo
            if fits:
                result.append(word)

        return result

3️⃣ Pure Recursion
class Solution(object):
    def findWords_recursive(self, words):
        """
        Pure recursive approach (no memoization).
        :type words: List[str]
        :rtype: List[str]
        """

        # Define the three keyboard rows
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        rows = [row1, row2, row3]

        def allInRow(word, row):
            """
            Recursively check if all characters in 'word' belong to 'row'.
            """

            # Base case: if no characters left, all checks passed
            if word == "":
                return True

            # Check first character
            first = word[0].lower()
            if first not in row:
                return False

            # Recurse on remainder of word
            return allInRow(word[1:], row)

        def helper(index):
            """
            Recursively process the list of words.
            """

            # Base case: processed all words
            if index == len(words):
                return []

            # Get current word
            word = words[index]

            # Check if word fits in any row
            valid = False
            for row in rows:
                if allInRow(word, row):
                    valid = True
                    break

            # Recurse for rest of words
            rest = helper(index + 1)

            # If valid, include current word
            return ([word] + rest) if valid else rest

        return helper(0)

