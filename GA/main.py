#!/usr/bin/python
from  InitialPopulation  import *
from Puzzle import Puzzle

GENE_LEN = 140 
POPULATION_SIZE=100
CROSSOVER_RATE = 0.25
MUTATION_RATE=0.01
ELITES_SIZE = 10
MAX_GENERATION = 1000


if __name__ == '__main__':
	initState=[2,1,0,3]
	puzzle = Puzzle(initState)
	print(puzzle.state)
