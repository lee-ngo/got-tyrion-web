from setup.scene import Scene

class KingsLanding(Scene):
# back at home
    def enter(self):
        print "\n"
        print "You can't wait to get back to King's Landing after"
        print "all that's happened to you. The sense of urgency is"
        print "only furthered by Bronn's rambling about what he'll"
        print "do with all the money he'll earned from you."
        print "\n"
        print "Finally arriving at King's Landing, you realize the"
        print "best way to repay your debt to Bronn: take him to"
        print "Petyr Baelish's renouned brothel."
        print "\n"
        raw_input("Press ENTER to continue...")
        print "\n"
        print "PETYR 'LITTLEFINGER' BAELISH greets you with open arms."
        print "\n"
        print "Littlefinger: \"Lord Tyrion. You bless us with your"
        print "presence here. My little sparrows inform me you have"
        print "had quite the adventure.\""
        print "\n"
        print "You: \"Indeed. The gods have been quite tempestuous."
        print "Probably not the most prudent move to come to a brothel,"
        print "but, if I could pray with my cock, I'd be far more religious.\""
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "You: \"Anyway, Lord Petyr, I was hoping you could take care of"
        print "my good friend Bronn here. He was quite pivotal in my survival"
        print "thus far, and I'd like to return him the favor.\""
        print "\n"

        print "Bronn: \"Now hang on just a minute. I was promised far more"
        print "than a night in a brothel. Don't think that we'll be even by"
        print "morning, little man.\""
        print "\n"

        print "Before Bronn could finish his objection, two beautiful women"
        print "emerge from beyond a satin curtain and gently grab Bronn"
        print "by each of his arms."
        print "\n"

        print "Bronn: \"Well, I suppose this is a decent start. Lead the way!\""
        print "\n"

        print "Bronn disappears with the women beyond the curtains."
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "Littlefinger: \"Lord Tyrion, I have some news for you."
        print "As a member of the Small Council, I'm here to inform you"
        print "that you have been invited to join us in our next meeting."
        print "I'm headed there right now, actually.\""
        print "\n"
        print "Do you with to JOIN Littlefinger or stay here and RELAX?"
        print "\n"
        choice = raw_input("> ")
        choice = choice.lower()

        if choice == "relax":
            print "\n"
            print "Littlefinger: \"As you wish, Lord Tyrion.\""
            print "\n"
            print "Littlefinger leaves the room. You exhale, wondering if you"
            print "should explore the harem a bit or take a well-deserved nap."
            print "\n"
            print "Your eyes catch a bottle of Dornish wine with"
            print "nothing more than the words 'Lannister' on its label."
            print "Not one to turn down an invitation, you pour yourself a"
            print "respectable glass and take a drink."
            print "\n"
            raw_input("Press ENTER to continue...")
            print "\n"
            print "The wine goes down smoothly. Perhaps the best you've ever"
            print "tasted in your life? Suddenly, you begin to choke. Your"
            print "throat starts to close as blood trickles out of your nose."
            print "With your last ounces of strength, you peel the label back"
            print "on the wine bottle, and a hidden message reads:"
            print "\n"
            print "\"For Elia.\""
            print "\n"
            return 'death'

        elif choice == "join":
            return 'small_council'
