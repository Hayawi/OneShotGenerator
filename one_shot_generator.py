from flask import Flask, render_template
from random import randint

app = Flask(__name__)
app.debug = 'true'

@app.route('/')
def main():
    Abilityaverage = 0

    # Prevent the overall ability average from being less than 12
    while (Abilityaverage < 12):
        Strengthscore = randint(3,18)
        Dexterityscore = randint(3,18)
        Constitutionscore = randint(3,18)
        Wisdomscore = randint(3,18)
        Intelligencescore = randint(3,18)
        Charismascore = randint(3,18)
        Abilityaverage = (Strengthscore + Dexterityscore + Constitutionscore + Wisdomscore + Intelligencescore + Charismascore)/6
    return render_template('index.html',
        charname="Kevin",
        Strengthscore = Strengthscore,
        Dexterityscore = Dexterityscore,
        Constitutionscore = Constitutionscore,
        Wisdomscore = Wisdomscore,
        Intelligencescore = Intelligencescore,
        Charismascore = Charismascore,
        Strengthmod=get_ability_modifier(Strengthscore),
        Dexteritymod = get_ability_modifier(Dexterityscore),
        Constitutionmod = get_ability_modifier(Constitutionscore),
        Wisdommod = get_ability_modifier(Wisdomscore),
        Intelligencemod = get_ability_modifier(Intelligencescore),
        Charismamod = get_ability_modifier(Charismascore))

def get_ability_modifier(mod):
    return {
        3: '-4',
        4: '-3',
        5: '-3',
        6: '-2',
        7: '-2',
        8: '-1',
        9: '-1',
        10: '0',
        11: '0',
        12: '+1',
        13: '+1',
        14: '+2',
        15: '+2',
        16: '+3',
        17: '+3',
        18: '+4'
    }.get(mod, '0')

@app.route('/dungeon')
def dungeon_generator():
	dungeonRow = 50
	dungeonCol = 100
	dungeonMap = [[1 for i in range(dungeonCol)] for j in range(dungeonRow)]
	initializationPass = 1
	carvingPass = 9
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
						dungeonMap[j][k] = 0;
						
				if (dungeonMap[j][k] == 0):
					xChange = randint(-1,1)
					yChange = randint(-1,1)
					if (j+xChange > 0 and j+xChange < dungeonRow and k+yChange > 0 and k +yChange < dungeonCol):
						dungeonMap[j+xChange][k+yChange] = 0					
	
	dungeonLayout = dungeofy(dungeonMap, dungeonRow, dungeonCol)
	return render_template('home.html', dungeon=dungeonLayout)
	
def dungeofy(map, dungeonRow, dungeonCol):
	dungeonLayout = [[" " for i in range(dungeonCol)] for j in range(dungeonRow)]
	dungeonString = ''
	for i in range(dungeonRow):
		for j in range(dungeonCol):
			if (map[i][j] == 1):
				dungeonLayout[i][j] = "#"
			dungeonString += dungeonLayout[i][j]
		dungeonString += '\n'
	return dungeonString

if __name__ == '__main__':
    app.run()
