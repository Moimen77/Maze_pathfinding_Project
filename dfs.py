# ------------------------------------------
# Depth-First Search (DFS) Algorithm
# ------------------------------------------

def dfs(maze, start, goal):
    """
    DFS algorithm for maze pathfinding.
    Parameters:
        maze  : 2D grid (0 = path, 1 = wall)
        start : (x, y)
        goal  : (x, y)
    Returns:
        path     : final path from start to goal
        visited  : all visited nodes
    """

    stack = [start]
    visited = set()
    parent = {}

    # Directions: Right, Down, Left, Up
    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    while stack:
        current = stack.pop()

        if current == goal:
            return reconstruct_path(parent, start, goal), visited

        if current not in visited:
            visited.add(current)
            x, y = current

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                    if maze[nx][ny] == 0 and (nx, ny) not in visited:
                        parent[(nx, ny)] = current
                        stack.append((nx, ny))

    return [], visited


def reconstruct_path(parent, start, goal):
    """Reconstruct the final DFS path."""
    path = []
    current = goal

    while current != start:
        path.append(current)
        if current not in parent:
            return []
        current = parent[current]

    path.append(start)
    return path[::-1]
