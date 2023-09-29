from collections import defaultdict

n = int(input())

graph = defaultdict(list)

for i in range(1, n + 1):
    a = int(input())
    graph[a].append(i)

checked = [0] * (n + 1)


def dfs(u, visited):
    visited.add(u)
    checked[u] = 1
    for i in graph[u]:
        if i not in visited:
            dfs(i, visited.copy())
        else:
            result.extend(list(visited))
            return


result = []
for i in range(1, n + 1):
    if not checked[i]:
        dfs(i, set([]))
result.sort()
print(result)
