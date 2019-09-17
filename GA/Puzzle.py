import sys
import os
from math import sqrt

###To do 
### 1* pratical move
### 2* check legal puzzle


class Puzzle:
	def __init__(self,initialState):
		self.state = initialState
		self.position = self.state.index(0)
		self.size = int(sqrt(len(self.state)))
		self.moves = ['U','D','L','R']
		self.inversionNum = 0
		self.inversion()
		self.solvable()

####  Move blank titles
	def swap(self,pos1,pos2):
		self.state[pos1],self.state[pos2] = self.state[pos2],self.state[pos1]

	def up(self):
		self.swap(self.position,self.position-self.size)
		self.position -= self.size
		self.inversion()
	def down(self):
		self.swap(self.position,self.position+self.size)
		self.position += self.size
		self.inversion()
	def left(self):
		self.swap(self.position,self.position-1)
		self.position -= 1
	def right(self):
		self.swap(self.position,self.position+1)
		self.position += 1

	
	
####  calculate inversion numbers
	def inversion(self):
		array = self.state.copy()
		array.remove(0)
		self.inversionNum = 0
		
		for i in range(len(array)-1):
			for j in range(i,len(array)):
				if(array[i]>array[j]):
					self.inversionNum += 1

		
	def solvable(self):
		if(self.size %2 == 1 and self.inversionNum %2 == 1):
			print("puzzle is insolvable! exit!")
			os._exit(0)
		elif(self.size %2 == 0):
			if((self.position//self.size)%2  == self.inversionNum % 2):
				print("puzzle is insolvable! exit!")
				os._exit(0)
