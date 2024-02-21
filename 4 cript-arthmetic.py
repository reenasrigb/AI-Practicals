from itertools import permutations

def solve_cryptarithmetic(puzzle):
    words = puzzle.split()
    unique_chars = set(''.join(words))
    if len(unique_chars) > 10:
        return "Invalid input: More than 10 unique characters"

    chars = ''.join(unique_chars)
    for perm in permutations('1234567890', len(unique_chars)):
        mapping = dict(zip(chars, perm))
        if all(int(''.join(mapping[c] for c in word)) != 0 for word in words):
            if sum(int(''.join(mapping[c] for c in word)) for word in words[:-1]) == int(''.join(mapping[c] for c in words[-1])):
                return {k: int(v) for k, v in mapping.items()}

    return "No solution found"

# Example
puzzle = "SEND + MORE == MONEY"
solution = solve_cryptarithmetic(puzzle)
print(solution)
