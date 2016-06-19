from setup.scene import Scene
from random import randint

class BronnFight(Scene):
# a more dynamic fight sequence with Bronn at the Vale
    def enter(self):
        print "\n"
        print "You breathe a sigh of relief as Bronn walks to the center."
        print "Bronn: \"I've grown fond of the little guy, I guess."
        print "Plus I expect to get paid in full once I win.\""
        print "You roll your eyes at his audacity."
        print "\n"
        print "Cat: \"Does anyone here wish to represent justice for my son?\""
        print "The largest soldier, Ser VARDIS EGEN, marches to the center."
        print "\n"
        print "Vardis: \"My lady, I would gladly fight the Imp's champion.\""
        print "\n"
        print "Standing side-by-side, Bronn appears slightly dwarfed by"
        print "Vardis's massive armor and prowess. Bronn remains unphased."
        print "\n"

        raw_input("Press ENTER to continue...")
        print "\n"

        print "Lysa: \"We have our champions. Begin the combat!\""
        print "\n"
        print "The trial by combat has begun! You now control Bronn's actions."
        print "Type in the command in CAPs you wish to do. Seven blessings!"
        bronn_health = 10
        vardis_health = 10

        while bronn_health > 0 and vardis_health > 0:
            print "\n"
            print "What action do you choose: SLASH, THRUST, or GUARD?"

            bronn_action = raw_input("> ")
            bronn_action = bronn_action.lower()

            vardis_choices = ["slash","thrust","guard"]
            vardis_action = vardis_choices[randint(0,2)]

            if vardis_action == "slash" and bronn_action == "slash":
                bronn_health -= 2
                vardis_health -= 2
            elif vardis_action == "slash" and bronn_action == "thrust":
                bronn_health -= 2
                vardis_health -= 1
            elif vardis_action == "thrust" and bronn_action == "guard":
                bronn_health -= 1
            elif vardis_action == "thrust" and bronn_action == "slash":
                bronn_health -= 1
                vardis_health -= 2
            elif vardis_action == "thrust" and bronn_action == "thrust":
                bronn_health -= 1
                vardis_health -= 1
            elif vardis_action == "guard" and bronn_action == "thrust":
                vardis_health -=1

            print "\n"
            print "Bronn chose to %s and Vardis chose to %s." % (bronn_action,vardis_action)
            print "Bronn's health is now %d." % (bronn_health)
            print "Vardis's health is now %d." % (vardis_health)

        if bronn_health > 0 and vardis_health <= 0:
            print "\n"
            print "With a decisive blow, Bronn stabs Ser Vardis through his"
            print "neck and kicks his body through the moon door."
            print "You clench your fists in triumph."
            print "\n"
            print "Lysa: (gasping) \"You fight without honor!\""
            print "\n"
            print "Bronn shrugs and points out the moon door."
            print "\n"
            print "Bronn: \"He did.\""
            print "\n"
            print "Bronn walks over to you and finally frees your hands."
            print "\n"
            print "Bronn: \"Shall we head home now, milord?\""
            print "\n"
            raw_input("Press ENTER to continue...")
            return 'kings_landing'
        else:
            print "\n"
            print "With one fell swoop, Bronn was defeated by Ser Vardis."
            print "The court of The Vale cheers as they throw Bronn's body"
            print "out the moon door."
            print "\n"
            print "Lysa: \"The gods have spoken, and justice will be served"
            print "to my dear sister Catelyn.\""
            print "\n"
            print "The soldiers of The Vale grab you as well. You pray that"
            print "you will land on Bronn's body... not that it will matter."
            print "\n"
            raw_input("Press ENTER to continue...")
            print "\n"
            return 'death'
