from collections import deque

def shortest_path(rooms, doors, start, goal):
    # If there are no rooms, there is no path
    if not rooms:
        return []

    # If start and goal are the same, return [start]
    if start == goal:
        return [start]

    # Build adjacency list
    graph = {room: set() for room in rooms}
    for a, b in doors:
        graph[a].add(b)
        graph[b].add(a)

    visited = set()
    parent = {}  # child -> parent mapping for path reconstruction

    queue = deque([start])
    visited.add(start)

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

                if neighbor == goal:
                    # Reconstruct path
                    path = [goal]
                    while path[-1] != start:
                        path.append(parent[path[-1]])
                    path.reverse()
                    return path

    # If we exit the loop, goal was not reached
    return []
