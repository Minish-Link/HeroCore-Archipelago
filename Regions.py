from typing import Dict, List, TYPE_CHECKING, Callable
from BaseClasses import CollectionState, MultiWorld, Region, Entrance
from worlds.generic.Rules import CollectionRule
from .Locations import HeroCoreLocation, location_table,location_table_levelups,\
    location_regions_normal, location_regions_hard, location_regions_annihilation

from .Items import create_item

if TYPE_CHECKING:
    from . import HeroCoreWorld

def create_regions(world: "HeroCoreWorld"):
    if world.options.goal == 1 or world.options.goal == 2:
        for name in regions_normal.keys():
            create_region(world, name, location_regions_normal)
        connect_regions(world, regions_normal)

    elif world.options.goal == 3 or world.options.goal == 4:
        for name in regions_hard.keys():
            create_region(world, name, location_regions_hard)
        connect_regions(world, regions_hard)

    elif world.options.goal == 5:
        for name in regions_annihilation.keys():
            create_region(world, name, location_regions_annihilation)
        connect_regions(world, regions_annihilation)

    for region in world.get_regions():
        for loc in region.locations:
            locked_item_name = location_table[loc.name].locked_item(world)
            if locked_item_name:
                loc.place_locked_item(create_item(world, locked_item_name, location_table[loc.name].locked_item_class(world)))
                



def create_region(world: "HeroCoreWorld", name: str, region_table: Dict[str,str]) -> Region:
    region = Region(name, world.player, world.multiworld)

    region.add_locations({
        location_name: location_data.code for location_name, location_data in location_table.items()
        if location_name in region_table.keys() and
        region_table[location_name] == region.name
        }, HeroCoreLocation)

    world.multiworld.regions.append(region)

def connect_regions(world: "HeroCoreWorld", exits: Dict[str, Dict[str, Callable[[CollectionState, "HeroCoreWorld"], bool]]]):
    for regname in exits.keys():
        reg = world.multiworld.get_region(regname, world.player)
        for exitreg, exitrule in exits[regname].items():
            reg.connect(world.multiworld.get_region(exitreg, world.player), None, lambda state, temprule=exitrule: temprule(state, world))

