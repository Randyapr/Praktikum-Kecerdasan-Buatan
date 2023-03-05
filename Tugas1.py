def blind_search(start, goal, graph):
    queue = [[start]]
    visited = set()


    while queue:
        path = queue.pop(0)
        node = path[-1]

 
        if node == goal:
            return path


        if node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

            visited.add(node)
    return None

graph = {
    0: [1, 3, 4],
    1: [0, 2, 3],
    2: [1, 3],
    3: [0, 1, 2, 4],
    4: [0, 3],
}
start = 0 #mulai dari 0
goal = 2 #tujuan ke 2
result = blind_search(start, goal, graph)
if result is None:
    print("Tidak ada jalur yang ditemukan.")
else:
    print("Jalur terpendek dari", start, "ke", goal, "adalah=", result)
