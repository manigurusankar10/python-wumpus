import random


### Class for individual rooms in the cave
class Room():
	def __init__(self, name, value):
		self.wumpus = False
		self.pit = False
		self.bat = False
		self.gold = False
		self.name = name
		self.empty = True
		self.value = value

### Class for all the rooms in the cave.
class Cave():

	#intial function to create the 4 x 4 grid of Rooms
	def __init__(self):
		self._rooms = [[Room('x', None) for x in range(4)] for y in range(4)]
		self._map = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)]
		self.assignValues()
		self.assignHazards()
		   
	#Assign values to each room to keep track of the player location    
	def assignValues(self):
		i = 1;
		for row in range(4):
			for item in range(4):
				self._rooms[row][item].value = i;
				i = i + 1

	#Assign hazards, players and the gold randomnly
	def assignHazards(self):
		i = 0
		location = [(x, y) for x in range(4) for y in range(4)]
		while i < 7:
			#random x,y coordinates
			x, y = random.choice(location)

			#only add to room is its empty
			if self._rooms[x][y].empty == True:
				if i == 0:
					self._rooms[x][y].name = 'P'
					self._rooms[x][y].empty = False
					self.playerLoc = self._rooms[x][y].value
				elif i == 1:
					self._rooms[x][y].name = 'W'
					self._rooms[x][y].empty = False
					self._rooms[x][y].wumpus = True
				elif i == 2:
					self._rooms[x][y].name = 'G'
					self._rooms[x][y].empty = False
					self._rooms[x][y].gold = True
				elif i == 3:
					self._rooms[x][y].name = 'p1'
					self._rooms[x][y].empty = False
					self._rooms[x][y].pit = True
				elif i == 4:
					self._rooms[x][y].name = 'p2'
					self._rooms[x][y].empty = False
					self._rooms[x][y].pit = True
				elif i == 5:
					self._rooms[x][y].name = 'b1'
					self._rooms[x][y].empty = False
					self._rooms[x][y].bat = True
				elif i == 6:
					self._rooms[x][y].name = 'b2'
					self._rooms[x][y].empty = False
					self._rooms[x][y].bat = True

				i = i + 1              

	#print the layout of the cave. ONLY for debugging purposes
	def printCave(self):
		for row in range(4):
			for item in range(4):
				print '{:9}'.format(self._rooms[row][item].name),
			print

	#get the x,y coordinates of a cell
	def getLocationValue(self, value):
		locx, locy = self._map[value - 1]
		return locx, locy

	#check to see if the room is a pit
	def isPit(self, locx, locy):
		return self._rooms[locx][locy].pit

	#check to see if the room has bats
	def isBat(self, locx, locy):
		return self._rooms[locx][locy].bat

	#check to see if the room has gold
	def isGold(self, locx, locy):
		return self._rooms[locx][locy].gold

	#check to see if the room has wumpus
	def isWumpus(self, locx, locy):
		return self._rooms[locx][locy].wumpus

	#get the neighbors of the cell
	def getNeighbors(self, value):
		neighbors = []
		locx, locy = self._map[value - 1]

		if locy - 1 >= 0:
			neighbors.append(self._rooms[locx][locy - 1].value)
		if locx - 1 >= 0:
			neighbors.append(self._rooms[locx - 1][locy].value)
		if locy + 1 <= 3:
			neighbors.append(self._rooms[locx][locy + 1].value)
		if locx + 1 <= 3:
			neighbors.append(self._rooms[locx + 1][locy].value)

		return neighbors

	#get the player location
	def getPlayerLocation(self, loc=None):
		if loc is None:
			return self.playerLoc
		else:
			locx, locy = self.getLocationValue(loc)
			return self._rooms[locx][locy].value

	#get the hazards localled near the player location
	def getHazards(self, neighbors):
		hazards = []

		for i in neighbors:
			valueX, valueY = self.getLocationValue(i)
			if self.isPit(valueX, valueY):
				hazards.append("You feel a breeze")
			elif self.isBat(valueX, valueY):
				hazards.append("You hear wings flapping")
			elif self.isGold(valueX, valueY):
				hazards.append("You see a glimmer nearby")
			elif self.isWumpus(valueX, valueY):
				hazards.append("You smell a terrible stench")

		return hazards

	#set value to the cell if wumpus is killed
	def wumpusKilled(self, locx, locy):
		self._rooms[locx][locy].wumpus = False

	#def moveWumpus(self, locx, locy):

	#check to see if the wumpus is nearby to the player's location
	def isWumpusNearby(self, locx, locy):
		wumpusNearby = False

		if self.isWumpus(locx, locy - 1) is True or self.isWumpus(locx - 1, locy) is True or self.isWumpus(locx, locy + 1) is True or self.isWumpus(locx + 1, locy) is True:
			wumpusNearby = True

		return wumpusNearby

