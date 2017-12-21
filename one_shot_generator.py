from flask import Flask, render_template
from characterSheet import characterSheet as cSheet

app = Flask(__name__)

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
                           Charismamod = c.charismaMod)
if __name__ == '__main__':
    app.run()