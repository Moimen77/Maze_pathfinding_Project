def dfs(maze, start, goal):
    stack = [start]
    visited_set = set()
    visited_order = []
    parent = {}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while stack:
        current = stack.pop()

        if current == goal:
            return reconstruct_path(parent, start, goal), visited_order

        if current not in visited_set:
            visited_set.add(current)
            visited_order.append(current)

            x, y = current
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                    if maze[nx][ny] == 0 and (nx, ny) not in visited_set:
                        parent[(nx, ny)] = current
                        stack.append((nx, ny))

    return [], visited_order

def reconstruct_path(parent, start, goal):
    """Reconstruct the final DFS path from parent dictionary."""
    path = []
    current = goal

    while current != start:
        path.append(current)
        if current not in parent:
            return []  # no path found
        current = parent[current]

    path.append(start)
    return path[::-1]
