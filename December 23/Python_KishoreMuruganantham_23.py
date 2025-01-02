def crystal_grid_final_result(grid):
    n = len(grid)
    primary_sum, secondary_sum, boundary_sum = 0, 0, 0

    for i in range(n):
        primary_sum += grid[i][i]
        secondary_sum += grid[i][n - 1 - i]
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                boundary_sum += grid[i][j]

    diagonal_energy = abs(primary_sum - secondary_sum)
    final_result = diagonal_energy + boundary_sum
    return final_result

# Example Usage
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(crystal_grid_final_result(grid))  # Output: 40
