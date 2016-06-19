from setup.scene import Scene

class Success(Scene):

    def enter(self):
        print "-|" * 20
        print "\n"
        print "CONGRATULATIONS!"
        print "You have won the game! But have you beaten... 'The Game'?"
        print "Until next time..."
        print "\n"
        exit(1)
