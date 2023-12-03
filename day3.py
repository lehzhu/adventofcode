def sum_part_numbers(grid):
    def is_symbol(char):
        return char in "*#$+"

    def get_number_at(grid, x, y):
        # Check if the current cell is a digit and continue until a non-digit is found
        if not grid[y][x].isdigit():
            return 0, 0
        
        number = ""
        original_x = x
        while x < len(grid[0]) and grid[y][x].isdigit():
            number += grid[y][x]
            x += 1
        
        return int(number), x - original_x

    def is_adjacent_to_symbol(grid, x, y, length):
        # Check adjacent cells for symbols
        for i in range(length):
            if (x + i < len(grid[0]) - 1 and is_symbol(grid[y][x + i + 1])) or \
               (x + i > 0 and is_symbol(grid[y][x + i - 1])) or \
               (y < len(grid) - 1 and is_symbol(grid[y + 1][x + i])) or \
               (y > 0 and is_symbol(grid[y - 1][x + i])):
                return True
        return False

    total = 0

    # Iterate over each cell in the grid
    for y in range(len(grid)):
        x = 0
        while x < len(grid[0]):
            number, length = get_number_at(grid, x, y)
            if number > 0 and is_adjacent_to_symbol(grid, x, y, length):
                total += number
            x += length or 1

    return total

# Example grid from the problem statement
grid_example = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

sum_part_numbers(grid_example)
