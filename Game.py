__author__ = 'Chris'

from BasicPlayerCharacter import *
from Lucas import *
from Travis import *
from PlayerEngine import *
from NPCEngine import *


def main():
    print("Who the hell are you?\n")
    name = input("> ")

    #Determine if a code has been entered and act accordingly (no switches in python
    if name == "LucasArts":
        print ("Lucas cheat code detected.\n")
        you = Lucas("Good Lucas", PlayerEngine(), 1)
    elif name == "Larson":
        print ("Travis cheat code detected.\n")
        you = Travis("Good Travis", PlayerEngine(), 1)
    else:
        #use the default
        you = BasicPlayerCharacter(name,PlayerEngine(),1)

    #instantiate the baddies in an array list of some kind
    baddies = [Lucas("Lucas" ,NPCEngine(),1), Travis("Travis" ,NPCEngine(),2)]

    #main loop
    done = False
    for npc in baddies:
        #loop for battle 1
        victorious = False
        npc.sayIntroQuote()

        while not victorious and not done:
            command = input("> ")
            if command.lower() == "exit":
                done = True
            else:
                victorious = you.play(command, npc)
        if done:
            print("Game Over")
            break

    if not done:
        print ("BIG WINNER!")


if __name__ == "__main__":
        main()
