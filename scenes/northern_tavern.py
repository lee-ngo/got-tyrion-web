from setup.scene import Scene

class NorthernTavern(Scene):
# where Tyrion gets arrested
    def enter(self):
        print "Bronn is a sellsword with excellent combat skills, and"
        print "he's not at all adverse to taking Lannister coin."
        print "\n"
        print "Bronn: \"Forgive me, Lord Tyrion, but you've been summoned"
        print "back to King's Landing. I'll personally escort you.\""
        print "\n"
        print "You: \"Very well. Apparently, 'winter is coming' anyway."
        print "Might as well get a head start.\""
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "A few days later, you and Bronn decided to stop in a tavern"
        print "on the road back to King's Landing. As you enter, the"
        print "predominantly Northern clientele sneer at your Southern"
        print "demeanor and blonde hair."
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "Not long after you, CATELYN STARK enters the tavern. A rare"
        print "sight to see such a familiar noblewoman in an establishment"
        print "such as this. She immediately locks eyes on you as you and Bronn"
        print "have already found a place to sit."
        print "\n"
        print "Cat: \"You. I have searched every tavern and brothel within"
        print "100 miles of Winterfell for you.\""
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "You: \"Good day, Lady Catelyn. It seems you have an educated"
        print "approach to tracking me down. How may I help you?\""
        print "\n"
        print "Your noble pleasantries are not matched. Cat begins to wander"
        print "the room, eyeing the other Northerners with sheathed swords."
        print "\n"
        print "Cat: \"Warriors of the North. Descendants of the First Men."
        print "You have all served under the banner of Stark for centuries"
        print "with honor and dignity, have you not?\""
        print "\n"
        print "The armed men cheer and pound their tankards in solidarity."
        print "You feel a sudden perspiration collect on your brow."
        print "\n"
        print "Cat: (pointing at you) \"This man has conspired against House"
        print "Stark! To kill my son! Bannermen, arrest Tyrion Lannister!\""
        print "\n"
        print "Do you YIELD to the arrest or summon Bronn to FIGHT back?"

        choice = raw_input("> ")
        choice = choice.lower()

        if choice == "yield":
            return 'the_vale'
        else:
            print "Bronn looks back at you. \"You're on your own, little man.\""
            print "Bronn leaps out of one of the windows and rides away."
            print "\n"
            print "In an act of desperation, you lunge at Cat Stark, but"
            print "your feeble attempt to take her hostage is thwarted by"
            print "dozens of Northern-forged steel backed by the fury of"
            print "the old gods. You fail to make it out of the tavern alive."
            print "\n"
            return 'death'
