from setup.scene import Scene

class SmallCouncil(Scene):

    def enter(self):
        print "\n"
        print "You walk with Littlefinger to the room of the Small Council,"
        print "perhaps the most powerful group in all of the Seven Kingdoms."
        print "\n"
        print "Members of the Small Council include:"
        print "- PYCELLE, Grand Maester"
        print "- VARYS, Master of Whisperers"
        print "- STANNIS, Master of Ships"
        print "- RENLY, Master of Laws"
        print "- LITTLEFINGER, Master of Coin"
        print "\n"
        print "You notice that the table of the Small Council has one chair"
        print "that is noticeably vacant: The Hand of the King."
        print "\n"
        print "Pycelle: \"Lord Tyrion. Welcome. We have been expecting you.\""
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "You: \"It is an honor to be in the presence of such esteemed"
        print "members of the Small Council. Forgive me if I still struggle"
        print "to understand the meaning of my invitation here.\""
        print "\n"
        print "Varys: \"We've been watching you for quite some time, Lord"
        print "Tyrion. My spiders everywhere have kept track of you since"
        print "you rode off to Winterfell not too long ago.\""
        print "\n"
        print "Renly: \"Indeed. While you may not be perfect, there aren't"
        print "many of us alive who have less ... quirks.\""
        print "\n"
        print "Stannis: \"...Fewer.\""
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "Renly rolls his eyes at his older brother's obsession with"
        print "proper grammar."
        print "\n"
        print "Littlefinger: \"To get to the point, the Kingdom needs"
        print "someone with your cunning and insight to lead it out of"
        print "a potentially dark time.\""
        print "\n"
        print "Pycelle: \"Lord Tyrion, we need you to serve as Hand of the King.\""
        print "\n"
        print "You are shocked. Surely they must be mistaken. You, Tyrion"
        print "Lannister, unwanted son of Tywin Lannister, frequenter of"
        print "brothels and wine... this is whom they want as Hand?"
        print "\n"
        print "You: \"Forgive me, gentlemen... but doesn't the position"
        print "currently belong to Ned Stark?\""
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "Renly: \"Yes, but... let's just say Stark is a bit too...\""
        print "\n"
        print "Littlefinger: \"Trusting.\""
        print "\n"
        print "Varys: \"What the kingdom needs is someone who knows all the"
        print "angles and how to play them properly. That person is you."
        print "\n"
        print "Pycelle: \"I think we've discussed enough. What do you think?\""
        print "\n"
        print "Do you ACCEPT or DECLINE the position of Hand of the King?"

        final_choice = raw_input("> ")
        final_choice = final_choice.lower()

        if final_choice == 'accept':
            print "\n"
            print "And so, Tyrion Lannister, son of Tywin Lannister"
            print "was named Hand of the King. With the support of multiple"
            print "houses, he managed to lead Westeros into a new era of"
            print "peace and prosperity, only to be overwhelmed by a frozen"
            print "zombie army from beyond The Wall and a blonde woman"
            print "commanding three dragons and a barbarian horde."
            print "\n"
            return 'success'
        else:
            print "\n"
            print "Pycelle: \"What an insult! I knew he could not be trusted!\""
            print "\n"
            print "Stannis: \"Indeed. Let's burn him at the stake.\""
            print "\n"
            print "Sometimes you should take an offer you can't refuse."
            print "\n"
            return 'death'
