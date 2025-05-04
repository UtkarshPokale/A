from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph.get(node, []))

    return result

def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(reversed(graph.get(node, [])))

    return result

def main():
    print("Enter the graph as an adjacency list (e.g., A:B,C D:E,F):")
    graph = {}

    while True:
        line = input("Enter node and its neighbors (or just press Enter to stop): ").strip()
        if not line:
            break

        try:
            node, neighbors = line.split(":")
            graph[node] = neighbors.split(",") if neighbors else []
        except ValueError:
            print("Invalid input format. Please use 'Node:Neighbor1,Neighbor2' format.")

    start_node = input("Enter the starting node for BFS and DFS: ").strip()

    if start_node not in graph:
        print(f"Error: Node '{start_node}' is not in the graph.")
        return

    print("\nBreadth-First Search (BFS):")
    print(bfs(graph, start_node))

    print("\nDepth-First Search (DFS):")
    print(dfs(graph, start_node))

if __name__ == "__main__":
    main()
