# 563 Binary Tree Tilt
# Algorithm:
# - Check if reshape is possible (total elements must match)
# - Flatten the original matrix into a list
# - Fill new r x c matrix row by row using elements from flattened list
# Complexity:
# - Time: O(m * n)
# - Space: O(m * n)

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        
        # Check if reshape is possible
        if m * n != r * c:
            return mat
        
        # Flatten the original matrix
        flat = []
        for row in mat:
            for val in row:
                flat.append(val)
        
        # Build the reshaped matrix
        reshaped = []
        for i in range(r):
            reshaped.append(flat[i*c:(i+1)*c])
        
        return reshaped

# Example usage:
# sol = Solution()
# print(sol.matrixReshape([[1,2],[3,4]], 1, 4))  # Output: [[1,2,3,4]]


# Algorithm:
# - Flatten the matrix recursively while tracking current index
# - Rebuild reshaped matrix recursively by picking c elements for each row
# Complexity:
# - Time: O(m * n)
# - Space: O(m * n) for recursion stack + flattened list

class Solution(object):
    def matrixReshape(self, mat, r, c, flat=None, index=0):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if flat is None:
            # Flatten original matrix recursively
            flat = [val for row in mat for val in row]
            if len(flat) != r * c:
                return mat  # cannot reshape
        
        # Base case: no rows left to build
        if index >= r:
            return []
        
        # Build current row
        row = flat[index*c:(index+1)*c]
        # Recurse for remaining rows
        return [row] + self.matrixReshape(mat, r, c, flat, index+1)

# Example usage:
# sol = Solution()
# print(sol.matrixReshape([[1,2],[3,4]], 1, 4))  # Output: [[1,2,3,4]]

# Algorithm:
# - Flatten matrix using list comprehension
# - Recursively build each row using slicing
# Complexity:
# - Time: O(m * n)
# - Space: O(m * n) recursion stack + flattened list

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        flat = [val for row in mat for val in row]
        if len(flat) != r * c:
            return mat
        
        if r == 0:
            return []
        
        return [flat[:c]] + self.matrixReshape([flat[c:]], r-1, c)

# Example usage:
# sol = Solution()
# print(sol.matrixReshape([[1,2],[3,4]], 1, 4))  # Output: [[1,2,3,4]]