# Region Names: Exits
regions_normal: Dict[str, Dict[str, Callable[[CollectionState, "HeroCoreWorld"], bool]]] = {
    "Menu": {
        "Natural Caves": lambda state, world:
            True},
    "Natural Caves": {
        "Army Storage Bottom": lambda state, world:
            state.has("Barrier - Natural Caves", world.player) or
            (state.can_reach_region("Core", world.player) and
            state.has("Progressive Blade", world.player, 1)) or
            (state.can_reach_region("Army Storage Top", world.player) and
            (state.has("Barrier - Army Storage Right", world.player) or
            state.has("Progressive Blade", world.player, 2))),
        "Core": lambda state, world:
            state.has("Progressive Suit", world.player, 2) or
            state.has("Progressive Blade", world.player, 2) or
            world.options.expelskips or
            (state.can_reach_region("Army Storage Top", world.player) and
            state.has("Barrier - Army Storage Left", world.player)) or
            state.has("Pattern Scanner", world.player)},
    "Army Storage Bottom": {
        "Core": lambda state, world:
            state.has("Progressive Blade", world.player, 1),
        "Army Storage Top": lambda state, world:
            state.has("Barrier - Army Storage Right", world.player) or
            state.has("Progressive Blade", world.player, 2),
        "Expel Computer": lambda state, world:
            state.has("Progressive Blade", world.player, 3)},
    "Army Storage Top": {
        "War Factory Computer": lambda state, world:
            state.has("Progressive Blade", world.player, 2),
        "Core": lambda state, world:
            state.has("Barrier - Army Storage Left", world.player)},
    "Army Storage Computer": {},
    "New Caves Left": {
        "New Caves Boss": lambda state, world:
            state.has("Barrier - New Caves Left", world.player) or
            state.has("Progressive Blade", world.player, 2)},
    "New Caves Boss": {},
    "New Caves Top Computer": {},
    "New Caves Bottom Computer": {},
    "War Factory Boss": {},
    "War Factory Computer": {},
    "Guardian Zone": {
        "Guardian Zone Middle": lambda state, world:
            state.has("Barrier - Guardian Zone Left", world.player)},
    "Guardian Zone Middle": {},
    "Annihilator Factory Middle": {
        "Annihilator Factory Boss": lambda state, world:
            state.has("Barrier - Annihilator Factory", world.player)},
    "Annihilator Factory Boss": {},
    "Old Base Boss": {},
    "Old Base Computer": {},
    "Core": {
        "Army Storage Top": lambda state, world:
            state.has("Barrier - Army Storage Left", world.player) or
            state.has("Pattern Scanner", world.player),
        "Army Storage Computer": lambda state, world:
            state.has("Pattern Scanner", world.player),
        "New Caves Left": lambda state, world:
            state.has("Barrier - New Caves Right", world.player) or
            state.has("Pattern Scanner", world.player),
        "New Caves Top Computer": lambda state, world:
            state.has("Progressive Blade", world.player, 2),
        "New Caves Bottom Computer": lambda state, world:
            state.has("Progressive Blade", world.player, 3),
        "War Factory Boss": lambda state, world:
            state.has("Progressive Blade", world.player, 3) or
            state.has("Barrier - War Factory", world.player),
        "Guardian Zone": lambda state, world:
            state.has("Progressive Blade", world.player, 3) or
            state.has("Pattern Scanner", world.player),
        "Guardian Zone Middle": lambda state, world:
            state.has("Barrier - Guardian Zone Right", world.player) or
            (state.can_reach_region("Guardian Zone", world.player) and
            state.has("Barrier - Guardian Zone Left", world.player)) or
            state.has("Pattern Scanner", world.player),
        "Annihilator Factory Middle": lambda state, world:
            state.has("Barrier - Annihilator Factory", world.player) or
            state.has("Progressive Blade", world.player, 3),
        "Annihilator Factory Boss": lambda state, world:
            state.has("Pattern Scanner", world.player),
        "Old Base Computer": lambda state, world:
            state.has("Progressive Blade", world.player, 3),
        "Old Base Boss": lambda state, world:
            state.has("Pattern Scanner", world.player),
        "Tetron": lambda state, world:
            state.has("Barrier - Core", world.player) and
            (world.options.goal.value == 1 or
            (world.options.goal.value == 2 and
            state.has("Core Computer", world.player, 10)))},
    "Tetron": {},
    "Expel Computer": {}
}

