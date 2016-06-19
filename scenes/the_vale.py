from setup.scene import Scene

class TheVale(Scene):
# trial by combat with a moon door
    def enter(self):
        print "\n"
        print "You put up no resistance as the Northerners converge upon you."
        print "\n"
        print "In a few days, you reach The Vale, one of the most formidable"
        print "and beautiful castles in all of the Seven Kingdoms. Your hands"
        print "are bound by rope as you are tugged along by Catelyn Stark. Not"
        print "too far back is Bronn, who is also tied at the wrists but not"
        print "particularly worried about his present situation."
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "The Vale is controlled by LYSA ARRYN, widow to the late Jon"
        print "Arryn and previous Hand of the King until he was mysteriously"
        print "poisoned. Lysa is obviously a little removed from reality,"
        print "as evident by her continued breastfeeding of her ten-year-old"
        print "son, the equally daft ROBYN."

        print "\n"
        raw_input("Press ENTER to continue...")
        print "\n"

        print "Lysa: \"Dear sister, it has been far too long."
        print "What brings you to The Vale, and with two captives, no less?\""
        print "\n"

        print "Cat: \"I seek justice for the attempted murder of my son."
        print "I have proof that Tyrion Lannister conspired to send an"
        print "assassin to my crippled son's bedchamber.\""
        print "\n"

        print "Lysa is clearly startled by the accusation and immediately"
        print "sympathizes with her sister, sending you a look of contempt."
        print "This was not off to a good start for you."
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "Lysa: \"It is obvious that Tyrion Lannister is guilty."
        print "Look at him. That is clearly the disposition of a murderer."
        print "As Lady Regent of The Vale, I hereby find you guilty--\""
        print "\n"

        print "You: \"WAIT! I demand a trial by combat!\""
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "The court of The Vale begins to murmur."
        print "\n"

        print "Cat: \"A trial by combat? How absurd!\""
        print "\n"

        print "Lysa: \"I'm afraid he is within his rights to demand one."
        print "Let's get on with it then. Choose your champion, Imp.\""
        print "\n"

        print "You boil every time someone calls you that."
        print "Who will be your champion: JAIME, BRONN, or TYRION?"
        print "\n"

        champion = raw_input("> ")
        champion = champion.lower()

        if champion == "jaime":
            print "\n"
            print "You: \"I choose Jaime Lannister as my champion.\""
            print "The rest of the court murmurs. 'The Kingslayer' as"
            print "he is known throughout the Seven Kingdoms was"
            print "renowned for his swordplay, and surely he would"
            print "come to his little brother's aid."
            print "\n"
            print "Lysa: \"We cannot honor that choice. Jaime Lannister's"
            print "whereabouts are unknown, and trials by combat must be"
            print "carried out within three days. Choose another.\""
            print "\n"
            print "You: \"Do I have any volunteers?\""
            print "\n"
            raw_input("Press ENTER to continue...")
            print "\n"

            print "The court laughs at your desperate plea."
            print "Your brow begins to sweat profusely. In all of the Seven"
            print "Kingdoms, who would be willing to sacrifice their life"
            print "for yours besides Jaime?"
            print "\n"
            print "Bronn: \"I'll do it, I guess.\""
            print "\n"

            raw_input("Press ENTER to continue...")
            print "\n"
            return 'bronn_fight'

        elif champion == "bronn":
            print "\n"
            print "You: \"I choose Bronn of the Blackwater.\""
            print "Bronn is surprised by the choice, but one look into"
            print "your fearful, knowing eyes was more than enough."
            return 'bronn_fight'

        elif champion == "tyrion":
            print "\n"
            print "You: \"I choose myself as champion.\""
            print "\n"
            print "The Vale court erupts with laughter. Even Bronn can't"
            print "help but contain his snickers."
            print "\n"
            print "Lysa: \"Let's just save us all time. Guards!\""
            print "\n"
            print "The knights grab you by the arms and vastly overpower you."
            print "\n"
            print "Robyn: \"Make the little man fly!\""
            print "\n"

            raw_input("Press ENTER to continue...")
            print "\n"
            print "The guards throw you out the moon door, a hole in the"
            print "middle of the castle that sends any unlucky soul to a brutal"
            print "death upon the rocky mountains below."
            print "\n"
            print "Today, that unlucky soul is you."
            print "\n"
            return 'death'

        else:
            print "\n"
            print "Your stammering will not be tolerated. The Vale guards"
            print "grab you and throw you out the Moon Door."
            print "\n"
            return 'death'
