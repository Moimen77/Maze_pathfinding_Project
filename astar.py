import heapq
import time

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    start_time = time.time()
    rows = len(maze)
    cols = len(maze[0])
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_cost = {start: 0}
    visited = []

    while open_set:
        _, current = heapq.heappop(open_set)
        visited.append(current)

        if current == goal:
            end_time = time.time()
            return reconstruct_path(came_from, start, goal), visited, g_cost[current], end_time - start_time

        for n in get_neighbors(current, rows, cols):
            r, c = n
            if maze[r][c] == 1:
                continue

            new_g = g_cost[current] + 1

            if n not in g_cost or new_g < g_cost[n]:
                g_cost[n] = new_g
                f_cost = new_g + manhattan_distance(n, goal)
                heapq.heappush(open_set, (f_cost, n))
                came_from[n] = current

    return None, visited, None, None

def get_neighbors(node, rows, cols):
    r, c = node
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    res = []
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if 0 <= nr < rows and 0 <= nc < cols:
            res.append((nr, nc))
    return res

def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path
