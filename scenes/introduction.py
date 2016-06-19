from setup.scene import Scene # do i have to do this every time?

class Introduction(Scene):

    def enter(self):
        print "-|" * 20
        print "\n"
        print "Welcome to this Game of Thrones text adventure!"
        print "In this game, you are TYRION LANNISTER,"
        print "a man blessed with wealth and education,"
        print "which mitigates your dwarfish appearance"
        print "and overindulgent demeanor."
        print "\n"
        print "When playing this game, your options are provided in CAPS."
        print "Type in your choice precisely to advance."
        print "\n"
        raw_input("Press ENTER to continue...")
        return 'winterfell'
