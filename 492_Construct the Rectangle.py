# 492 Construct the Rectangle
🔹 Iterative Solution (with detailed comments)
import math

class Solution(object):
    def constructRectangle(self, area):
        """
        Iterative solution to construct rectangle dimensions.
        We want L >= W and L * W = area, with |L - W| minimized.
        """

        # Step 1: start with the integer square root of area
        # Why? Because the closest factors will be near sqrt(area)
        w = int(math.sqrt(area))

        # Step 2: decrease w until we find a divisor
        # If area % w == 0, then w is a valid width
        while area % w != 0:
            w -= 1  # move downward

        # Step 3: calculate length
        l = area // w

        # Step 4: return [L, W] ensuring L >= W
        return [l, w]


# Example usage
sol = Solution()
print(sol.constructRectangle(4))        # [2,2]
print(sol.constructRectangle(37))       # [37,1]
print(sol.constructRectangle(122122))   # [427,286]
"""
🔹 Recursive with Explicit State
import math

class Solution(object):
    def constructRectangle(self, area):
        """
        Recursive solution with explicit state.
        We simulate the while loop using recursion:
        - Base case: if w divides area, return [area//w, w].
        - Recursive case: try w-1.
        """

        def helper(w):
            # Base case: found a divisor
            if area % w == 0:
                return [area // w, w]

            # Recursive step: keep searching with smaller width
            return helper(w - 1)

        # Start recursion from sqrt(area)
        start = int(math.sqrt(area))
        return helper(start)


Pure Functional Recursion
import math

class Solution(object):
    def constructRectangle(self, area):
        """
        Pure functional recursion.
        Same as above but styled in a functional way:
        - The recursive function directly returns the result.
        - No external state variables are carried along.
        """

        def find_factor(w):
            # If w is a divisor, return immediately
            if area % w == 0:
                return [area // w, w]

            # Otherwise, check the next smaller width
            return find_factor(w - 1)

        # Start searching from sqrt(area)
        return find_factor(int(math.sqrt(area)))
"""
