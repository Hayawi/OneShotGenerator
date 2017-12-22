from flask import Flask, render_template, request
from characterSheet import characterSheet as cSheet
from environment import environment

app = Flask(__name__)
app.debug = 'true'

@app.route('/')
def main():
    c = cSheet()
    return render_template('index.html',
                               charname=c.name,
                               Strengthscore = c.strengthScore,
                               Dexterityscore = c.dexterityScore,
                               Constitutionscore = c.constitutionScore,
                               Wisdomscore = c.wisdomScore,
                               Intelligencescore = c.intelligenceScore,
                               Charismascore = c.charismaScore,
                               Strengthmod=c.strengthMod,
                               Dexteritymod = c.dexterityMod,
                               Constitutionmod = c.constitutionMod,
                               Wisdommod = c.wisdomMod,
                               Intelligencemod = c.intelligenceMod,
                               Charismamod = c.charismaMod,
                               classlevel = c.charClass)
							   
@app.route('/dungeon')
def createDungeon():
	return render_template('home.html', initPassVal="5", carvePassVal="3", colVal="60", rowVal="30", numberOfRooms="5")

@app.route('/dungeon', methods=['POST'])
def createDungeonPost():
	createdDungeon = environment(request.form['row'], request.form['column'], request.form['InitPass'], request.form['CarvePass'], request.form['rooms'])
	return render_template('home.html', generatedText="The generated dungeon is:", numberOfRooms=createdDungeon.rooms, dungeon=createdDungeon.dungeonLayout, initPassVal=createdDungeon.initializationPass, carvePassVal=createdDungeon.carvingPass, colVal=createdDungeon.dungeonCol, rowVal=createdDungeon.dungeonRow)

if __name__ == '__main__':
    app.run()