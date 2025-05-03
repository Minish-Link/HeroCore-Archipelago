import random
from typing import Callable, Dict, NamedTuple, TYPE_CHECKING, List

from BaseClasses import CollectionState, Location, ItemClassification
from worlds.generic.Rules import CollectionRule

if TYPE_CHECKING:
    from . import HeroCoreWorld

class HeroCoreLocation(Location):
    game="Hero Core"

def get_total_locations(world: "HeroCoreWorld") -> int:
    total: int = 0
    for loc in world.multiworld.get_locations(world.player):
        total+=1
    return total

class LocData(NamedTuple):
    code: int
    locked_item: Callable[["HeroCoreWorld"], str] = lambda world: None
    locked_item_class: Callable[["HeroCoreWorld"], int] = lambda world: ItemClassification.filler

location_table_items: Dict[str, LocData] = {
    "Powerup from Rock Smasher":            LocData(code=1),
    "Powerup from Silencer":                LocData(code=2),
    "Powerup from Plasma Hydra":            LocData(code=3),
    "Powerup from Reaper Drone":            LocData(code=4),
    "Powerup from Liquid Metal Processor":  LocData(code=5),
    "Powerup from Grand Mother":            LocData(code=6),
    "Powerup from Guardian":                LocData(code=7),
    "Powerup from Star Splitter":           LocData(code=8),
    "Powerup from Elites":                  LocData(code=9)
}

location_table_levelups: Dict[str, LocData] = {
    "Level Up from Rock Smasher":           LocData(code=10,\
        locked_item = lambda world: "Level Up" if (not world.options.levelups)  else None,\
        locked_item_class = lambda world: ItemClassification.progression_skip_balancing),
    "Level Up from Silencer":               LocData(code=11,\
        locked_item = lambda world: "Level Up" if (not world.options.levelups)  else None,\
        locked_item_class = lambda world: ItemClassification.progression_skip_balancing),
    "Level Up from Plasma Hydra":           LocData(code=12,\
        locked_item = lambda world: "Level Up" if (not world.options.levelups)  else None,\
        locked_item_class = lambda world: ItemClassification.progression_skip_balancing),
    "Level Up from Reaper Drone":           LocData(code=13,\
        locked_item = lambda world: "Level Up" if (not world.options.levelups)  else None,\
        locked_item_class = lambda world: ItemClassification.progression_skip_balancing),
    "Level Up from Liquid Metal Processor": LocData(code=14,\
        locked_item = lambda world: "Level Up" if (not world.options.levelups)  else None,\
        locked_item_class = lambda world: ItemClassification.progression_skip_balancing),
    "Level Up from Grand Mother":           LocData(code=15,\
        locked_item = lambda world: "Level Up" if (not world.options.levelups)  else None,\
        locked_item_class = lambda world: ItemClassification.progression_skip_balancing),
    "Level Up from Guardian":               LocData(code=16,\
        locked_item = lambda world: "Level Up" if (not world.options.levelups)  else None,\
        locked_item_class = lambda world: ItemClassification.progression_skip_balancing),
    "Level Up from Star Splitter":          LocData(code=17,\
        locked_item = lambda world: "Level Up" if (not world.options.levelups)  else None,\
        locked_item_class = lambda world: ItemClassification.progression_skip_balancing),
    "Level Up from Elites":                 LocData(code=18,\
        locked_item = lambda world: "Level Up" if (not world.options.levelups)  else None,\
        locked_item_class = lambda world: ItemClassification.progression_skip_balancing),
    "Level Up from Eliminator":             LocData(code=19,\
        locked_item = lambda world: "Level Up" if (not world.options.levelups)  else None,\
        locked_item_class = lambda world: ItemClassification.progression_skip_balancing)
}


