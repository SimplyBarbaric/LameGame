__author__ = 'Chris'
from random import random, randint


class NPCEngine(object):
    def play(self,command, player, opponent):
        if command.lower() == 'attack':
            self.attack(player, opponent)
            return self.endTurn(player, opponent)

        else:
            #do nothing if command is invalid
            pass

    def attack(self, player, opponent):
        #could add more advanced AI later, for now use random
        attackNumber = randint(1, 4)
        if attackNumber == 1:
            player.attack1(opponent)
        elif attackNumber == 2:
            player.attack2(opponent)
        elif attackNumber == 3:
            player.attack3(opponent)
        else:
            player.attack4(opponent)

    def endTurn(self, player, opponent):
        return opponent.health <= 0