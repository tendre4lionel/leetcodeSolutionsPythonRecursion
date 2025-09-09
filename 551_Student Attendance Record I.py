# 551 Student Attendance Record I
# Algorithm:
# - Traverse the string once
# - Count total 'A's and track consecutive 'L's
# - Return False immediately if any rule is violated
# Complexity:
# - Time: O(n), n = length of string
# - Space: O(1)

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absents = 0
        consecutive_lates = 0
        
        for ch in s:
            if ch == 'A':
                absents += 1
                if absents >= 2:
                    return False
                consecutive_lates = 0  # reset consecutive lates
            elif ch == 'L':
                consecutive_lates += 1
                if consecutive_lates >= 3:
                    return False
            else:  # 'P'
                consecutive_lates = 0
        
        return True

# Example usage:
# sol = Solution()
# print(sol.checkRecord("PPALLP"))  # True
# print(sol.checkRecord("PPALLL"))  # False



# Algorithm:
# - Use recursion to track index, total absents, and consecutive lates
# - Base case: if index reaches end of string, return True
# - Return False immediately if rules are violated
# Complexity:
# - Time: O(n)
# - Space: O(n) recursion stack

class Solution(object):
    def checkRecord(self, s, index=0, absents=0, cons_lates=0):
        """
        :type s: str
        :rtype: bool
        """
        if index == len(s):
            return True
        
        ch = s[index]
        
        if ch == 'A':
            absents += 1
            cons_lates = 0
            if absents >= 2:
                return False
        elif ch == 'L':
            cons_lates += 1
            if cons_lates >= 3:
                return False
        else:
            cons_lates = 0
        
        return self.checkRecord(s, index + 1, absents, cons_lates)

# Example usage:
# sol = Solution()
# print(sol.checkRecord("PPALLP"))  # True
# print(sol.checkRecord("PPALLL"))  # False


# Algorithm:
# - Slice string and process first character at each recursion
# - Check conditions for current character
# - Recurse on remaining string
# Complexity:
# - Time: O(n)
# - Space: O(n) recursion stack

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        if s[0] == 'A':
            # Count total 'A' in the string
            if s.count('A') >= 2:
                return False
        # Check for three consecutive 'L's anywhere
        if 'LLL' in s:
            return False
        
        return True

# Example usage:
# sol = Solution()
# print(sol.checkRecord("PPALLP"))  # True
# print(sol.checkRecord("PPALLL"))  # False







