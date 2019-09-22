#!/usr/bin/python
from random import choice

class Chromsome:
	def __init__(self,puzzle,chrom_len):
		self.steps = [None]*chrom_len
		self.minManhattanDist = puzzle.manhattanDist
		self.minInversionNum = puzzle.inversionNum
		self.minStep = 0
		self.fitness = puzzle.width*puzzle.size - self.minManhattanDist
		#self.fitness = (puzzle.size-1)(puzzle.size-2)/2 - self.minInversionNum
		#self.fitness = puzzle.width*puzzle.size+(puzzle.size-1)(puzzle.size-2)/2 -self.minManhattanDist- self.minInversionNum
		self.lastMove = None

		self.initialChr(puzzle,chrom_len)

	
	def initialChr(self,puzzle,chrom_len):
		for i in range(chrom_len):
			moves = puzzle.availMove(self.lastMove)
			move = moves.pop()
			puzzle.move(move)
			self.steps[i] = move
			self.lastMove = move
			if(self.minManhattanDist>puzzle.manhattanDist):
				self.minManhattanDist = puzzle.manhattanDist
				self.minStep = i


			
