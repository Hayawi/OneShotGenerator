from flask import Flask, render_template
from random import randint

app = Flask(__name__)


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

if __name__ == '__main__':
    app.run()
