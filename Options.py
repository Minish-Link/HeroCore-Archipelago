from typing import List, TYPE_CHECKING, Dict
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Range, Toggle, DeathLink, Choice, OptionDict, DefaultOnToggle, OptionGroup

if TYPE_CHECKING:
    from . import HeroCoreWorld

class Goal(Choice):
    """
    Normal: Defeat Tetron in Core on Normal difficulty

    Normal True Ending: Obtain all 10 Computers and then defeat Tetron on Normal difficulty

    Hard: Defeat Tetron in Core on Hard difficulty

    Hard True Ending: Obtain all 10 Computers and then defeat Tetron on Hard difficulty

    Annihilation: Defeat Living Warmachine at the end of Annihilation difficulty
    """
    display_name="Goal"
    default=1
    option_normal=1
    option_normal_true_ending=2
    option_hard=3
    option_hard_true_ending=4
    option_annihilation=5

class ShuffleLevelUps(Toggle):
    """
    If enabled, the Levelups obtained from defeating bosses will be randomly shuffled into the multiworld
    Otherwise they will be locked to their vanilla locations.
    If your goal is Annihilation, this option does nothing
    """
    display_name = "Shuffle Level Ups"

class ShuffleExpel(Toggle):
    """
    If enabled, the ability to use Expel will be added as an item, and the Expel computer will be added as a location.
    If your goal is Annihilation, this option does nothing
    """
    display_name = "Shuffle Expel"

class ExpelSkips(Toggle):
    """
    Whether or not the logic should expect the player to use Expel to kill otherwise out-of-reach enemies
    """
    display_name = "Expel Skips"

class ShuffleComputers(DefaultOnToggle):
    """
    If enabled, computers will be added to the multiworld's item pool.
    Otherwise, the computers will be locked to their vanilla locations.
    """
    display_name = "Shuffle Computers"

@dataclass
class HeroCoreOptions(PerGameCommonOptions):
    goal:       Goal
    levelups:   ShuffleLevelUps
    expelskips: ExpelSkips
    deathlink:  DeathLink
    computers:  ShuffleComputers