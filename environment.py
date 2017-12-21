from random import randint 

class environment(object): 
	
	def __init__(self, row, col, initPass, carvePass):
		self.dungeonRow = int(row)
		self.dungeonCol = int(col)
		dungeonMap = [[1 for i in range(self.dungeonCol)] for j in range(self.dungeonRow)] 
		self.initializationPass = int(initPass)
		self.carvingPass = int(carvePass)
		for i in range(self.initializationPass): 
			for j in range (self.dungeonRow): 
				for k in range (self.dungeonCol): 
					if (randint(1, 100) == 1): 
						dungeonMap[j][k] = 0 

		for i in range(self.carvingPass): 
			for j in range(self.dungeonRow): 
				for k in range(self.dungeonCol): 		 
					if (dungeonMap[j][k] == 1 and j > 0 and j < self.dungeonRow - 1 and k > 0 and k < self.dungeonCol - 1): 
						if ((dungeonMap[j-1][k] == 0 and dungeonMap[j+1][k] == 0) or (dungeonMap[j][k-1] == 0 and dungeonMap[j][k+1] == 0)): 
							dungeonMap[j][k] = 0

					if (dungeonMap[j][k] == 0):  
						xChange = randint(-1,1) 
						yChange = randint(-1,1) 
						if (j+xChange > 0 and j+xChange < self.dungeonRow and k+yChange > 0 and k +yChange < self.dungeonCol): 
							dungeonMap[j+xChange][k+yChange] = 0 
		self.dungeonLayout = self.dungeofy(dungeonMap, self.dungeonRow, self.dungeonCol) 
 
	def dungeofy(self, map, dungeonRow, dungeonCol): 
		dungeonLayout = [[" " for i in range(dungeonCol)] for j in range(dungeonRow)] 
		dungeonString = "" 
		for i in range(dungeonRow): 
			for j in range(dungeonCol): 
				if (map[i][j] == 1): 
					dungeonLayout[i][j] = "#" 
				dungeonString += dungeonLayout[i][j] 
			dungeonString += '\n' 
		return dungeonString