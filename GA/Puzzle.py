import sys
import os
from math import sqrt

INVERT = dict(L='R',R='L',U='D',D='U') 

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
		self.position = pos2

	def up(self):
		new_position = self.position-self.width
		self.changeRowManhDist(self.position,new_position)
		self.inversionNum +=  self.changeInversion(self.state[new_position+1:self.position],self.state[new_position])
		self.swap(self.position,new_position)
	def down(self):
		new_position = self.position+self.width
		self.changeRowManhDist(self.position,new_position)
		self.inversionNum -=  self.changeInversion(self.state[self.position+1:new_position],self.state[new_position])
		self.swap(self.position,new_position)

	def left(self):
		self.changeColManhDist(self.position,self.position-1)
		self.swap(self.position,self.position-1)
	def right(self):
		self.changeColManhDist(self.position,self.position+1)
		self.swap(self.position,self.position+1)

	def move(self,move):
		if move=="U":
			self.up()
		elif move=="D":
			self.down()
		elif move=="L":
			self.left()
		elif move=="R":
			self.right()
		else:
			print("Invalid step name. please enter either 'U','D','L','R'") 
	
	
####  calculate inversion numbers
	def calInversion(self):
		array = self.state.copy()
		array.remove(0)
		self.inversionNum = 0
		
		for i in range(len(array)-1):
			for j in range(i,len(array)):
				if(array[i]>array[j]):
					self.inversionNum += 1

####  calculate inversion numbers
	def changeInversion(self,array,movingNum):
		change = 0
		for ele in array:
			if(ele>movingNum):
				change += 1
			else:
				change -= 1

		return change
		
	def solvable(self):
		if(self.width %2 == 1 and self.inversionNum %2 == 1):
			print("Puzzle is insolvable! Exit!")
			os._exit(0)
		elif(self.width %2 == 0):
			if((self.position//self.width)%2  == self.inversionNum % 2):
				print("Puzzle is insolvable! Exit!")
				os._exit(0)
	


	
	def calManhDist(self):
		self.manhattanDist = 0
		for i in range(self.size):
			if(self.state[i]>0):
				self.manhattanDist += abs((self.state[i]-1)//self.width - i//self.width) ###Row
				self.manhattanDist += abs((self.state[i]-1)%self.width - i%self.width)  ###Col

	def changeColManhDist(self,pos1,pos2):
		 man1 = abs((self.state[pos2]-1)%self.width - pos1%self.width) ###Col After
		 man2 = abs((self.state[pos2]-1)%self.width - pos2%self.width) ###Col Before
		 self.manhattanDist += (man1-man2)

	def changeRowManhDist(self,pos1,pos2):
		 man1 = abs((self.state[pos2]-1)//self.width - pos1//self.width) ###Row After
		 man2 = abs((self.state[pos2]-1)//self.width - pos2//self.width) ###Row Before
		 self.manhattanDist += (man1-man2)


####    Check legal self
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
	

	def display(self):
		for i in range(self.size):
			print('%-3d' % self.state[i],end='')
			if(i%self.width==self.width-1):
				print()

	
	def availMove(self,lastMove):
		moves = ['U','D','L','R']

		if(self.position % self.width == 0):
			moves.remove('L')
		elif(self.position % self.width == self.width-1):
			moves.remove('R')

		if(self.position //  self.width == 0):
			moves.remove('U')
		elif(self.position //  self.width == self.width-1):
			moves.remove('D')

		if lastMove in INVERT.keys():
			moves.remove(INVERT[lastMove])

		return moves
