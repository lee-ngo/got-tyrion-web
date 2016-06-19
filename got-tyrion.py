# list of core functions used in game Setup
from sys import exit
from setup.scene import Scene # imported before every inherited Scene
from setup.engine import Engine

# list of scenes used in this game
from scenes.death import Death
from scenes.introduction import Introduction
from scenes.success import Success
from scenes.winterfell import Winterfell
from scenes.northern_brothel import NorthernBrothel
from scenes.night_with_ros import NightWithRos
from scenes.the_wall import TheWall
from scenes.northern_tavern import NorthernTavern
from scenes.the_vale import TheVale
from scenes.bronn_fight import BronnFight
from scenes.kings_landing import KingsLanding
from scenes.small_council import SmallCouncil

class Map(object):
# lists all the scenes that can be explored. These need to come AFTER the scenes and not before.
    scenes = {
        'introduction': Introduction(),
        'winterfell': Winterfell(),
        'northern_brothel': NorthernBrothel(),
        'night_with_ros': NightWithRos(),
        'northern_tavern': NorthernTavern(),
        'the_vale': TheVale(),
        'bronn_fight': BronnFight(),
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

start_map = Map('introduction')
start_game = Engine(start_map)
start_game.play()
