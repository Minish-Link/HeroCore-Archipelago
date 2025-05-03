from typing import List, Dict, TYPE_CHECKING, NamedTuple, Optional

from BaseClasses import Item, ItemClassification
from .Locations import get_total_locations

if TYPE_CHECKING:
    from . import HeroCoreWorld

class HeroCoreItem(Item):
    game = "Hero Core"

def create_itempool(world: "HeroCoreWorld") -> List[Item]:
    itempool: List[Item] = []

    if (world.options.goal.value != 5):
        for i in range(3):
            itempool.append(create_item(world, "Progressive Blade", ItemClassification.progression))
            itempool.append(create_item(world, "Progressive Suit", ItemClassification.progression))
        for i in range(2):
            itempool.append(create_item(world, "Progressive Blaster", ItemClassification.progression))
        itempool.append(create_item(world, "Pattern Scanner", ItemClassification.progression))

        if world.options.levelups and world.options.goal != 5:
            for i in range(10):
                itempool.append(create_item(world, "Level Up", ItemClassification.progression_skip_balancing))

        #if world.options.expel:
        #    itempool.append(create_item(world, "Expel", ItemClassification.progression))

    if world.options.computers:
        for i in range(10):
            if world.options.goal.value == 2 or world.options.goal.value == 4:
                itempool.append(create_item(world, "Core Computer", ItemClassification.progression))
            else:
                itempool.append(create_item(world, "Core Computer", ItemClassification.filler))

    if world.options.goal.value == 1 or world.options.goal.value == 2:
        for name in barriers_normal:
            itempool.append(create_item(world, name, ItemClassification.progression))
    elif world.options.goal.value == 3 or world.options.goal.value == 4:
        for name in barriers_hard:
            itempool.append(create_item(world, name, ItemClassification.progression))
    elif world.options.goal.value == 5:
        for name in barriers_annihilation:
            itempool.append(create_item(world, name, ItemClassification.progression))

    # This shouldn't happen, but just in case...
    filleritems = get_total_locations(world) - len(itempool)
    for i in range(filleritems):
        itempool.append(create_item(world, "Nothing", ItemClassification.filler))

    # Remove Locked Items
    if world.options.goal.value != 5 and (not world.options.expelskips):
        remove_locked_item(world, itempool, "Barrier - Natural Caves")
        if world.options.goal.value == 1 or world.options.goal.value == 2:
            remove_locked_item(world, itempool, "Progressive Blade")
        else:
            remove_locked_item(world, itempool, "Barrier - Light Factory Right")

    return itempool

def create_item(world: "HeroCoreWorld", name: str, progtype: ItemClassification = ItemClassification.filler):
    return HeroCoreItem(name, progtype, item_table[name], world.player)

def remove_locked_item(world: "HeroCoreWorld", itempool: List[Item], name: str):
    for item in itempool:
        if item.name == name:
            itempool.remove(item)
            return

base_item_table: Dict[str, int] = {
    "Progressive Blaster":  1, 
    "Progressive Blade":    2, 
    "Progressive Suit":     3, 
    "Pattern Scanner":      4, 
    "Level Up":             5, 
    "Core Computer":        6, 
    "Expel":                7, 
    "Nothing":              255
}

barrier_item_table: Dict[str, int] = {
    "Barrier - Natural Caves":              8,
    "Barrier - Army Storage Right":         9,
    "Barrier - Army Storage Left":          10,
    "Barrier - New Caves Right":            11,
    "Barrier - New Caves Left":             12,
    "Barrier - War Factory":                13,
    "Barrier - Guardian Zone Right":        14,
    "Barrier - Guardian Zone Left":         15,
    "Barrier - Annihilator Factory":        16,
    "Barrier - Core":                       17,
    "Barrier - Army Storage":               18,
    "Barrier - Light Factory Right":        19,
    "Barrier - Light Factory Left":         20,
    "Barrier - New Caves":                  21,
    "Barrier - Guardian Zone Bottom":       22,
    "Barrier - Guardian Zone Top":          23,
    "Barrier - Annihilator Factory Bottom": 24,
    "Barrier - Annihilator Factory Top":    25,
    "Barrier - Ciretako Top":               26,
    "Barrier - Ciretako Right":             27,
    "Barrier - Ciretako Bottom":            28
}

barriers_normal: List[str] = [
    "Barrier - Natural Caves",
    "Barrier - Army Storage Right",
    "Barrier - Army Storage Left",
    "Barrier - New Caves Right",
    "Barrier - New Caves Left",
    "Barrier - War Factory",
    "Barrier - Guardian Zone Right",
    "Barrier - Guardian Zone Left",
    "Barrier - Annihilator Factory",
    "Barrier - Core"
]

barriers_hard: List[str] = [
    "Barrier - Natural Caves",
    "Barrier - Core",
    "Barrier - Army Storage",
    "Barrier - Light Factory Right",
    "Barrier - Light Factory Left",
    "Barrier - New Caves",
    "Barrier - Guardian Zone Bottom",
    "Barrier - Guardian Zone Top",
    "Barrier - Annihilator Factory Bottom",
    "Barrier - Annihilator Factory Top",
]

barriers_annihilation: List[str] = [
    "Barrier - Ciretako Top",
    "Barrier - Ciretako Right",
    "Barrier - Ciretako Bottom"
]

item_table = {
    **base_item_table,
    **barrier_item_table
}

item_groups_table = {
    "Barrier": barrier_item_table.keys()
}