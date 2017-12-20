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
        strengthScore = randint(3,18)
        dexterityScore = randint(3,18)
        constitutionScore = randint(3,18)
        wisdomScore = randint(3,18)
        intelligenceScore = randint(3,18)
        charismaScore = randint(3,18)
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
