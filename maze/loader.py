def load_maze(file_path):
    """
    Loads a maze from a text file and identifies start & goal.

    Symbols:
        # → Wall (1)
        . → Free (0)
        S → Start (0)
        G → Goal (0)
    """

    maze = []
    start = None
    goal = None

    with open(file_path, "r") as file:
        for row_index, line in enumerate(file):
            row = []
            for col_index, cell in enumerate(line.strip()):
                if cell == "#":
                    row.append(1)
                elif cell == ".":
                    row.append(0)
                elif cell == "S":
                    start = (row_index, col_index)
                    row.append(0)
                elif cell == "G":
                    goal = (row_index, col_index)
                    row.append(0)
                else:
                    raise ValueError(f"Invalid character '{cell}' in maze file")

            maze.append(row)

    if start is None or goal is None:
        raise ValueError("Maze must contain 'S' (start) and 'G' (goal).")

    return maze, start, goal
