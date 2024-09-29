from collections import defaultdict

def dfs(node, graph, visited, order):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, order)
    order.append(node)

def topological_sort(graph, n):
    visited = [False] * n
    order = []
    for i in range(n):
        if not visited[i]:
            dfs(i, graph, visited, order)
    return order[::-1]

def solve_mikado(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        cases = int(lines[0])
        lines = lines[1:]
        i = 0
        case_num = 1
        while i < len(lines):
            n, m = map(int, lines[i].split())
            graph = defaultdict(list)
            for j in range(i+1, i+m+1):
                x, y = map(int, lines[j].split())
                graph[y].append(x)
            order = topological_sort(graph, n)
            print(f"Case #{case_num}: {' '.join(map(str, order))}")
            case_num += 1
            i += m + 1

if __name__ == "__main__":
    solve_mikado("input-mikado-3596.txt")
