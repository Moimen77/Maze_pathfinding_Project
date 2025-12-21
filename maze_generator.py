import random

def generate_valid_maze(rows, cols, wall_prob=0.3):
    while True:
        maze, start, goal = generate_random_maze(rows, cols, wall_prob)
        if is_valid_maze(maze, start, goal):
            from dfs import dfs
            path, _ = dfs(maze, start, goal)
            if path:
                return maze, start, goal

def is_valid_maze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])

    sx, sy = start
    gx, gy = goal

    if not (0 <= sx < rows and 0 <= sy < cols):
        return False
    if not (0 <= gx < rows and 0 <= gy < cols):
        return False

    if maze[sx][sy] == 1 or maze[gx][gy] == 1:
        return False

    return True


def generate_random_maze(rows, cols, wall_prob=0.3):
    maze = []
    for r in range(rows):
        row = []
        for c in range(cols):
            if random.random() < wall_prob:
                row.append(1)
            else:
                row.append(0)
        maze.append(row)

    start = (0, 0)
    goal = (rows - 1, cols - 1)

    maze[start[0]][start[1]] = 0
    maze[goal[0]][goal[1]] = 0

    return maze, start, goal
