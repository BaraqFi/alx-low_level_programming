#!usr/bin/python3

def islamd_perimeter(grid):
"""
Returns the perimeter of the island described in the given grid

Args:
grid (list of list of int): a rectangular grid of 0's and 1's, where 0 represents water and 1 represents land

Returns:
int: the perimeter of the island

Raises:
None
"""

if not grid:
    return 0

perimeter = 0
rows = len(grid)
cols = len(grid[0])

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1:
            # check top
            if i == 0 or grid[i-1][j] == 0:
                perimeter += 1
            # check left
            if j == 0 or grid[i][j-1] == 0:
                perimeter += 1
            # check bottom
            if i == rows-1 or grid[i+1][j] == 0:
                perimeter += 1
            # check right
            if j == cols-1 or grid[i][j+1] == 0:
                perimeter += 1

return perimeter
