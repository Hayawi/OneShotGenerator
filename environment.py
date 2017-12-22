from random import randint 

class room():
	def __init__(self, maxX, maxY, dungeonCol, dungeonRow):
		self.xSize = randint(dungeonCol / 10,maxX)
		self.ySize = randint(dungeonRow / 10,maxY)
		self.xLocation = randint(self.xSize,dungeonCol - self.xSize)
		self.yLocation =  randint(self.ySize,dungeonRow - self.ySize)
		self.roomStatus = False
		self.connectedToMainRoom = False

class environment(object): 
	#0 is empty space, 1 is wall, 2 is encounter, 3 is treasure, 4 is furniture
	def __init__(self, row, col, initPass, carvePass, numberOfRooms):
		self.dungeonRow = int(row)
		self.dungeonCol = int(col)
		self.rooms = int(numberOfRooms)
		dungeonMap = [[1 for i in range(self.dungeonCol)] for j in range(self.dungeonRow)] 
		self.initializationPass = int(initPass)
		self.carvingPass = int(carvePass)
		
		#dungeonMap = self.generateCave(dungeonMap)
		dungeonMap = self.generateDungeon(dungeonMap)
		
		dungeonMap = self.populateDungeon(dungeonMap, self.dungeonRow, self.dungeonCol)
		self.dungeonLayout = self.dungeofy(dungeonMap, self.dungeonRow, self.dungeonCol) 
	
	def generateDungeon(self, map):	
		roomList = [room(self.dungeonCol / 5, self.dungeonRow / 5, self.dungeonCol, self.dungeonRow) for i in range(self.rooms)]
		mainRoom = randint(0,4)
		roomList[mainRoom].roomStatus = True
		roomList[mainRoom].connectedToMainRoom = True
		for i in range(self.dungeonRow):
			for j in range(self.dungeonCol):
				for k in roomList:
				
					if k.xLocation == j and k.yLocation == i:
						for l in range(i-k.ySize/2, i+k.ySize/2):
							for m in range(j-k.xSize/2, j+k.xSize/2):
								map[l][m] = 0
					
					if randint(0, 4) == 3:
						roomToConnect = randint(0, self.rooms - 1)
						k.connectedToMainRoom = roomList[roomToConnect].connectedToMainRoom
						startingX = 0
						startingY = 0
						endingX = 0
						endingY = 0
						if k.xLocation < roomList[roomToConnect].xLocation:
							startingX = k.xLocation
							endingX = roomList[roomToConnect].xLocation
						else:
							startingX = roomList[roomToConnect].xLocation
							endingX = k.xLocation
						if k.yLocation < roomList[roomToConnect].yLocation:
							startingY = k.yLocation
							endingY = roomList[roomToConnect].yLocation
						else :
							startingY = roomList[roomToConnect].yLocation
							endingY = k.yLocation
						xChange = 0
						yChange = 0
						for l in range(0, endingX - startingX + endingY - startingY):
							direction = randint(0,1)
							if (endingX - startingX > xChange):
								xChange = xChange + 1
							else:
								yChange = yChange + 1
							map[startingY + yChange][startingX + xChange] = 0
							
		for k in roomList:
			if (k.connectedToMainRoom == False):
				roomToConnect = mainRoom
				k.connectedToMainRoom = True
				startingX = 0
				startingY = 0
				endingX = 0
				endingY = 0
				if k.xLocation < roomList[roomToConnect].xLocation:
					startingX = k.xLocation
					endingX = roomList[roomToConnect].xLocation
				else:
					startingX = roomList[roomToConnect].xLocation
					endingX = k.xLocation
				if k.yLocation < roomList[roomToConnect].yLocation:
					startingY = k.yLocation
					endingY = roomList[roomToConnect].yLocation
				else :
					startingY = roomList[roomToConnect].yLocation
					endingY = k.yLocation
				xChange = 0
				yChange = 0
				for l in range(0, endingX - startingX + endingY - startingY):
					direction = randint(0,1)
					if (endingX - startingX > xChange):
						xChange = xChange + 1
					else:
						yChange = yChange + 1
					map[startingY + yChange][startingX + xChange] = 0
		
		return map
	
	def dungeofy(self, map, dungeonRow, dungeonCol): 
		dungeonLayout = [[" " for i in range(dungeonCol)] for j in range(dungeonRow)] 
		dungeonString = "" 
		for i in range(dungeonRow): 
			for j in range(dungeonCol): 
				if (map[i][j] == 1): 
					dungeonLayout[i][j] = "#" 
				if (map[i][j] == 2):
					dungeonLayout[i][j] = "e"
				if (map[i][j] == 3):
					dungeonLayout[i][j] = "t"
				if (map[i][j] == 4):
					dungeonLayout[i][j] = "f"
				dungeonString += dungeonLayout[i][j] 
			dungeonString += '\n' 
		return dungeonString
		
	def populateDungeon(self, map, dungeonRow, dungeonCol):
		encounters = 0
		for i in range(dungeonRow):
			for j in range(dungeonCol):
				if (map[i][j] == 0):
					populateRNG = randint(0, 100)
					if (populateRNG == 99): #Hostile Encounter
						map[i][j] = 2
						enncounters = encounters + 1
					elif (populateRNG == 98): #Treasure
						map[i][j] = 3
					elif (populateRNG == 97):  #Furniture
						map[i][j] = 4;
		return map;
						
	def generateCave(self, map):
		for i in range(self.initializationPass): 
			for j in range (self.dungeonRow): 
				for k in range (self.dungeonCol): 
					if (randint(1, 100) == 1): 
						map[j][k] = 0 
	
		for i in range(self.carvingPass): 
			for j in range(self.dungeonRow): 
				for k in range(self.dungeonCol): 		 
					if (map[j][k] == 1 and j > 0 and j < self.dungeonRow - 1 and k > 0 and k < self.dungeonCol - 1): 
						if ((map[j-1][k] == 0 and map[j+1][k] == 0) or (map[j][k-1] == 0 and map[j][k+1] == 0)): 
							map[j][k] = 0

					if (map[j][k] == 0):  
						xChange = randint(-1,1) 
						yChange = randint(-1,1) 
						if (j+xChange > 0 and j+xChange < self.dungeonRow and k+yChange > 0 and k +yChange < self.dungeonCol): 
							map[j+xChange][k+yChange] = 0 
		return map
	