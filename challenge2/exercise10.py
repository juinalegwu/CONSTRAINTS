def path_exists(graph, start, target, visited=None):
    if visited is None:
        visited = set()

    if start == target:
        return True

    if start in visited:
        return False

    visited.add(start)

    for neighbour in graph.get(start, []):
        if path_exists(graph, neighbour, target, visited):
            return True

    return False


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": ["F"],
    "F": []
}

print(path_exists(graph, "A", "F"))   
print(path_exists(graph, "D", "A"))  
 