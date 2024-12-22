import math
from collections import defaultdict

def calculate_combinations(distribution):
    """Calculate combinations for a specific hit distribution across sub-puzzles."""
    total_combinations = 1
    remaining_sub_puzzles = 6

    # Count occurrences of each "hit" level
    hit_counts = defaultdict(int)
    for hit in distribution:
        hit_counts[hit] += 1

    # For each unique hit count, calculate the combinations based on binomial coefficients
    for occurrences in hit_counts.values():
        total_combinations *= math.comb(remaining_sub_puzzles, occurrences)
        remaining_sub_puzzles -= occurrences

    return total_combinations

def generate_valid_partitions(n, max_value, parts):
    """Generate all unique, valid partitions of `n` into `parts` parts, each at most `max_value`."""
    if parts == 1:
        if 1 <= n <= max_value:
            yield (n,)
        return

    for i in range(1, min(n, max_value) + 1):
        for rest in generate_valid_partitions(n - i, max_value, parts - 1):
            partition = tuple(sorted((i,) + rest))
            if all(value <= max_value for value in partition):
                yield partition

def distribution_for_puzzle_b(max_rows):
    """Generate and count configurations of row distributions up to `max_rows`, ensuring only valid configurations."""
    results = {}

    with open("Assignment/Assignment 2/puzzle_b_distribution_debug.txt", "w") as file:
        for rows in range(6, max_rows + 1):
            total_cases = 0
            unique_distributions = set()

            # Generate all valid, unique partitions of `rows` into exactly 6 parts with each ≤ 6
            for distribution in generate_valid_partitions(rows, 6, 6):
                if distribution not in unique_distributions:
                    unique_distributions.add(distribution)
                    cases = calculate_combinations(distribution)
                    total_cases += cases
                    file.write(f"Rows: {rows}, Distribution: {distribution}, Cases for this distribution: {cases}\n")

            results[rows] = total_cases
            file.write(f"Total for Rows: {rows}, Cases: {total_cases}\n\n")

# Run function for rows up to 30 for debugging; adjust as needed
distribution_for_puzzle_b(96)
