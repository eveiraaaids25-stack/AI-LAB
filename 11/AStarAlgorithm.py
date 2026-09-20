"""
EX.NO: 11  IMPLEMENT A* ALGORITHM
AIM: To implement A* algorithm using Python programming.
"""

import heapq


class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost from current node to goal
        self.f = 0  # Total cost

    def __lt__(self, other):
        return self.f < other.f


def heuristic(a, b):
    # Using Manhattan distance as heuristic
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def add_to_open(open_list, neighbor):
    for node in open_list:
        if neighbor.position == node.position and neighbor.g > node.g:
            return False
    return True


def a_star(maze, start, end):
    start_node = Node(start)
    end_node = Node(end)

    open_list = []
    closed_list = set()

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        # Found the goal
        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        # Generate children
        (x, y) = current_node.position
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for next_position in neighbors:
            # Ensure within range and walkable terrain
            if (0 <= next_position[0] < len(maze)) and (0 <= next_position[1] < len(maze[0])) \
                    and maze[next_position[0]][next_position[1]] == 0:
                neighbor = Node(next_position, current_node)

                if neighbor.position in closed_list:
                    continue

                neighbor.g = current_node.g + 1
                neighbor.h = heuristic(neighbor.position, end_node.position)
                neighbor.f = neighbor.g + neighbor.h

                if add_to_open(open_list, neighbor):
                    heapq.heappush(open_list, neighbor)

    return None  # No path found


def main():
    maze = [
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (4, 6)

    path = a_star(maze, start, end)
    print("Path found:", path)


if __name__ == "__main__":
    main()
