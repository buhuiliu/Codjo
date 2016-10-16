"""
dfs.py
------
https://www.hackerrank.com/challenges/connected-cell-in-a-grid
Ana, Leo and Lin
09/22/16
"""

def get_neighbors(i, j, num_rows, num_cols):
    """Returns a list of matrix indices neighboring (i, j)."""
    x_values = [i - 1, i, i + 1]
    y_values = [j - 1, j, j + 1]
    return [(x, y) for x in x_values for y in y_values if x >= 0 and x < num_rows and y >= 0 and y < num_cols and (x != i or y != j)]


def DFS(matrix, i, j, visited):
    """Perform DFS in matrix from the i,j cell, after having seen the cells in
    visited.
    Return a list of matrix indices that belong in the region.
    """
    value = matrix[i][j]
    if not value:
        return visited

    visited.append((i, j))

    for node in get_neighbors(i, j, len(matrix), len(matrix[0])):
        if node not in visited:
            #print('   following {},{}'.format(node[0], node[1]))
            # search modifies visited!
            DFS(matrix, node[0], node[1], visited)

    return visited


def largest_region():
    """Read the matrix, perform DFS, output the size of largest region."""
    # Read the matrix
    num_rows = int(raw_input())
    num_cols = int(raw_input())

    matrix = [[0] * num_cols for _ in range(num_rows)]
    for i in range(num_rows):
        matrix[i] = [int(s) for s in raw_input().split(' ')]

    # Perform DFS
    region_sizes = []
    regions = []
    for i in range(1, num_rows):
        for j in range(1, num_cols):
            if not (i, j) in regions:
                #print('Starting at {},{}'.format(i, j))
                region = DFS(matrix, i, j, [])
                regions.append(region)
                region_sizes.append(len(region))

    # Output the size of largest region
    return max(region_sizes)

if __name__ == '__main__':
    print largest_region()
