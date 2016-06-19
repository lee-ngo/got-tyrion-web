from setup.scene import Scene

class NorthernBrothel(Scene):
# a PG-13 depicted pit stop
    def enter(self):
        print "\n"
        print "Ah, there's nothing quite like a brothel! While not up to the standards"
        print "of a Petyr 'Littlefinger' Baelish establishment, the charm of the Northern"
        print "women is enough to thaw the frost you've been feeling since you've arrived."
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"
        print "The madam of the establishment, ROS, walks out in a flowing robe that"
        print "leaves very little to the imagination. She claps her hands and a row of"
        print "young maidens walks into the main room, one more beautiful than the last."

        print "\n"
        print "Ros: \"Lord Tyrion, welcome! Which of these fine ladies do you choose?\""
        print "\n"
        print "Do you select ROS or a RANDOM woman?"
        print "\n"
        choice = raw_input("> ")
        choice.lower()

        if choice == "ros":
            return 'night_with_ros'
        elif choice == "random":
            print "\n"
            print "Ros: \"Excellent choice, Lord Tyrion.\""
            print "\n"
            print "A young maiden escorts you to one of their finest rooms."
            print "Before you remove your clothes, however, the maiden pulls"
            print "a dagger and slits your throat!"
            print "\n"

            raw_input("Press ENTER to continue...")
            print "\n"
            print "Before taking all of your gold, she looks down upon your"
            print "slowly draining corpse and smiles wickedly."
            print "\n"
            print "Woman: \"A Lannister always pays his debts.\""
            print "\n"
            print "Turns out you choose the one woman who had a score to settle"
            print "with your family a long time ago."
            print "\n"

            raw_input("Press ENTER to continue...")
            print "\n"
            return 'death'
        else:
            print "Don't give me that sass."
            return 'northern_brothel'
