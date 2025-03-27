import math
import heapq


# Define the Cell class representing each cell in the grid
class Cell:
    def __init__(self):
        self.parent_row = 0  # Parent cell's row index
        self.parent_col = 0  # Parent cell's column index
        self.f_cost = float("inf")  # Total cost of the cell (g_cost + h_cost)
        self.g_cost = float("inf")  # Cost from start to this cell
        self.h_cost = 0  # Heuristic cost from this cell to destination


# Define the size of the grid
GRID_ROWS = 9
GRID_COLS = 10


# Check if a cell is within the grid boundaries
def is_valid_cell(row, col):
    return 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS


# Check if a cell is not blocked
def is_cell_unblocked(grid, row, col):
    return grid[row][col] == 1


# Check if a cell is the destination
def is_cell_destination(row, col, destination):
    return row == destination[0] and col == destination[1]


# Calculate the heuristic value (Euclidean distance to destination)
def calculate_heuristic(row, col, destination):
    return math.sqrt((row - destination[0]) ** 2 + (col - destination[1]) ** 2)


# Trace the path from source to destination
def trace_path(cell_details, destination):
    print("The Path is:")
    path = []
    row, col = destination

    # Backtrack from the destination to the source using parent cells
    while not (
        cell_details[row][col].parent_row == row
        and cell_details[row][col].parent_col == col
    ):
        path.append((row, col))
        temp_row = cell_details[row][col].parent_row
        temp_col = cell_details[row][col].parent_col
        row, col = temp_row, temp_col

    # Add the source cell to the path
    path.append((row, col))
    path.reverse()

    # Print the path
    for cell in path:
        print("->", cell, end=" ")
    print()


# Implement the A* search algorithm
def a_star_search(grid, start, destination):
    # Check if the start and destination cells are valid and unblocked
    if not is_valid_cell(start[0], start[1]) or not is_valid_cell(
        destination[0], destination[1]
    ):
        print("Invalid start or destination cell.")
        return
    if not is_cell_unblocked(grid, start[0], start[1]) or not is_cell_unblocked(
        grid, destination[0], destination[1]
    ):
        print("Start or destination cell is blocked.")
        return
    if is_cell_destination(start[0], start[1], destination):
        print("We are already at the destination.")
        return

    # Initialize the closed list (visited cells)
    visited_cells = [[False for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
    # Initialize the details of each cell
    cell_details = [[Cell() for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

    # Initialize the start cell details
    start_row, start_col = start
    cell_details[start_row][start_col].f_cost = 0
    cell_details[start_row][start_col].g_cost = 0
    cell_details[start_row][start_col].h_cost = 0
    cell_details[start_row][start_col].parent_row = start_row
    cell_details[start_row][start_col].parent_col = start_col

    # Initialize the open list (priority queue of cells to be visited)
    open_list = []
    heapq.heappush(open_list, (0.0, start_row, start_col))

    # Flag to indicate if the destination has been found
    destination_found = False

    # Directions to move in the grid (8 possible moves)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    # Main loop of the A* search algorithm
    while open_list:
        # Pop the cell with the lowest f_cost from the open list
        current_f_cost, current_row, current_col = heapq.heappop(open_list)
        visited_cells[current_row][current_col] = True

        # Explore the neighboring cells
        for direction in directions:
            neighbor_row = current_row + direction[0]
            neighbor_col = current_col + direction[1]

            if (
                is_valid_cell(neighbor_row, neighbor_col)
                and is_cell_unblocked(grid, neighbor_row, neighbor_col)
                and not visited_cells[neighbor_row][neighbor_col]
            ):
                if is_cell_destination(neighbor_row, neighbor_col, destination):
                    cell_details[neighbor_row][neighbor_col].parent_row = current_row
                    cell_details[neighbor_row][neighbor_col].parent_col = current_col
                    print("Destination cell found!")
                    trace_path(cell_details, destination)
                    destination_found = True
                    return
                else:
                    new_g_cost = cell_details[current_row][current_col].g_cost + 1.0
                    new_h_cost = calculate_heuristic(
                        neighbor_row, neighbor_col, destination
                    )
                    new_f_cost = new_g_cost + new_h_cost

                    if (
                        cell_details[neighbor_row][neighbor_col].f_cost == float("inf")
                        or cell_details[neighbor_row][neighbor_col].f_cost > new_f_cost
                    ):
                        heapq.heappush(
                            open_list, (new_f_cost, neighbor_row, neighbor_col)
                        )
                        cell_details[neighbor_row][neighbor_col].f_cost = new_f_cost
                        cell_details[neighbor_row][neighbor_col].g_cost = new_g_cost
                        cell_details[neighbor_row][neighbor_col].h_cost = new_h_cost
                        cell_details[neighbor_row][
                            neighbor_col
                        ].parent_row = current_row
                        cell_details[neighbor_row][
                            neighbor_col
                        ].parent_col = current_col

    if not destination_found:
        print("Failed to find the destination cell.")


# Main function to run the A* search algorithm
def main():
    # Define the grid (1 for unblocked, 0 for blocked)
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    ]

    # Define the source and destination
    start = [8, 0]
    destination = [0, 0]

    # Run the A* search algorithm
    a_star_search(grid, start, destination)


if __name__ == "__main__":
    main()
