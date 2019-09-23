#!/usr/bin/python
from Puzzle import Puzzle
from Chromsome import Chromsome

CHROM_LEN = 100
POPULATION_SIZE=200
CROSSOVER_RATE = 0.25
MUTATION_RATE=0.01
ELITES_SIZE = 10
MAX_GENERATION = 1000




if __name__ == '__main__':
	initState=[4,5,6,7,8,2,1,3,0,9,10,11,12,13,15,14]
	puzzle = Puzzle(initState)
	print("Initail Puzzle:")
	puzzle.display()
	print("Initial Mahattan distance: ",puzzle.manhattanDist)
	print("Initial inversion number: ",puzzle.inversionNum)

	#puzzle.move('U')
	#puzzle.display()
	#print(puzzle.availMove('U'))


	chro = [None]*POPULATION_SIZE
	for i in range(POPULATION_SIZE):
		chro[i] = Chromsome(puzzle,CHROM_LEN)
	
	#chromsome = Chromsome(puzzle,CHROM_LEN)
	chromsome = chro[100]
	print(chromsome.steps)
	print('min manhattanDist: ',chromsome.minManhattanDist)
	print('min step: ',chromsome.minStep)
	print('min state: ',chromsome.states[chromsome.minStep])
	print('min pos: ',chromsome.positions[chromsome.minStep])
