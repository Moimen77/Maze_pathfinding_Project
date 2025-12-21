# main.py
from Visualization import visualize
from maze_generator import generate_valid_maze
from dfs import dfs
from bfs import bfs
from astar import a_star

def main():
    print("=== Maze Pathfinding Visualization ===\n")

    # 1️⃣ Generate a random maze
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    maze, start, goal = generate_valid_maze(rows, cols, wall_prob=0.3)

    # 2️⃣ Choose the algorithm
    print("\nChoose an algorithm:")
    print("1 - DFS")
    print("2 - BFS")
    print("3 - A*")
    choice = input("Your choice (1/2/3): ")

    if choice == "1":
        path, visited = dfs(maze, start, goal)
        alg_name = "DFS"
    elif choice == "2":
        path, visited = bfs(maze, start, goal)
        alg_name = "BFS"
    elif choice == "3":
        path, visited = a_star(maze, start, goal)
        alg_name = "A*"
    else:
        print("Invalid choice!")
        return

    # 3️⃣ Run the visualization
    visualize(
        maze,
        start,
        goal,
        path=path,
        visited=visited,
        animate=True,
        title=f"{alg_name} — Maze Solver"
    )

if __name__ == "__main__":
    main()
