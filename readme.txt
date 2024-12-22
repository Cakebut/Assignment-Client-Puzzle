CLIENT PUZZLE 

Puzzle A: One sub–puzzles. k = 6. 
Puzzle B: Six sub-puzzles. k = 4. 

Run the code on any python terminal (VSC, Idle, etc...)

This code is intended to generate all possible cases for Question 1 Puzzle B. 

Edit this portion of the code first to wherever you saved this file accordingly.

with open("Assignment/Assignment 2/puzzle_b_distribution.txt", "w") as file:


Once done just execute it.

-------------------------------------------------------------------------------------------------------

The purpose is to use a Python program that calculates all possible ways of assigning rows across six sub
puzzles. Using the combinations_with_replacement function from Python's itertools library, I 
generated different ways to distribute the total rows, with each sub-puzzle receiving between 
1 and 6 rows. Then, I filtered these distributions based on the row constraints (i.e., no sub
puzzle should exceed 6 rows), for example, {7,1,1,1,1,1} would be invalid.

