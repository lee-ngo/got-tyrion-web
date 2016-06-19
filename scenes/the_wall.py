from setup.scene import Scene

class TheWall(Scene):
# hang out with the Night's Watch for a bright
    def enter(self):
        print "\n"
        print "Muttering along the way to The Wall, you travel with JON SNOW,"
        print "bastard son of Eddard 'Ned' Stark, Lord of Winterfell"
        print "and Warden of the North. Jon has opted to 'take the black,'"
        print "a colloquialism for those who pledge their lives to The Night's Watch."
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "At a rest stop, Jon stares at you as you read a book."
        print "You look up for a moment, smile politely, and return to the book."
        print "\n"
        print "Jon: \"Why do you read so much?\""
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "You sigh, close your book, and look up at Jon."
        print "You: \"Tell me, bastard. When you look at me, what do you see?\""
        print "\n"
        print "Jon looks back at you, perplexed by the question."
        print "\n"
        print "Jon: \"Is this a trick?\" (Jon Snow generally knows nothing.)"
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "You: \"What you see ... is a dwarf."
        print "If I had been born a peasant,"
        print "they might have left me out in the woods to die."
        print "Alas, I was born a Lannister of Casterly Rock."
        print "Things are expected of me. My father was the"
        print "Hand of the King for twenty years.\""
        print "\n"
        print "Jon: \"Until your brother killed that king.\""
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "You: \"...Yes. Until my brother killed him."
        print "Life is full of these little ironies."
        print "My sister married the new king, and"
        print "my repulsive nephew will be king after him.\""
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "You: \"I must do my part for the honor of my house;"
        print "wouldn't you agree? But how? Well, my brother has his sword,"
        print "and I have my mind. And a mind needs books like a sword"
        print "needs a whetstone. That's why I read so much, Jon Snow.\""
        print "\n"
        print "Jon nods, slightly impressed. You resume reading your book."
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "In a week, you and the rest of the part arrive at The Wall."
        print "From the base at Castle Black, you stare up in amazement."
        print "The view is impressive. Miles of ice stretch in every direction."
        print "You've been invited to take the lift to the top of the wall."
        print "\n"
        print "Would you like to go to the TOP or LEAVE Castle Black?"
        print "\n"

        choice_top = raw_input("> ")
        choice_top = choice_top.lower()

        if choice_top == "top":

            print "\n"
            print "The top of The Wall bestows an even more breathtaking view."
            print "You look out into the frozen lands to the North and wonder"
            print "if the legends are true. Are there really giants, faeries,"
            print "cannibals, undead armies, even white walkers...?"
            print "\n"

            raw_input("Press ENTER to continue...")
            print "\n"

            print "\"Nonsense,\" you mutter to yourself. Suddenly, a weird"
            print "idea popped into your head. What would happen if you..."
            print "piss over the edge of The Wall?"
            print "\n"

            print "Do you piss off the edge of the world? (Y/N)"
            print "\n"

            choice_piss = raw_input(">")
            choice_piss = choice_piss.lower()

            if choice_piss == "y":
                print "Living up to your reputation as a bit of a hedonist,"
                print "you whip out your member and urinate over the edge."
                print "The warmth pairs surprisingly well with the cold."
                print "\n"
                print "A strong gust of wind hits you from behind."
                print "A normal-sized man would stagger a bit. You, however,"
                print "are not a normal-sized man."
                print "\n"
                print "You are forced off the edge, falling thousands of yards"
                print "down the Northern side of The Wall. Your member dangles"
                print "freely as you fall to a crushing, freezing demise."
                print "\n"

                raw_input("Press ENTER to continue...")
                print "\n"
                return 'death'

            elif choice_piss == "n":
                print "\n"

                print "\"A silly idea,\" you reflect to yourself. Besides,"
                print "whipping out your member might not be the most prudent"
                print "idea from this altitude and at this temperature."
                print "\n"

                raw_input("Press ENTER to continue...")
                print "\n"

                print "As you are about to leave, BRONN approaches you."
                return 'northern_tavern'

            else:
                print "\n"
                print "Before you can make a decision, BRONN approaches you."
                return 'northern_tavern'

        elif choice_top == "leave":
            print "\n"
            print "As you are about to leave, BRONN approaches you."
            return 'northern_tavern'

        else:
            print "\n"
            print "Before you can make a decision, BRONN approaches you."
            return 'northern_tavern'
