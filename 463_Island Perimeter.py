# 463 Island Perimeter
class Solution(object):
    def islandPerimeter(self, grid):
        """
        Calculate the perimeter of the island using an iterative approach.
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        # Iterate over every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # Only consider land cells
                if grid[r][c] == 1:
                    # Start with 4 sides for each land cell
                    cell_perimeter = 4

                    # Check each neighbor: if neighbor is land, subtract 1 for shared edge
                    if r > 0 and grid[r-1][c] == 1:  # Up
                        cell_perimeter -= 1
                    if r < rows - 1 and grid[r+1][c] == 1:  # Down
                        cell_perimeter -= 1
                    if c > 0 and grid[r][c-1] == 1:  # Left
                        cell_perimeter -= 1
                    if c < cols - 1 and grid[r][c+1] == 1:  # Right
                        cell_perimeter -= 1

                    # Add this cell's contribution to total perimeter
                    perimeter += cell_perimeter

        return perimeter


# Example usage
sol = Solution()
grid1 = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
]
print(sol.islandPerimeter(grid1))  # Output: 16


"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        Calculate the perimeter of the island by counting land cells and shared edges.
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        land_cells = 0   # Total number of land cells
        shared_edges = 0 # Number of edges shared between adjacent land cells

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    land_cells += 1

                    # Check up neighbor
                    if r > 0 and grid[r-1][c] == 1:
                        shared_edges += 1
                    # Check left neighbor
                    if c > 0 and grid[r][c-1] == 1:
                        shared_edges += 1

        # Each land cell contributes 4 sides, but each shared edge reduces perimeter by 2
        perimeter = 4 * land_cells - 2 * shared_edges
        return perimeter


# Example usage
sol = Solution()
grid1 = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
]
print(sol.islandPerimeter(grid1))  # Output: 16

"""