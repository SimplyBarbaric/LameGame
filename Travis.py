__author__ = 'Chris'
from Character import *
from random import random, randint

class Travis(Character):

    def setDefaults(self):
        #default gaining 100 every level
        self.fullHealth = 120 * self.level
        #gain 30 of every stat every level
        self.fullAttackPower = 25 * self.level
        self.fullMagicPower = 30 * self.level
        self.fullDefense = 20 * self.level

    def attack1(self, opponent):
        print(""+str(self.name)+" is abrasive!\n")

        damageDefenseValue = opponent.damageHealth((self.attackPower))

        print("He deals "+str(damageDefenseValue)+" damage to "+str(opponent.name)+"\n")

    def attack2(self, opponent):
        print (""+str(self.name)+" throws sand in "+str(opponent.name)+"'s eyes!\n")

        attackReduction = opponent.reduceAttack(self.magicPower /5)
        defenseReduction = opponent.reduceDefense(self.magicPower /5)

        print (""+str(self.name)+" reduces "+str(opponent.name)+"'s attack to "+str(attackReduction)+" and defence to "+str(defenseReduction)+"\n")

    def attack3(self, opponent):
        print (""+str(self.name)+" buries himself in sand!?\n")

        self.defense = self.fullDefense + (10* self.level);
        attackReduction = self.reduceAttack(self.magicPower /10)
        self.reduceMagic(attackReduction)

        print (""+str(self.name)+" returns increases is defense at the cost of reducing both his attack and magic by "+str(self.magicPower /10)+"!\n")

    def attack4(self, opponent):
        print (""+str(self.name)+" plays Wii Party U! \n")

        diceResult = randint(1, 6)
        damageValue = opponent.damageHealth(((self.attackPower)*(diceResult)) /4)

        print ("...and the resulting dice roll lands on ("+str(diceResult)+" meaning he does "+str(damageValue)+" damage")

    def secretAttack(self, opponent):
        print ("You cheat and punch your opponent in the junk")
        opponent.reduceAttack(opponent.attackPower)
        opponent.reduceMagic(opponent.magicPower)
        opponent.reduceDefense(opponent.defense)
        print ("Your opponent's attack, defense, and magic are all reduced to zero")

    def sayQuote(self):
        print ("\"Get good or get wrecked!\"-Travis")

    def sayVictoryQuote(self):
        print ("\"I'm never wrong!\"-Travis")

    def sayDefeatQuote(self):
        print ("\"THE ANGLES MAN! THE ANGLES!\"-Travis")

    def sayIntroQuote(self):
        print (""+str(self.name)+" just climbed out of the sewers! Prepare to fight!")
