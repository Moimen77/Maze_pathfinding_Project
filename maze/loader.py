def load_maze(file_path):
    """
    Loads a maze from a text file and identifies the start and goal positions.

    Symbols:
        '#' → Wall
        '.' → Free cell
        'S' → Start
        'G' → Goal
    """

    maze = []
    start = None
    goal = None

    with open(file_path, "r") as file:
        for row_index, line in enumerate(file):
            row = list(line.strip())
            maze.append(row)

            for col_index, cell in enumerate(row):
                if cell == "S":
                    start = (row_index, col_index)
                elif cell == "G":
                    goal = (row_index, col_index)

    if start is None or goal is None:
        raise ValueError("Maze must contain 'S' for start and 'G' for goal.")

    return maze, start, goal