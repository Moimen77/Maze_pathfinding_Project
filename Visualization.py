# ui/visualization.py
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import animation


def visualize(
    maze,
    start,
    goal,
    path=None,
    visited=None,
    title="Maze Visualization",
    animate=False
):
    """
    Enhanced visualization with clear grid, better colors, and cleaner layout.
    """

    rows, cols = len(maze), len(maze[0])

    fig, ax = plt.subplots(figsize=(cols / 2.5, rows / 2.5))
    ax.set_aspect('equal')
    ax.invert_yaxis()
    ax.set_xticks(range(cols))
    ax.set_yticks(range(rows))
    ax.grid(True, linewidth=0.5)

    # Draw maze walls
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 1:
                rect = patches.Rectangle((c, r), 1, 1, color='#2d2d2d')
                ax.add_patch(rect)

    # Draw visited nodes
    if visited:
        for (r, c) in visited:
            rect = patches.Rectangle((c, r), 1, 1, color='#ffd54f', alpha=0.35)
            ax.add_patch(rect)

    # Draw path
    if path:
        for (r, c) in path:
            rect = patches.Rectangle((c, r), 1, 1, color='#4caf50', alpha=0.4)
            ax.add_patch(rect)

        px = [c + 0.5 for (_, c) in path]
        py = [r + 0.5 for (r, _) in path]
        ax.plot(px, py, linewidth=2)

    # Start & Goal
    ax.text(start[1] + 0.5, start[0] + 0.5, "S",
            va='center', ha='center', fontsize=13, fontweight='bold', color='blue')
    ax.text(goal[1] + 0.5, goal[0] + 0.5, "G",
            va='center', ha='center', fontsize=13, fontweight='bold', color='red')

    ax.set_title(title, fontsize=14)
    plt.tight_layout()
    plt.show()

    # ------------------ ANIMATION MODE ------------------
    if animate and visited:
        fig, ax = plt.subplots(figsize=(cols / 2.5, rows / 2.5))
        ax.set_aspect('equal')
        ax.invert_yaxis()
        ax.set_xticks(range(cols))
        ax.set_yticks(range(rows))
        ax.grid(True, linewidth=0.5)

        for r in range(rows):
            for c in range(cols):
                if maze[r][c] == 1:
                    rect = patches.Rectangle((c, r), 1, 1, color='#2d2d2d')
                    ax.add_patch(rect)

        def update(frame):
            r, c = visited[frame]
            rect = patches.Rectangle((c, r), 1, 1, color='#ff9800', alpha=0.6)
            ax.add_patch(rect)
            return rect,

        animation.FuncAnimation(
            fig,
            update,
            frames=len(visited),
            interval=60,
            blit=True
        )

        if path:
            px = [c + 0.5 for (_, c) in path]
            py = [r + 0.5 for (r, _) in path]
            ax.plot(px, py, linewidth=2)

        ax.text(start[1] + 0.5, start[0] + 0.5, "S",
                va='center', ha='center', fontsize=13, fontweight='bold', color='blue')
        ax.text(goal[1] + 0.5, goal[0] + 0.5, "G",
                va='center', ha='center', fontsize=13, fontweight='bold', color='red')

        ax.set_title(title + " — Animated", fontsize=14)
        plt.show()