regions_hard: Dict[str, Callable[[CollectionState, "HeroCoreWorld"], bool]] = {
    "Menu": {
        "Natural Caves": lambda state, world:
            True},
    "Natural Caves": {
        "Army Storage Left": lambda state, world:
            state.has("Barrier - Natural Caves", world.player),
        "Light Factory Top": lambda state, world:
            state.has("Barrier - Natural Caves", world.player),
        "Core": lambda state, world:
            state.has("Progressive Suit", world.player, 2) or
            world.options.expelskips or
            state.has("Pattern Scanner", world.player) or
            (state.can_reach_region("Light Factory Top", world.player) and
            state.has("Barrier - Light Factory Right", world.player)) or
            (state.can_reach_region("Army Storage Left", world.player) and
            state.has("Progressive Blade", world.player, 1)) or
            state.can_reach_region("Army Storage Right", world.player)},
    "Army Storage Left": {
        "Army Storage Right": lambda state, world:
            state.has("Barrier - Army Storage", world.player) or
            state.has("Progressive Blade", world.player, 2)},
    "Army Storage Right": {},
    "Control Computer": {},
    "Light Factory Top": {
        "Expel Computer": lambda state, world:
            state.has("Progressive Blade", world.player, 3)},
    "Light Factory Boss": {},
    "New Caves Boss": {},
    "War Factory Computer": {},
    "Guardian Zone Middle": {
        "Guardian Zone Right": lambda state, world:
            state.has("Progressive Blade", world.player, 2),
        "Guardian Zone Right Computer": lambda state, world:
            state.has("Barrier - Guardian Zone Top", world.player) and
            state.has("Progressive Blade", world.player, 2)},
    "Guardian Zone Right": {},
    "Guardian Zone Left Computer": {},
    "Guardian Zone Right Computer": {},
    "Annihilator Factory Right": {
        "Annihilator Factory Middle": lambda state, world:
            state.has("Progressive Blade", world.player, 3)},
    "Annihilator Factory Middle": {
        "Annihilator Factory Top": lambda state, world:
            state.has("Barrier - Annihilator Factory Bottom", world.player),
        "Annihilator Factory Boss": lambda state, world:
            state.has("Barrier - Annihilator Factory Top", world.player)},
    "Annihilator Factory Top": {},
    "Annihilator Factory Boss": {},
    "Old Base": {},
    "Core": {
        "Army Storage Left": lambda state, world:
            state.has("Progressive Blade", world.player, 1) or
            state.has("Pattern Scanner", world.player),
        "Army Storage Right": lambda state, world:
            state.has("Pattern Scanner", world.player),
        "Control Computer": lambda state, world:
            state.has("Progressive Suit", world.player, 2),
        "Light Factory Top": lambda state, world:
            state.has("Progressive Blade", world.player, 1) or
            state.has("Barrier - Light Factory Right", world.player) or
            state.has("Pattern Scanner", world.player),
        "Light Factory Boss": lambda state, world:
            state.has("Barrier - Light Factory Left", world.player),
        "New Caves Boss": lambda state, world:
            state.has("Barrier - New Caves", world.player),
        "War Factory Computer": lambda state, world:
            state.has("Progressive Blade", world.player, 3),
        "Guardian Zone Middle": lambda state, world:
            state.has("Barrier - Guardian Zone Bottom", world.player) or
            state.has("Barrier - Guardian Zon Top", world.player) or
            (state.has("Pattern Scanner", world.player) and
             state.has("Progressive Blade", world.player, 2)),
        "Guardian Zone Right": lambda state, world:
            state.has("Pattern Scanner", world.player),
        "Guardian Zone Left Computer": lambda state, world:
            state.has("Progressive Suit", world.player, 2) and
            state.has("Progressive Blade", world.player, 3),
        "Annihilator Factory Right": lambda state, world:
            state.has("Progressive Blade", world.player, 3),
        "Annihilator Factory Middle": lambda state, world:
            state.has("Pattern Scanner", world.player),
        "Old Base": lambda state, world:
            state.has("Pattern Scanner", world.player),
        "Tetron": lambda state, world:
            state.has("Barrier - Core", world.player) and
            (world.options.goal.value == 3 or
            (world.options.goal.value == 4 and
            state.has("Core Computer", world.player, 10)))},
    "Tetron": {},
    "Expel Computer": {}
}

regions_annihilation: Dict[str, Callable[[CollectionState, "HeroCoreWorld"], bool]] = {
    "Menu": {
        "Ciretako Middle": lambda state, world:
            True},
    "Ciretako Middle": {
        "Ciretako Top": lambda state, world:
            state.has("Barrier - Ciretako Top", world.player),
        "Ciretako Right": lambda state, world:
            state.has("Barrier - Ciretako Right", world.player) or
            state.has("Barrier - Ciretako Bottom", world.player)},
    "Ciretako Top": {},
    "Ciretako Right": {
        "Ciretako Bottom": lambda state, world:
            state.has("Barrier - Ciretako Bottom", world.player)},
    "Ciretako Bottom": {}
}