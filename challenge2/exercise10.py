from collection import deque

def path_exists(graph, start, target):
    if start == target:
        return True

    for neighbor in graph.get(start, []):
        if path_exists(graph, neighbor, target):
            return True

    return False