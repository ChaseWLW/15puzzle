#!/usr/bin/python
from random import choice
from copy import deepcopy

class Chromsome:
	def __init__(self,puzzle,chrom_len):
		self.puzzle = deepcopy(puzzle)
		self.chrom_len = chrom_len
		self.steps = [None]*(chrom_len+1)
		self.positions = [None]*(chrom_len+1)
		self.positions[0] = self.puzzle.position
		self.states = {0:self.puzzle.state.copy()}

		self.minManhattanDist = self.puzzle.manhattanDist
		self.minInversionNum = self.puzzle.inversionNum
		self.minStep = 0
		self.fitness = self.puzzle.width*self.puzzle.size - self.minManhattanDist
		self.lastMove = None

		self.initialChr()
		#self.puzzle.display()
		#self.fitness = (self.puzzle.size-1)(self.puzzle.size-2)/2 - self.minInversionNum
		#self.fitness = self.puzzle.width*self.puzzle.size+(self.puzzle.size-1)(self.puzzle.size-2)/2 -self.minManhattanDist- self.minInversionNum

	
	def initialChr(self):
		for i in range(1,self.chrom_len+1):
			moves = self.puzzle.availMove(self.lastMove)
			move = choice(moves)
			self.steps[i] = move
			self.lastMove = move
			self.puzzle.move(move)
			self.states[i] = self.puzzle.state.copy()
			self.positions[i] = self.puzzle.position

			#print('self.puzzle state in step ',i)
			#self.puzzle.display()
			#print("inversionNum:",self.puzzle.inversionNum)
			#print("manhattanDist:",self.puzzle.manhattanDist)

			#if(self.minInversionNum>self.puzzle.inversionNum):
				#self.minManhattanDist = self.puzzle.manhattanDist
			#	self.minInversionNum = self.puzzle.inversionNum
			#	self.minStep = i
			if(self.minManhattanDist>self.puzzle.manhattanDist):
				self.minManhattanDist = self.puzzle.manhattanDist
				self.minStep = i

	
