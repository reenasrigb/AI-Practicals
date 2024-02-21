from queue import Queue

goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
start_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]

def print_board(state):
    for i in range(9):
        if i % 3 == 0:
            print()
        print(state[i], end=' ')
    print()

def move(state, direction):
    new_state = state.copy()
    i = new_state.index(0)
    if direction == 'up':
        if i not in [0, 1, 2]:
            new_state[i], new_state[i - 3] = new_state[i - 3], new_state[i]
    elif direction == 'down':
        if i not in [6, 7, 8]:
            new_state[i], new_state[i + 3] = new_state[i + 3], new_state[i]
    elif direction == 'left':
        if i not in [0, 3, 6]:
            new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
    elif direction == 'right':
        if i not in [2, 5, 8]:
            new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
    return new_state

def bfs(start):
    visited = set()
    q = Queue()
    q.put((start, []))

    while not q.empty():
        state, path = q.get()
        visited.add(tuple(state))

        if state == goal_state:
            return path

        for direction in ['up', 'down', 'left', 'right']:
            new_state = move(state, direction)
            if tuple(new_state) not in visited:
                q.put((new_state, path + [direction]))

    return None

path = bfs(start_state)
if path:
    print("Moves to reach the goal state:")
    for move in path:
        print(move)
else:
    print("Goal state is not reachable from the given start state.")
