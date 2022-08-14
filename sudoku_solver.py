def display_puzzle(puzzle):
    for row in puzzle:
        row = list(map(lambda x: ' ' if x==0 else x, row))
        print(row)

# return true if guess can go in row else return false
def possible_in_row(puzzle, row_index, guess):

    for num in puzzle[row_index]:

        if num == guess:
            return False

    return True

# return true if guess can go in column else return false
def possible_in_column(puzzle, column_index, guess):

    for row in puzzle:

        if row[column_index] == guess:
            return False

    return True

# return true if guess can go in square else return false
def possible_in_square(puzzle, x, y, guess):
    top_left_x = (x // 3) * 3
    top_left_y = (y // 3) * 3

    for y in range(top_left_y, top_left_y+3):
        for x in range(top_left_x, top_left_x+3):
            if puzzle[y][x] == guess:
                return False
    
    return True

def possible(puzzle, x, y, guess):

    if not possible_in_column(puzzle, x, guess):
        return False
    
    if not possible_in_row(puzzle, y, guess):
        return False
    
    if not possible_in_square(puzzle, x, y, guess):
        return False

    return True


def solve_puzzle(puzzle):
    for y in range(len(puzzle)):
        for x in range(len(puzzle[y])):
            if puzzle[y][x] == 0:
                for guess in range(1,10):
                    if possible(puzzle, x, y, guess):
                        puzzle[y][x] = guess
                        solve_puzzle(puzzle)
                        puzzle[y][x] = 0

                return puzzle
    display_puzzle(puzzle)
    print()
    