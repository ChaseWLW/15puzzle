import sys
import os
from math import sqrt

###To do 
### 1* pratical move
### 2* manhattan Distance
### 3* final state: blank position will influence the solvalble

class Puzzle:
	def __init__(self,initialState):
		self.state = initialState
		self.size = len(self.state)
		self.width = int(sqrt(self.size))
		self.checkPuzzle()
		self.position = self.state.index(0)
		self.moves = ['U','D','L','R']
		
		self.inversionNum = 0
		self.calInversion()
		self.solvable()
		
		self.manhattanDist = 0
		self.calManhDist()

####  Move  titles
	def swap(self,pos1,pos2):
		self.state[pos1],self.state[pos2] = self.state[pos2],self.state[pos1]

	def up(self):
		self.swap(self.position,self.position-self.width)
		self.position -= self.width
		self.calInversion()
	def down(self):
		self.swap(self.position,self.position+self.width)
		self.position += self.width
		self.calInversion()
	def left(self):
		self.swap(self.position,self.position-1)
		self.position -= 1
	def right(self):
		self.swap(self.position,self.position+1)
		self.position += 1

	
	
####  calculate inversion numbers
	def calInversion(self):
		array = self.state.copy()
		array.remove(0)
		self.inversionNum = 0
		
		for i in range(len(array)-1):
			for j in range(i,len(array)):
				if(array[i]>array[j]):
					self.inversionNum += 1

		
	def solvable(self):
		if(self.width %2 == 1 and self.inversionNum %2 == 1):
			print("Puzzle is insolvable! Exit!")
			os._exit(0)
		elif(self.width %2 == 0):
			if((self.position//self.width)%2  == self.inversionNum % 2):
				print("Puzzle is insolvable! Exit!")
				os._exit(0)
	

####    Check legal puzzle
	def checkPuzzle(self):
		if(self.width*self.width != self.size):
			print("Puzzle number is not correct! Exit!")
			os._exit(0)
		else:
			for ele in self.state:
				if(not isinstance(ele,int)):
					print("Tiles are not integer! Exit!")
					os._exit(0)

				if(ele<0 or ele>self.size):
					print("Tiles out of range! Exit!")
					os._exit(0)
						
				if(self.state.count(ele) != 1):
					print("Repeat tiles! Exit!")
					os._exit(0)

	
	def calManhDist(self):
		self.manhattanDist = 0
		for i in range(self.size):
			self.manhattanDist += abs(self.state[i]//self.width - i//self.width) ###row
			self.manhattanDist += abs(self.state[i]%self.width - i%self.width)  ###colum