location_table_computers: Dict[str, LocData] = {
    "Computer in Natural Caves":            LocData(code=20,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.progression if (world.options.goal == 2 or
                                                                             world.options.goal == 4)
                                                    else ItemClassification.filler),
    "Computer in Army Storage":             LocData(code=21,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.progression if (world.options.goal == 2 or
                                                                             world.options.goal == 4)
                                                    else ItemClassification.filler),
    "Computer in Control":                  LocData(code=22,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.progression if (world.options.goal == 2 or
                                                                             world.options.goal == 4)
                                                    else ItemClassification.filler),
    "Computer in Light Factory":            LocData(code=23,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.progression if (world.options.goal == 2 or
                                                                             world.options.goal == 4)
                                                    else ItemClassification.filler),
    "Computer in New Caves":                LocData(code=24,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.progression if (world.options.goal == 2 or
                                                                             world.options.goal == 4)
                                                    else ItemClassification.filler),
    "Computer in War Factory":              LocData(code=25,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.progression if (world.options.goal == 2 or
                                                                             world.options.goal == 4)
                                                    else ItemClassification.filler),
    "Computer in Guardian Zone":            LocData(code=26,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.progression if (world.options.goal == 2 or
                                                                             world.options.goal == 4)
                                                    else ItemClassification.filler),
    "Computer in Annihilator Factory":      LocData(code=27,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.progression if (world.options.goal == 2 or
                                                                             world.options.goal == 4)
                                                    else ItemClassification.filler),
    "Computer in Old Base":                 LocData(code=28,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.progression if (world.options.goal == 2 or
                                                                             world.options.goal == 4)
                                                    else ItemClassification.filler),
    "Top Computer in New Caves":            LocData(code=29,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.progression if (world.options.goal == 2 or
                                                                             world.options.goal == 4)
                                                    else ItemClassification.filler),
    "Bottom Computer in New Caves":         LocData(code=30,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.progression if (world.options.goal == 2 or
                                                                             world.options.goal == 4)
                                                    else ItemClassification.filler),
    "Left Computer in Guardian Zone":       LocData(code=31,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.progression if (world.options.goal == 2 or
                                                                             world.options.goal == 4)
                                                    else ItemClassification.filler),
    "Right Computer in Guardian Zone":      LocData(code=32,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.progression if (world.options.goal == 2 or
                                                                             world.options.goal == 4)
                                                    else ItemClassification.filler),
    "Computer 1":                           LocData(code=33,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.filler),
    "Computer 2":                           LocData(code=34,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.filler),
    "Computer 3":                           LocData(code=35,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.filler),
    "Computer 4":                           LocData(code=36,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.filler),
    "Computer 5":                           LocData(code=37,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.filler),
    "Computer 6":                           LocData(code=38,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.filler),
    "Computer 7":                           LocData(code=39,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.filler),
    "Computer 8":                           LocData(code=40,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.filler),
    "Computer 9":                           LocData(code=41,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.filler),
    "Computer 10":                          LocData(code=42,\
        locked_item = lambda world: "Core Computer" if (not world.options.computers) else None,\
        locked_item_class = lambda world: ItemClassification.filler)
}

location_table_generators: Dict[str, LocData] = {
    "Destroy Natural Caves Generator":              LocData(code=43,\
        locked_item = lambda world: "Barrier - Natural Caves" if (not world.options.expelskips) else None,\
        locked_item_class = lambda world: ItemClassification.progression),
    "Destroy Army Storage Right Generator":         LocData(code=44,\
        locked_item = lambda world: "Progressive Blade" if (not world.options.expelskips) else None,\
        locked_item_class = lambda world: ItemClassification.progression),
    "Destroy Army Storage Left Generator":          LocData(code=45),
    "Destroy New Caves Right Generator":            LocData(code=46),
    "Destroy New Caves Left Generator":             LocData(code=47),
    "Destroy War Factory Generator":                LocData(code=48),
    "Destroy Guardian Zone Right Generator":        LocData(code=49),
    "Destroy Guardian Zone Left Generator":         LocData(code=50),
    "Destroy Annihilator Factory Generator":        LocData(code=51),
    "Destroy Core Generator":                       LocData(code=52),
    "Destroy Army Storage Generator":               LocData(code=53,\
        locked_item = lambda world: "Barrier - Light Factory Right" if (not world.options.expelskips) else None,\
        locked_item_class = lambda world: ItemClassification.progression),
    "Destroy Light Factory Right Generator":        LocData(code=54),
    "Destroy Light Factory Left Generator":         LocData(code=55),
    "Destroy New Caves Generator":                  LocData(code=56),
    "Destroy Guardian Zone Bottom Generator":       LocData(code=57),
    "Destroy Guardian Zone Top Generator":          LocData(code=58),
    "Destroy Annihilator Factory Bottom Generator": LocData(code=59),
    "Destroy Annihilator Factory Top Generator":    LocData(code=60),
    "Destroy Ciretako Top Generator":               LocData(code=61),
    "Destroy Ciretako Right Generator":             LocData(code=62),
    "Destroy Ciretako Bottom Generator":            LocData(code=63)
}

