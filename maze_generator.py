import random

def generate_random_maze(rows, cols, wall_prob=0.3):
    maze = []
    for r in range(rows):
        row = []
        for c in range(cols):
            if random.random() < wall_prob:
                row.append(1)  # wall
            else:
                row.append(0)  # path
        maze.append(row)

    start = (0, 0)
    goal = (rows - 1, cols - 1)

    maze[start[0]][start[1]] = 0
    maze[goal[0]][goal[1]] = 0

    return maze, start, goal


def is_valid_maze(maze, start, goal):
    if maze[start[0]][start[1]] == 1:
        return False
    if maze[goal[0]][goal[1]] == 1:
        return False
    return True
