# 205 Isomorphic Strings
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def helper(i):
            # Base case: reached the end of strings
            if i == len(s):
                return True
            
            # Compare first occurrence indices
            if s.index(s[i]) != t.index(t[i]):
                return False
            
            # Recurse to next character
            return helper(i + 1)
        
        return helper(0)


"""
def isIsomorphic(s, t):
    return [s.index(c) for c in s] == [t.index(c) for c in t]

"""