# 412 Fizz Buzz
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        # Recursive helper function
        def helper(i):
            # Base case: all numbers processed
            if i > n:
                return

            # Determine Fizz/Buzz/FizzBuzz
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

            # Recurse for next number
            helper(i + 1)

        # Start recursion from 1
        helper(1)

        return result
