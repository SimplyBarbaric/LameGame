__author__ = 'Chris'
from Character import *


class BasicPlayerCharacter(Character):

    attackList={"attack1":  "Lame Punch","attack2":  "The Fleeing Rat","attack3":  "The Royale with Cheese","attack4":  "Black Hole"}

    def setDefaults(self):
        #default gaining 100 every level
        self.fullHealth = 150 * self.level
        #gain 30 of every stat every level
        self.fullAttackPower = 40 * self.level
        self.fullMagicPower = 30 * self.level
        self.fullDefense = 30 * self.level

    def attack1(self, opponent):
        print ("You punch "+ str(opponent.name) +" with your puny human hands\n" )

        damageValue = opponent.damageHealth(self.attackPower)

        print ("You deal "+str(damageValue)+" damage, leaving "+str(opponent.name)+" with "+str(opponent.health)+" health\n")

    def attack2(self, opponent):
        if self.level < 2:
            print ("You are still too weak to use a second attack")
        else:
            print ("You savagely claw at "+ str(opponent.name) + "'s eyes with your cracked fingernails\n" )

            damageValue = opponent.damageHealth(self.attackPower * (3/4))
            opponentAttack = opponent.reduceAttack(self.magicPower /4)

            print ("You deal "+str(damageValue)+" damage and reduce "+str(opponent.name)+"'s attack to "+str(opponentAttack)+", leaving them with "+str(opponent.health)+" health\n")

    def attack3(self, opponent):
        if self.level < 3:
            print ("You are still too weak to use a third attack")
        else:
            pass

    def attack4(self, opponent):
        if self.level < 4:
            print ("You are still too weak to use a fourth attack")
        else:
            pass

    def secretAttack(self, opponent):
        print ("You cheat and bring a knife to a fistfight.")
        opponent.damageHealth(opponent.health + (1/2) * opponent.defense);
        print ("You stab "+str(opponent.name)+" and kill them instantly.")

    def sayQuote(self):
        print ("\"I AM THE GREATEST\"-you")

    def sayVictoryQuote(self):
        print ("\"WHO'S NEXT?!-you\"")

    def sayDefeatQuote(self):
        print ("\"Oh bother...\"-you")
