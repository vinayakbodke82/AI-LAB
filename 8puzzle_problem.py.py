from collections import deque

# Function to print the puzzle state in grid form
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Possible moves (up, down, left, right)
moves = {
    'up': -3,
    'down': 3,
    'left': -1,
    'right': 1
}

# Check if move is valid
def is_valid(index, move):
    if move == 'left' and index % 3 == 0:
        return False
    if move == 'right' and index % 3 == 2:
        return False
    if move == 'up' and index < 3:
        return False
    if move == 'down' and index > 5:
        return False
    return True

# Function to get neighbors
def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)  # blank tile position
    for move, pos in moves.items():
        if is_valid(zero_index, move):
            new_state = state[:]
            swap_index = zero_index + pos
            # Swap blank with the adjacent tile
            new_state[zero_index], new_state[swap_index] = new_state[swap_index], new_state[zero_index]
            neighbors.append(new_state)
    return neighbors

# BFS Algorithm
def bfs(start, goal):
    queue = deque([start])
    visited = set()
    parent = {tuple(start): None}

    while queue:
        current = queue.popleft()
        
        if current == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = parent[tuple(current)]
            return path[::-1]

        visited.add(tuple(current))

        for neighbor in get_neighbors(current):
            if tuple(neighbor) not in visited and neighbor not in queue:
                parent[tuple(neighbor)] = current
                queue.append(neighbor)
    return None

# Example usage
start_state = [1, 2, 3,
               4, 0, 5,
               6, 7, 8]  # initial state (0 is the blank)

goal_state = [1, 2, 3,
              4, 5, 6,
              7, 8, 0]  # goal state

solution = bfs(start_state, goal_state)

if solution:
    print("Solution found in", len(solution)-1, "moves:")
    for step in solution:
        print_state(step)
else:
    print("No solution exists!")
