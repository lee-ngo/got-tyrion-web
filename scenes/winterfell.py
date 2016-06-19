from setup.scene import Scene

class Winterfell(Scene):
# Winter is coming...
    def enter(self):
        print "\n"
        print "You begin your journey riding with your family"
        print "and in-laws to Winterfell,"
        print "your first time traveling to the North part of Westeros."
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"
        print "You ride up to Winterfell, the keep that maintains order"
        print "in the North for centuries."
        print "The frigid air does not suit you, and you feel"
        print "a tingling in your loins."
        print "\n"
        print "Do you talk to JON SNOW and head with him to The Wall,"
        print "Or do you go to a BROTHEL to ease your troubled mind?"
        print "\n"
        choice = raw_input("> ")
        choice.lower()

        if choice == "jon snow":
            return 'the_wall'
        elif choice == 'brothel':
            return 'northern_brothel'
        else:
            print "Don't give me that sass."
            return 'winterfell'