location_regions_normal: Dict[str, str] = {
    "Level Up from Rock Smasher":           "Core",
    "Level Up from Silencer":               "Army Storage Top",
    "Level Up from Plasma Hydra":           "Core",
    "Level Up from Reaper Drone":           "Core",
    "Level Up from Liquid Metal Processor": "New Caves Boss",
    "Level Up from Grand Mother":           "War Factory Boss",
    "Level Up from Guardian":               "Guardian Zone",
    "Level Up from Star Splitter":          "Annihilator Factory Boss",
    "Level Up from Elites":                 "Old Base Boss",
    "Level Up from Eliminator":             "Natural Caves",
    "Powerup from Rock Smasher":            "Core",
    "Powerup from Silencer":                "Army Storage Top",
    "Powerup from Plasma Hydra":            "Core",
    "Powerup from Reaper Drone":            "Core",
    "Powerup from Liquid Metal Processor":  "New Caves Boss",
    "Powerup from Grand Mother":            "War Factory Boss",
    "Powerup from Guardian":                "Guardian Zone",
    "Powerup from Star Splitter":           "Annihilator Factory Boss",
    "Powerup from Elites":                  "Old Base Boss",
    "Computer in Natural Caves":            "Core",
    "Computer in Army Storage":             "Army Storage Computer",
    "Computer in Control":                  "Core",
    "Computer in Light Factory":            "Core",
    "Top Computer in New Caves":            "New Caves Top Computer",
    "Bottom Computer in New Caves":         "New Caves Bottom Computer",
    "Computer in War Factory":              "War Factory Computer",
    "Computer in Guardian Zone":            "Guardian Zone",
    "Computer in Annihilator Factory":      "Core",
    "Computer in Old Base":                 "Old Base Computer",
    "Destroy Natural Caves Generator":      "Natural Caves",
    "Destroy Army Storage Right Generator": "Army Storage Bottom",
    "Destroy Army Storage Left Generator":  "Army Storage Top",
    "Destroy New Caves Right Generator":    "Core",
    "Destroy New Caves Left Generator":     "New Caves Left",
    "Destroy War Factory Generator":        "Core",
    "Destroy Guardian Zone Right Generator":"Core",
    "Destroy Guardian Zone Left Generator": "Guardian Zone Middle",
    "Destroy Annihilator Factory Generator":"Annihilator Factory Middle",
    "Destroy Core Generator":               "Core",
    "Expel Computer":                       "Expel Computer"
}

location_regions_hard: Dict[str, str] = {
    "Level Up from Rock Smasher":                   "Core",
    "Level Up from Silencer":                       "Army Storage Right",
    "Level Up from Plasma Hydra":                   "Core",
    "Level Up from Reaper Drone":                   "Light Factory Boss",
    "Level Up from Liquid Metal Processor":         "New Caves Boss",
    "Level Up from Grand Mother":                   "Core",
    "Level Up from Guardian":                       "Guardian Zone Right",
    "Level Up from Star Splitter":                  "Annihilator Factory Boss",
    "Level Up from Elites":                         "Old Base",
    "Level Up from Eliminator":                     "Natural Caves",
    "Powerup from Rock Smasher":                    "Core",
    "Powerup from Silencer":                        "Army Storage Right",
    "Powerup from Plasma Hydra":                    "Core",
    "Powerup from Reaper Drone":                    "Light Factory Boss",
    "Powerup from Liquid Metal Processor":          "New Caves Boss",
    "Powerup from Grand Mother":                    "Core",
    "Powerup from Guardian":                        "Guardian Zone Right",
    "Powerup from Star Splitter":                   "Annihilator Factory Boss",
    "Powerup from Elites":                          "Old Base",
    "Computer in Natural Caves":                    "Core",
    "Computer in Army Storage":                     "Army Storage Right",
    "Computer in Control":                          "Control Computer",
    "Computer in Light Factory":                    "Core",
    "Computer in New Caves":                        "New Caves Boss",
    "Computer in War Factory":                      "War Factory Computer",
    "Computer in Annihilator Factory":              "Annihilator Factory Right",
    "Computer in Old Base":                         "Old Base",
    "Left Computer in Guardian Zone":               "Guardian Zone Left Computer",
    "Right Computer in Guardian Zone":              "Guardian Zone Right Computer",
    "Destroy Natural Caves Generator":              "Natural Caves",
    "Destroy Core Generator":                       "Core",
    "Destroy Army Storage Generator":               "Army Storage Left",
    "Destroy Light Factory Right Generator":        "Light Factory Top",
    "Destroy Light Factory Left Generator":         "Core",
    "Destroy New Caves Generator":                  "Core",
    "Destroy Guardian Zone Bottom Generator":       "Core",
    "Destroy Guardian Zone Top Generator":          "Guardian Zone Middle",
    "Destroy Annihilator Factory Bottom Generator": "Annihilator Factory Right",
    "Destroy Annihilator Factory Top Generator":    "Annihilator Factory Top",
    "Expel Computer":                               "Expel Computer"
}

location_regions_annihilation: Dict[str, str] ={
    "Computer 1":                           "Ciretako Middle",
    "Computer 2":                           "Ciretako Middle",
    "Computer 3":                           "Ciretako Middle",
    "Computer 4":                           "Ciretako Middle",
    "Computer 5":                           "Ciretako Top",
    "Computer 6":                           "Ciretako Right",
    "Computer 7":                           "Ciretako Right",
    "Computer 8":                           "Ciretako Bottom",
    "Computer 9":                           "Ciretako Bottom",
    "Computer 10":                          "Ciretako Bottom",
    "Destroy Ciretako Top Generator":       "Ciretako Middle",
    "Destroy Ciretako Right Generator":     "Ciretako Top",
    "Destroy Ciretako Bottom Generator":    "Ciretako Right",

}

location_table = {
    **location_table_items,
    **location_table_levelups,
    **location_table_computers,
    **location_table_generators
}