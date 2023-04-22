"""Task 15: Compulsory Task 1: Data Structures - 2D Lists
In this program, we are creating a function that takes a grid of # and -
Each hash (#) represents a mine and each dash (-) represents a mine-free spot."""

# In the function below we define the function to count adjacent mines for a given cell
# Using for loops to iterate through the neighbouring cells
# We use an if statement to check if the cells are within the grid boundaries and contains a mine
def minesweeper(grid):
    def count_adjacent_mines(row, col):
        count = 0
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (r, c) != (row, col) and 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '#':
                    count += 1
        return count

    # Here I iterate through the rows and columns of the grid using the enumerate function
    # Check for mines to add to the result row, and for mine-free cells, add the count of adjacent mines
    # All stored in results[]
    result = []
    for row, row_values in enumerate(grid):
        result_row = []
        for col, cell in enumerate(row_values):
            if cell == '#':
                result_row.append('#')
            else:
                result_row.append(str(count_adjacent_mines(row, col)))
        result.append(result_row)
    return result

# Here I have used the example input from the spreadsheet to validate my work
grid = [['-', '-', '-', '#', '#'],
        ['-', '#', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
        ['-', '#', '#', '-', '-'],
        ['-', '-', '-', '-', '-']]

result = minesweeper(grid)

# I have printed the results similar to the examples and looks visually better
for row_index, row in enumerate(result):
    print(f"Row {row_index} has {len(row)} columns: {'  '.join(row)}")
