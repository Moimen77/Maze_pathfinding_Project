# bfs.py
from collections import deque


def bfs(maze, start, goal):
    """
    Breadth-First Search to find the shortest path in a maze.

    Returns:
        path          : shortest path from start to goal
        visited_order : nodes visited in order
    """

    queue = deque([start])
    visited = set([start])
    visited_order = []
    parent = {}

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        current = queue.popleft()
        visited_order.append(current)

        if current == goal:
            break

        for dr, dc in dirs:
            nr, nc = current[0] + dr, current[1] + dc

            if (
                0 <= nr < len(maze)
                and 0 <= nc < len(maze[0])
                and maze[nr][nc] == 0
                and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                parent[(nr, nc)] = current
                queue.append((nr, nc))

    # Reconstruct path
    path = []
    if goal in visited:
        cur = goal
        while cur != start:
            path.append(cur)
            cur = parent[cur]
        path.append(start)
        path.reverse()

    return path, visited_order
