# bfs.py
from collections import deque

def bfs(maze, start, goal):
    """
    تنفيذ خوارزمية Breadth-First Search لإيجاد أقصر مسار داخل المتاهة.
    - maze: قائمة ثنائية 2D
    - start: نقطة البداية (r, c)
    - goal: نقطة الهدف (r, c)
    
    يرجّع:
        path: المسار النهائي
        visited: النقاط التي تم زيارتها
    """

    queue = deque([start])
    visited = set([start])
    parent = {}
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    visited_order = []

    while queue:
        current = queue.popleft()
        visited_order.append(current)

        if current == goal:
            break

        for d in dirs:
            nr = current[0] + d[0]
            nc = current[1] + d[1]

            if (
                0 <= nr < len(maze)
                and 0 <= nc < len(maze[0])
                and maze[nr][nc] != "#"
                and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                parent[(nr, nc)] = current
                queue.append((nr, nc))

    # إعادة بناء المسار Path
    path = []
    if goal in visited:
        cur = goal
        while cur != start:
            path.append(cur)
            cur = parent[cur]
        path.append(start)
        path.reverse()

    return path, visited_order