class Game:
	def __init__(self):
		self.cave = Cave()
		#self.cave.printCave()
		self.arrows = 3
		self.gotGold = False
		self.killedWumpus = False
		self.gameOver = False

		self.moveAction()

		self.initialLoc = self.playerLoc

		while not self.gameOver:
			self.output()

	# inputs and outputs messages to the player
	def output(self):
		print
		print
		print
		print "You are in room " + str(self.playerLoc)
		for i in self.hazards:
			print i
		print "Exists go to: "  + (str(self.playerNeighbors))
		print "----------------------------------------- "
		while True: 
			action = raw_input("What do you want to do? (m)ove or (s)hoot? ")
			if action not in ('m', 's'):
				print("Not an appropriate choice.")
			else:
				break
		while True:
			newLoc = raw_input("Where? ")
			if int(newLoc) not in self.playerNeighbors:
				print("Not an appropriate choice.")
			else:
				break
		print "----------------------------------------- "

		if action == "m" or action == "s":
			self.performAction(action, newLoc)
		else:
			print "please"

	# when user enter 'm' or 's'
	def performAction(self, action=None, newLoc=None):
		if action == "m":
			#player got the gold, killed the wumpus and got back to their initial location		
			if int(newLoc) == self.initialLoc and self.gotGold is True and self.killedWumpus is True:
				print "You WON!!!!!!!!!!! :) :) :)"
				self.gameOver = True
			else:
				self.moveAction(newLoc)	
		elif action == "s":
		 	self.shootAction(newLoc)

	# when user enters 'm'
	def moveAction(self, newLoc=None):
		if newLoc is not None:
			self.playerLoc = self.cave.getPlayerLocation(int(newLoc))
		else:
			self.playerLoc = self.cave.getPlayerLocation()

		self.playerNeighbors = self.cave.getNeighbors(self.playerLoc)
		self.hazards = self.cave.getHazards(self.playerNeighbors)
		locx, locy = self.cave.getLocationValue(self.playerLoc)

		if self.cave.isPit(locx, locy):
			print "You fell in a pit"
			print "YOU LOST!!!!!!!!!!!! :D :D :D :D"
			self.gameOver = True
		elif self.cave.isBat(locx, locy):
			self.playerLoc =  random.randint(1, 16)
			print "You entered a room full of bats. The bat takes you to a room " + str(self.playerLoc)
			self.moveAction(self.playerLoc)
		elif self.cave.isWumpus(locx, locy):
			print "You entered a room where Wumpus was sleeping. It eats you and kills you"
			print "YOU LOST!!!!!!!!!!!! :D :D :D :D"
			self.gameOver = True
		elif self.cave.isGold(locx, locy):
			print "You entered a room where there is Gold. You pick it up"
			self.cave._rooms[locx][locy].gold = False
			self.gotGold = True

	# when user enters 's'
	def shootAction(self, loc):
		locx, locy = self.cave.getLocationValue(int(loc))

		if self.cave.isWumpus(locx, locy):
			print "YOU KILLED THE WUMPUS!"
			self.killedWumpus = True
			self.cave.wumpusKilled(locx,locy)
			self.hazards = self.cave.getHazards(self.playerNeighbors)
		else:
			print "You missed!!"
			self.arrows = self.arrows - 1
			playerlocX, playerLocY = self.cave.getLocationValue(self.playerLoc)
			if self.cave.isWumpusNearby(playerlocX, playerLocY) is True:
				print "Wumpus heard you from firing the arrow. It comes into your room and eats you"
				print "YOU LOST!!!!!!!!!!!! :D :D :D :D"
				self.gameOver = True
			elif self.arrows < 1:
				print "You ran out of arrows!!!!"
				print "YOU LOST!!!!!!!!!!!! :D :D :D :D"
				self.gameOver = True

if __name__ == "__main__":
	game = Game()
