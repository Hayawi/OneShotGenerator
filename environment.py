from random import randint 

class environment(object): 
	
	def __init__(self):
		dungeonRow = 30
		dungeonCol = 60
		dungeonMap = [[1 for i in range(dungeonCol)] for j in range(dungeonRow)] 
		initializationPass = 3 
		carvingPass = 6
		for i in range(initializationPass): 
			for j in range (dungeonRow): 
				for k in range (dungeonCol): 
					if (randint(1, 100) == 1): 
						dungeonMap[j][k] = 0 

		for i in range(carvingPass): 
			for j in range(dungeonRow): 
				for k in range(dungeonCol): 		 
					if (dungeonMap[j][k] == 1 and j > 0 and j < dungeonRow - 1 and k > 0 and k < dungeonCol - 1): 
						if ((dungeonMap[j-1][k] == 0 and dungeonMap[j+1][k] == 0) or (dungeonMap[j][k-1] == 0 and dungeonMap[j][k+1] == 0)): 
							dungeonMap[j][k] = 0

					if (dungeonMap[j][k] == 0):  
						xChange = randint(-1,1) 
						yChange = randint(-1,1) 
						if (j+xChange > 0 and j+xChange < dungeonRow and k+yChange > 0 and k +yChange < dungeonCol): 
							dungeonMap[j+xChange][k+yChange] = 0 
		self.dungeonLayout = self.dungeofy(dungeonMap, dungeonRow, dungeonCol) 
 
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