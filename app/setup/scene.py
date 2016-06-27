class Scene(object):
# inherited class for all the scenes in case you haven't built it yet
    def enter(self):
         print "This scene is not yet configured. Subclass it and implement enter()."
         exit(1)

    def __init__(self, name, paths):
        self.name = name # name of scene
        self.paths = {} # empty dictionary for options

    def go(self, direction): # grab the next scene with a button
        return self.paths.get(direction, None)

    def add_paths(self, paths): # create options afterwards
        self.paths.update(paths)

introduction = Scene("Introduction")

winterfell = Scene("Winterfell")

northern_brothel = Scene("Northern Brothel")

night_with_ros = Scene("A Night with Ros")

northern_tavern = Scene("Rest Stop at a Tavern")

the_vale = Scene("The Vale")

the_wall = Scene("The Wall")

kings_landing = Scene("Arrival at King's Landing")

small_council = Scene("Meet with the Small Council")

death = Scene("You have died")

success = Scene("You win!")

START = introduction
