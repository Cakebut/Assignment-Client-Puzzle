# JUST RUN THE FILE AS PER NORMAL
# This is to compute the distribution of hashes required for the client to solve the puzzle.


import math
from collections import defaultdict

def calculate_arrangements(hits_per_puzzle):
    """Calculate ways to arrange hits across sub-puzzles."""
    arrangements = 1
    remaining_spots = 6  # Total sub-puzzles

    # Count each unique number of hits
    hit_counts = defaultdict(int)
    for hits in hits_per_puzzle:
        hit_counts[hits] += 1

    # Calculate arrangements based on different hit levels
    for count in hit_counts.values():
        arrangements *= math.comb(remaining_spots, count)
        remaining_spots -= count

    return arrangements

def find_combinations(total_hits, max_hits, parts):
    """Split total hits into `parts` where each part has at most `max_hits`."""
    if parts == 1:
        # If one part is left, it should match the remaining hits if valid
        if 1 <= total_hits <= max_hits:
            yield (total_hits,)
        return

    for i in range(1, min(total_hits, max_hits) + 1):
        for remainder in find_combinations(total_hits - i, max_hits, parts - 1):
            # Only allow valid, unique combinations
            combination = tuple(sorted((i,) + remainder))
            if all(part <= max_hits for part in combination):
                yield combination

def calculate_distributions(max_rows):
    """Calculate valid hit distributions up to a certain number of rows."""
    results = {}

    with open("Assignment/Assignment 2/puzzle_b_distribution.txt", "w") as file:
        for rows in range(6, max_rows + 1): #The value 6 is to be the same value as the subpuzzle ^^^^ remaining_spots = 6
            case_count = 0
            unique_distributions = set()

            # Generate unique ways to distribute hits across rows
            for hits in find_combinations(rows, 6, 6): #The value 6 is to be the same value as the subpuzzle ^^^^ remaining_spots = 6
                if hits not in unique_distributions:
                    unique_distributions.add(hits)
                    case_count += calculate_arrangements(hits)

            results[rows] = case_count
            file.write(f"Rows: {rows}, Cases: {case_count}\n")


calculate_distributions(96) # Change accordingly to how many possible cases there are
