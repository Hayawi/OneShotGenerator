from flask import Flask, render_template
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
                                classlevel = c.charClass + ' ' + str(c.charLevel),
                                race = c.charRace,
                                background = c.charBackground,
                                alignment = c.charAlignment,
                                personality = c.charPersonality,
                                ideals = c.charIdeal,
                                bonds = c.charBond,
                                flaws = c.charFlaw,
                                speed = c.charSpeed + 'ft',
                                strengthSaveProf = c.strSavingThrwProf,
                                dexteritySaveProf= c.dexSavingThrwProf,
                                constitutionSaveProf= c.conSavingThrwProf,
                                wisdomSaveProf= c.wisSavingThrwProf,
                                intelligenceSaveProf= c.intSavingThrwProf,
                                charismaSaveProf= c.chaSavingThrwProf,
                                proficiencybonus = c.getStringInteger(c.charProficiencyBonus),
                                strengthSave = c.getStringInteger(c.strSavingThrw),
                                dexteritySave = c.getStringInteger(c.dexSavingThrw),
                                constitutionSave = c.getStringInteger(c.conSavingThrw),
                                wisdomSave = c.getStringInteger(c.wisSavingThrw),
                                intelligenceSave = c.getStringInteger(c.intSavingThrw),
                                charismaSave = c.getStringInteger(c.chaSavingThrw),
                                totalhd = str(c.charLevel) + "d" + str(c.maxHitDie),
                                maxhp = c.maxHP,
                                passiveperception = c.passiveWisdom)

@app.route('/dungeon')
def creatDungeon():
	createdDungeon = environment()
	return render_template('home.html', dungeon=createdDungeon.dungeonLayout)

if __name__ == '__main__':
    app.run()