from flask import Flask, render_template
from random import randint
from faker import Faker

app = Flask(__name__)


@app.route('/')
def main():
    abilityAverage = 0
    fake = Faker()
    # Prevent the overall ability average from being less than 12
    while (abilityAverage < 12):
			sMin = min(strengthScore4Dice) # smallest dice
			strengthScore = strengthScore4Dice[0] + strengthScore4Dice[1] + strengthScore4Dice[2] +strengthScore4Dice[3] - sMin;
		
			dexterityScore4Dice = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
			dMin = min(dexterityScore4Dice)
			dexterityScore = dexterityScore4Dice[0] + dexterityScore4Dice[1] + dexterityScore4Dice[2] +dexterityScore4Dice[3] - dMin;
		
			constitutionScore4Dice = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
			cMin = min(constitutionScore4Dice)
			constitutionScore = constitutionScore4Dice[0] + constitutionScore4Dice[1] + constitutionScore4Dice[2] +constitutionScore4Dice[3] -cMin;
		
			wisdomScore4Dice = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
			wMin = min(wisdomScore4Dice)
			wisdomScore = wisdomScore4Dice[0] + wisdomScore4Dice[1] + wisdomScore4Dice[2] + wisdomScore4Dice[3] -wMin;
		
			intelligenceScore4Dice = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
			iMin = min(intelligenceScore4Dice)
			intelligenceScore = intelligenceScore4Dice[0] + intelligenceScore4Dice[1] + intelligenceScore4Dice[2] + intelligenceScore4Dice[3] -iMin;
		
			charismaScore4Dice = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
			cMin = min(charismaScore4Dice)
			charismaScore = charismaScore4Dice[0] + charismaScore4Dice[1] + charismaScore4Dice[2] + charismaScore4Dice[3] -cMin;
		
        
       
        
        
        
			abilityAverage = (strengthScore + dexterityScore + constitutionScore + wisdomScore + intelligenceScore + charismaScore)/6

    return render_template('index.html',
                           charname=fake.name(),
                           Strengthscore = strengthScore,
                           Dexterityscore = dexterityScore,
                           Constitutionscore = constitutionScore,
                           Wisdomscore = wisdomScore,
                           Intelligencescore = intelligenceScore,
                           Charismascore = charismaScore,
                           Strengthmod=getAbilityModifier(strengthScore),
                           Dexteritymod = getAbilityModifier(dexterityScore),
                           Constitutionmod = getAbilityModifier(constitutionScore),
                           Wisdommod = getAbilityModifier(wisdomScore),
                           Intelligencemod = getAbilityModifier(intelligenceScore),
                           Charismamod = getAbilityModifier(charismaScore))

def getAbilityModifier(mod):
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

if __name__ == '__main__':
    app.run()
