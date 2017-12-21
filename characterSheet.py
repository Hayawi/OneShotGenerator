from random import randint
from faker import Faker

class characterSheet(object):

    def __init__(self):
        abilityAverage = 0
        fake = Faker()
        self.name = fake.name()
        # Prevent the overall ability average from being less than 12
        while abilityAverage < 12:
            strengthScore4Dice = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
            sMin = min(strengthScore4Dice) # smallest dice
            self.strengthScore = strengthScore4Dice[0] + strengthScore4Dice[1] + strengthScore4Dice[2] +strengthScore4Dice[3] - sMin

            dexterityScore4Dice = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
            dMin = min(dexterityScore4Dice)
            self.dexterityScore = dexterityScore4Dice[0] + dexterityScore4Dice[1] + dexterityScore4Dice[2] +dexterityScore4Dice[3] - dMin

            constitutionScore4Dice = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
            cMin = min(constitutionScore4Dice)
            self.constitutionScore = constitutionScore4Dice[0] + constitutionScore4Dice[1] + constitutionScore4Dice[2] +constitutionScore4Dice[3] -cMin

            wisdomScore4Dice = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
            wMin = min(wisdomScore4Dice)
            self.wisdomScore = wisdomScore4Dice[0] + wisdomScore4Dice[1] + wisdomScore4Dice[2] + wisdomScore4Dice[3] -wMin

            intelligenceScore4Dice = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
            iMin = min(intelligenceScore4Dice)
            self.intelligenceScore = intelligenceScore4Dice[0] + intelligenceScore4Dice[1] + intelligenceScore4Dice[2] + intelligenceScore4Dice[3] -iMin

            charismaScore4Dice = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
            cMin = min(charismaScore4Dice)
            self.charismaScore = charismaScore4Dice[0] + charismaScore4Dice[1] + charismaScore4Dice[2] + charismaScore4Dice[3] -cMin

            abilityAverage = (self.strengthScore + self.dexterityScore + self.constitutionScore + self.wisdomScore + self.intelligenceScore + self.charismaScore)/6

        self.strengthMod = self.getAbilityModifier(self.strengthScore)
        self.dexterityMod = self.getAbilityModifier(self.dexterityScore)
        self.constitutionMod = self.getAbilityModifier(self.constitutionScore)
        self.wisdomMod = self.getAbilityModifier(self.wisdomScore)
        self.intelligenceMod = self.getAbilityModifier(self.intelligenceScore)
        self.charismaMod = self.getAbilityModifier(self.charismaScore)

    def getAbilityModifier(self, mod):
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