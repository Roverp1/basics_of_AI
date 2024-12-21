import random
import numpy as np
import math
from random import choice
import statistics

# Initial Sudoku board as a string
starting_sudoku = """
                    024007000
                    600000000
                    003680415
                    431005000
                    500000032
                    790000060
                    209710800
                    040093000
                    310004750
                """

# Convert the Sudoku board to a numpy array
sudoku = np.array([[int(i) for i in line] for line in starting_sudoku.split()])


def print_sudoku(sudoku):
    """Prints the Sudoku board in a readable format."""
    print("\n")
    for i in range(len(sudoku)):
        line = ""
        if i % 3 == 0 and i != 0:
            print("---------------------")
        for j in range(len(sudoku[i])):
            if j % 3 == 0 and j != 0:
                line += "| "
            line += str(sudoku[i, j]) + " "
        print(line)


def mark_fixed_cells(sudoku):
    """Marks cells with fixed values as 1, others as 0."""
    fixed_cells = np.copy(sudoku)
    fixed_cells[fixed_cells != 0] = 1
    return fixed_cells


def calculate_total_errors(sudoku):
    """Calculates the total number of errors in the Sudoku board."""
    total_errors = 0
    for i in range(9):
        total_errors += calculate_row_column_errors(i, i, sudoku)
    return total_errors


def calculate_row_column_errors(row, column, sudoku):
    """Calculates the number of errors in a row and column."""
    row_errors = 9 - len(np.unique(sudoku[row, :]))
    col_errors = 9 - len(np.unique(sudoku[:, column]))
    return row_errors + col_errors


def create_block_indices():
    """Creates a list of indices for all 3x3 blocks."""
    blocks = []
    for block_idx in range(9):
        block_rows = [i + 3 * (block_idx % 3) for i in range(3)]
        block_cols = [i + 3 * (block_idx // 3) for i in range(3)]
        block = [[r, c] for r in block_rows for c in block_cols]
        blocks.append(block)
    return blocks


def fill_blocks_randomly(sudoku, block_indices):
    """Randomly fills empty cells in each 3x3 block while ensuring uniqueness."""
    for block in block_indices:
        for cell in block:
            if sudoku[cell[0], cell[1]] == 0:
                block_values = sudoku[block[0][0]:block[-1][0]+1, block[0][1]:block[-1][1]+1]
                sudoku[cell[0], cell[1]] = choice([i for i in range(1, 10) if i not in block_values])
    return sudoku


def calculate_block_sum(sudoku, block):
    """Calculates the sum of values in a 3x3 block."""
    return sum(sudoku[cell[0], cell[1]] for cell in block)


def select_two_random_cells(fixed_cells, block):
    """Selects two random non-fixed cells within a block."""
    while True:
        first_cell = random.choice(block)
        second_cell = choice([cell for cell in block if cell != first_cell])
        if fixed_cells[first_cell[0], first_cell[1]] == 0 and fixed_cells[second_cell[0], second_cell[1]] == 0:
            return [first_cell, second_cell]


def swap_cells(sudoku, cells_to_swap):
    """Swaps the values of two cells."""
    proposed_sudoku = np.copy(sudoku)
    temp = proposed_sudoku[cells_to_swap[0][0], cells_to_swap[0][1]]
    proposed_sudoku[cells_to_swap[0][0], cells_to_swap[0][1]] = proposed_sudoku[cells_to_swap[1][0], cells_to_swap[1][1]]
    proposed_sudoku[cells_to_swap[1][0], cells_to_swap[1][1]] = temp
    return proposed_sudoku


def generate_new_state(sudoku, fixed_cells, block_indices):
    """Generates a new Sudoku state by swapping two random cells in a random block."""
    random_block = random.choice(block_indices)

    # Skip blocks with mostly fixed cells
    if calculate_block_sum(fixed_cells, random_block) > 6:
        return sudoku, 1, 1

    cells_to_swap = select_two_random_cells(fixed_cells, random_block)
    new_sudoku = swap_cells(sudoku, cells_to_swap)
    return new_sudoku, cells_to_swap


def accept_new_state(current_sudoku, fixed_cells, block_indices, temperature):
    """Determines whether to accept a new state based on the simulated annealing algorithm."""
    proposed_sudoku, swapped_cells = generate_new_state(current_sudoku, fixed_cells, block_indices)
    current_cost = calculate_row_column_errors(swapped_cells[0][0], swapped_cells[0][1], current_sudoku) + \
                   calculate_row_column_errors(swapped_cells[1][0], swapped_cells[1][1], current_sudoku)
    new_cost = calculate_row_column_errors(swapped_cells[0][0], swapped_cells[0][1], proposed_sudoku) + \
               calculate_row_column_errors(swapped_cells[1][0], swapped_cells[1][1], proposed_sudoku)

    cost_difference = new_cost - current_cost
    acceptance_probability = math.exp(-cost_difference / temperature)

    if random.uniform(0, 1) < acceptance_probability:
        return proposed_sudoku, cost_difference
    return current_sudoku, 0


def calculate_initial_temperature(sudoku, fixed_cells, block_indices):
    """Calculates the initial temperature for simulated annealing."""
    cost_differences = []
    temp_sudoku = sudoku
    for _ in range(10):
        temp_sudoku, _ = generate_new_state(temp_sudoku, fixed_cells, block_indices)
        cost_differences.append(calculate_total_errors(temp_sudoku))
    return statistics.pstdev(cost_differences)


def solve_sudoku(sudoku):
    """Solves the Sudoku using a simulated annealing approach."""
    solution_found = False

    while not solution_found:
        cooling_rate = 0.99
        stuck_counter = 0

        fixed_cells = mark_fixed_cells(sudoku)
        block_indices = create_block_indices()
        temp_sudoku = fill_blocks_randomly(sudoku, block_indices)
        temperature = calculate_initial_temperature(sudoku, fixed_cells, block_indices)
        current_score = calculate_total_errors(temp_sudoku)

        if current_score == 0:
            solution_found = True

        while not solution_found:
            previous_score = current_score

            for _ in range(np.sum(fixed_cells == 0)):
                temp_sudoku, score_change = accept_new_state(temp_sudoku, fixed_cells, block_indices, temperature)
                current_score += score_change
                print(f"Current Errors: {current_score}")  # Printing the number of errors at each iteration

                if current_score == 0:
                    solution_found = True
                    break

            temperature *= cooling_rate

            if current_score == 0:
                solution_found = True
                break

            if current_score >= previous_score:
                stuck_counter += 1
            else:
                stuck_counter = 0

            if stuck_counter > 80:
                temperature += 2

    return temp_sudoku


# Solve the Sudoku
solution = solve_sudoku(sudoku)
print("Final Errors:", calculate_total_errors(solution))
print_sudoku(solution)
