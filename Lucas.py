__author__ = 'Chris'
from Character import *


class Lucas(Character):

    def setDefaults(self):
        #default gaining 100 every level
        self.fullHealth = 110 * self.level
        #gain 30 of every stat every level
        self.fullAttackPower = 30 * self.level
        self.fullMagicPower = 20 * self.level
        self.fullDefense = 20 * self.level

    def attack1(self, opponent):
        print(""+str(self.name)+" complains loudly at "+str(opponent.name)+"\n")
        damageDefenseValue = opponent.reduceDefense((self.magicPower/5))
        print("He reduces "+str(opponent.name)+"'s defense/patience by "+str(damageDefenseValue)+"\n")

    def attack2(self, opponent):
        print (""+str(self.name)+" karate chops "+str(opponent.name)+"\n")
        damageValue = opponent.damageHealth(self.attackPower)
        print (""+str(self.name)+" deals "+str(damageValue)+" damage, leaving "+str(opponent.name)+" with "+str(opponent.health)+" health\n")

    def attack3(self, opponent):
        print (""+str(self.name)+" sleeps til 4 pm\n")
        self.heal(self.magicPower)
        self.reduceDefense(5 * self.level)
        print (""+str(self.name)+" heals for "+str(self.magicPower)+" health but decreases his defense by "+str( (self.level * 5) )+" \n")

    def attack4(self, opponent):
        print (""+str(self.name)+" does a flying kick! \n")
        damageValue = opponent.damageHealth((self.attackPower - (10 * self.level)))
        self.attackPower += 6 * self.level;
        print (""+str(self.name)+" deals "+str(damageValue)+" damage, leaving "+str(opponent.name)+" with "+str(opponent.health)+" health\n He also increases his attack power by "+str((6 * self.level))+"")

    def secretAttack(self, opponent):
        print ("You cheat and change the source code")
        self.level = 9
        self.levelUp()
        print ("You are now level 10. Congrats.")

    def sayQuote(self):
        print ("\"f-words\"-Lucas")

    def sayVictoryQuote(self):
        print ("\"VICTORY SCREECH!\"-Lucas")

    def sayDefeatQuote(self):
        print ("\"That's it, I'm walking home\"-Lucas\n (CHEAT CODE UNLOCKED: \"LucasArts\")")

    def sayIntroQuote(self):
        print ("Lucas just shows up out of nowhere! Prepare to fight!")
