# 507 Perfect Number
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Algorithm (Iterative):
        # 1. Handle edge cases: numbers <= 1 are not perfect.
        # 2. Iterate from 1 up to sqrt(num), check divisors.
        # 3. Add both divisor and quotient (if distinct).
        # 4. Subtract num itself from the sum.
        # 5. Compare sum with num.
        #
        # Time Complexity: O(sqrt(n))
        # Space Complexity: O(1)

        if num <= 1:
            return False

        total = 1  # 1 is always a divisor
        i = 2
        while i * i <= num:
            if num % i == 0:
                total += i
                if i != num // i:  # avoid double counting sqrt
                    total += num // i
            i += 1

        return total == num


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Algorithm (Recursive with state):
        # 1. Handle num <= 1 → False.
        # 2. Use recursion from divisor=2 to sqrt(num).
        # 3. Track total sum in a shared variable.
        # 4. Add divisors when found.
        # 5. Return whether total == num.
        #
        # Time Complexity: O(sqrt(n))
        # Space Complexity: O(sqrt(n)) recursion depth.

        if num <= 1:
            return False

        total = [1]  # use list as mutable state

        def helper(d):
            if d * d > num:
                return
            if num % d == 0:
                total[0] += d
                if d != num // d:
                    total[0] += num // d
            helper(d + 1)

        helper(2)
        return total[0] == num


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Algorithm (Pure recursion):
        # 1. Handle num <= 1 → False.
        # 2. Define recursive function that returns sum of divisors from d..sqrt(num).
        # 3. Combine sums using return values (no external state).
        # 4. At the end, check if sum == num.
        #
        # Time Complexity: O(sqrt(n))
        # Space Complexity: O(sqrt(n)) recursion depth.

        if num <= 1:
            return False

        def helper(d):
            if d * d > num:
                return 0
            if num % d == 0:
                # count divisor and its pair (if not same)
                if d != num // d:
                    return d + (num // d) + helper(d + 1)
                else:
                    return d + helper(d + 1)
            return helper(d + 1)

        total = 1 + helper(2)  # include divisor 1
        return total == num













