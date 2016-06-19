from setup.scene import Scene
from random import randint

class Death(Scene):

    death_scene = [
        "You are now dead. At least your debts have been paid in full.",
        "You are no longer alive. Great shame upon House Lannister.",
        "You died. Honestly, it's quite surprising you made it this far."
        "You are now deceased. Somewhere in King's Landing, \nyour cruel sister Cersei is laughing.",
    ]

    def enter(self):
        print Death.death_scene[randint(0,len(self.death_scene)-1)]
        print "\n"
        print "-|" * 20
        print "\n"
        print "Would you like to play again? (y/n)"

        play_again = raw_input("> ")
        play_again = play_again.lower()

        if play_again == "y":
            return 'introduction'
        elif play_again == "n":
            print "\n"
            print "Seven blessings to you."
            print "\n"
            print "\"In the game of thrones, you either win or you die.\""
            print "-Cersei Lannister"
            print "\n"
            exit(1)
        else:
            print "Sorry, I do not understand."
            current_scene.enter()
