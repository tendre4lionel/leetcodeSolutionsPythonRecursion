# 290 Word Pattern
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        Check if a string 's' follows the same pattern as 'pattern'.
        
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False

        def check(i, c2w={}, w2c={}):
            if i == len(pattern):
                return True

            c = pattern[i]
            w = words[i]

            # --- Explicit condition for letter -> word ---
            if c in c2w:
                # Letter is already mapped, check if it maps to the current word
                if c2w[c] != w:
                    return False
            else:
                # Letter not mapped yet, safe to map
                pass  # mapping will be added later

            # --- Explicit condition for word -> letter ---
            if w in w2c:
                # Word is already mapped, check if it maps to the current letter
                if w2c[w] != c:
                    return False
            else:
                # Word not mapped yet, safe to map
                pass  # mapping will be added later

            # Update mappings if they are not already present
            new_c2w = dict(c2w)
            if c not in c2w:
                new_c2w[c] = w

            new_w2c = dict(w2c)
            if w not in w2c:
                new_w2c[w] = c

            # Recurse to next index
            return check(i + 1, new_c2w, new_w2c)

        return check(0)
