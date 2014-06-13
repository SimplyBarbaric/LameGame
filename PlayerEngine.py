__author__ = 'Chris'
from CharacterEngine import *



class PlayerEngine(CharacterEngine):
    def play(self, command, player, opponent):
        #first, interpret the command


        #Determine if the command is valid (python has no switch statement)
        if command.lower() == 'attack1':
            return self.attack1(player, opponent)
        elif command.lower() == 'attack2':
            return self.attack2(player, opponent)
        elif command.lower() == 'attack3':
            return self.attack3(player, opponent)
        elif command.lower() == 'attack4':
            return self.attack4(player, opponent)
        elif command.lower() == 'taunt':
            self.taunt(player)
        elif command.lower() == 'status':
            self.status(player)
        elif command.lower() == 'opponent status':
            self.status(opponent)
        elif command.lower() == 'secret attack':
            return self.secretAttack(player, opponent)
        else:
            #print an error
            print("Command not recognized\n")
            self.help()

        return False



    def attack1(self, player, opponent):
        player.attack1(opponent)
        return self.endTurn(player, opponent)

    def attack2(self, player, opponent):
        player.attack2(opponent)
        return self.endTurn(player, opponent)

    def attack3(self, player, opponent):
        player.attack3(opponent)
        return self.endTurn(player, opponent)

    def attack4(self, player, opponent):
        player.attack4(opponent)
        return self.endTurn(player, opponent)

    def secretAttack(self, player, opponent):
        player.secretAttack(opponent)
        return self.endTurn(player, opponent)

    def taunt(self, player):
        player.sayQuote()

    def status(self, player):
        player.status()

    def endTurn(self, player, opponent):
        if(opponent.health <= 0):
            opponent.sayDefeatQuote()
            player.sayVictoryQuote()
            print(str(opponent.name)+" defeated! You level up!")
            player.levelUp()
            return True
        else:
            #true means that the opponent killed you otherwise he just attacked
            if opponent.play("attack",  player):
                opponent.sayVictoryQuote()
                player.sayDefeatQuote()
                print("You lose!, better luck next time!\n")
                player.resetToDefaults()
                opponent.resetToDefaults()
                opponent.sayIntroQuote()
                print("...again\n")
            return False

    def help(self):
        print("Possible commands:\nattack1\nattack2\nattack3\nattack4\ntaunt\nstatus\nopponent status\nexit\n")