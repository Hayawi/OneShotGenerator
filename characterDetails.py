from random import randint
import requests
import json
from characterSheet import characterSheet as cSheet

class characterDetails(object):

		c = cSheet()	
		bBond = "Character Details/" + c.charBackground  + "/Bond.txt"
		bIdeal = "Character Details/" + c.charBackground + "/Ideal.txt"
		bFlaw = "Character Details/" + c.charBackground + "/Flaw.txt"
		bPersonality = "Character Details/" + c.charBackground + "/Personality Trait.txt"
		bond = open(bBond, "r")
		ideal = open(bIdeal, "r")
		flaw = open(bFlaw, "r")
		personalityTrait = open(bPersonality, "r")
		
		bLine = bond.readlines()
		characterBond = bLine[randint(1,6) - 1]

		iLine = ideal.readlines()
		characterIdeal = iLine[randint(1,6) - 1]

		fLine = flaw.readlines()
		characterFlaw = fLine[randint(1,6) - 1]

		pLine = personalityTrait.readlines()
		characterPersonality = pLine[randint(1,8) - 1]

		print characterBond
		print characterFlaw
		print characterIdeal
		print characterPersonality
		
		