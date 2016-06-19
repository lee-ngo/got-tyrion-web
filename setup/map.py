class Map(object):
# lists all the scenes that can be explored. These need to come AFTER the scenes and not before.
    scenes = {
        'introduction': Introduction(),
        'winterfell': Winterfell(),
        'northern_brothel': NorthernBrothel(),
        'night_with_ros': NightWithRos(),
        'northern_tavern': NorthernTavern(),
        'the_vale': TheVale(),
        'the_wall': TheWall(),
        'kings_landing': KingsLanding(),
        'small_council': SmallCouncil(),
        'death': Death(),
        'success': Success(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
