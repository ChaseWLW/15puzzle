#!/usr/bin/python
from Puzzle import Puzzle
from Chromsome import Chromsome

CHROM_LEN = 10
POPULATION_SIZE=2
CROSSOVER_RATE = 0.25
MUTATION_RATE=0.01
ELITES_SIZE = 10
MAX_GENERATION = 1000




if __name__ == '__main__':
	initState=[4,5,6,7,8,2,1,3,0]
	puzzle = Puzzle(initState)
	puzzle.display()
	print("mahattan distance: ",puzzle.manhattanDist)
	print("inversion number: ",puzzle.inversionNum)
	moves = puzzle.availMove('R')
	#print(moves.pop())
	chromsome = Chromsome(puzzle,CHROM_LEN)
	print(chromsome.steps)
