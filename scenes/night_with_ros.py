from setup.scene import Scene

class NightWithRos(Scene):
# where Tyrion has a night with Ros but gets interrupted
    def enter(self):
        print "\n"
        print "Ros blushes at the audacity of your choice."
        print "\n"
        print "Ros: \"Lord Tyrion, you flatter me. However, I cannot abide."
        print "I'm afraid the madam of the house is not for sale.\""
        print "\n"
        print "You: \"Everything's for sale, milady. Especially when you're a Lannister.\""
        print "\n"
        raw_input("Press ENTER to continue...")

        print "\n"
        print "You throw an additional bag of gold on the table. Ros' eyes widen."
        print "\n"
        print "Ros: \"Very well, milord. Please come with me.\""
        print "\n"
        print "You walk with raised anticipation to a private room with Ros. As she undresses"
        print "in front of you, you feel a swell of excitement and pour more wine."
        print "\n"
        raw_input("Press ENTER to continue...")

        print "\n"
        print "BOOM! Your brother JAIME storms into the room. Perfect timing as always."
        print "\n"
        print "Jaime: \"Forgive me, little brother. Pressing matters at hand.\""
        print "\n"
        print "You: \"You are certainly not forgiven. What could it be, Ser Jaime?\""
        print "\n"
        print "Jaime: \"You've been asked to join the party heading to The Wall.\""
        print "\n"
        raw_input("Press ENTER to continue...")

        print "\n"
        print "You: \"And what would I be doing at The Wall?\""
        print "\n"
        print "Jaime: \"Meet with the Night's Watch. Provide a full report to the"
        print "Small Council upon your return to King's Landing.\""
        print "\n"
        print "You sigh and begin to gather your clothes. Ros looks back at you, confused."
        print "\n"
        print "You (to Ros): \"And now my watch begins....\""
        print "\n"
        
        raw_input("Press ENTER to continue")
        return 'the_wall'
