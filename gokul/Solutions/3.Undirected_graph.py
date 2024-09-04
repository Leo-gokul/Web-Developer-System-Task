import sys
import ast

def min_key(keys, mst_set, n):
    min_value = sys.maxsize
    min_index = -1
    for v in range(n):
        if keys[v] < min_value and not mst_set[v]:
            min_value = keys[v]
            min_index = v
    return min_index

def prim_mst(graph):
    n = len(graph)
    keys = [sys.maxsize] * n
    parent = [-1] * n
    mst_set = [False] * n
    keys[0] = 0  # Start from the first vertex
    parent[0] = -1
    for _ in range(n - 1):
        u = min_key(keys, mst_set, n)
        mst_set[u] = True
        for v in range(n):
            if graph[u][v] and not mst_set[v] and graph[u][v] < keys[v]:
                keys[v] = graph[u][v]
                parent[v] = u
    mst_weight = sum(graph[parent[i]][i] for i in range(1, n))
    return mst_weight

def main():
    # Get input from the user lists (e.g., [[0,2,0],[2,0,3],[0,3,0]]):
    user_input = input("graph=")
    # Convert input string to a 2D list of integers
    graph = ast.literal_eval(user_input)
    # Calculate and print the MST weight
    result = prim_mst(graph)
    print("Output=", result)

if __name__ == "__main__":
    main()
