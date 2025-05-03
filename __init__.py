from typing import Any, Dict, List
from BaseClasses import Item, ItemClassification, Location, MultiWorld
from worlds.AutoWorld import World, CollectionState
from worlds.generic.Rules import set_rule
from worlds.herocore.Options import HeroCoreOptions
from .Locations import location_table
from .Items import create_itempool, create_item, item_table, item_groups_table
from .Regions import create_regions

class HeroCoreWorld(World):
    """
    Hero Core
    """

    game="Hero Core"
    location_name_to_id = {name: data.code for name, data in location_table.items()}
    item_name_to_id = item_table
    item_name_groups = item_groups_table
    options_dataclass = HeroCoreOptions
    options: HeroCoreOptions


    def create_items(self):
        self.multiworld.itempool += create_itempool(self)

    def create_item(self, name: str) -> Item:
        return create_item(self, name)

    def get_filler_item_name(self) -> str:
        return "Nothing"

    def create_regions(self):
        create_regions(self)

        #if self.options.goal != 5 and (not self.options.expelskips or self.options.expel):
        #    self.multiworld.get_location("Destroy Natural Caves Generator", self.player)\
        #        .place_locked_item(create_item(self, "Barrier - Natural Caves", ItemClassification.progression))
        #    if (self.options.goal.value == 1 or self.options.goal.value == 2):
        #        if self.options.expel and self.options.expelskips:
        #            self.multiworld.get_location("Destroy Army Storage Right Generator", self.player)\
        #                .place_locked_item(create_item(self, "Expel", ItemClassification.progression))
        #        else:
        #            self.multiworld.get_location("Destroy Army Storage Right Generator", self.player)\
        #                .place_locked_item(create_item(self, "Progressive Blade", ItemClassification.progression))
        #    else:
        #        if self.options.expel and self.options.expelskips:
        #            self.multiworld.get_location("Destroy Army Storage Generator", self.player)\
        #                .place_locked_item(create_item(self, "Expel", ItemClassification.progression))
        #        else:
        #            self.multiworld.get_location("Destroy Army Storage Generator", self.player)\
        #                .place_locked_item(create_item(self, "Barrier - Light Factory Right", ItemClassification.progression))


    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "Goal": self.options.goal.value,
            "ShuffleLevelUps": self.options.levelups.value,
            "ExpelSkips": self.options.expelskips.value,
            "DeathLink": self.options.deathlink.value,
            "Shuffle Computers": self.options.computers.value
        }

    def set_rules(self):
        if self.options.levelups and self.options.goal.value != 5:
            set_rule(self.multiworld.get_location("Level Up from Eliminator", self.player),
                     lambda state: state.has("Level Up", self.player, 9))
            

        if (self.options.goal.value == 5):
            self.multiworld.completion_condition[self.player] = lambda state:\
                state.can_reach_region("Ciretako Bottom", self.player)
        else:
            self.multiworld.completion_condition[self.player] = lambda state:\
                state.can_reach_region("Tetron", self.player)