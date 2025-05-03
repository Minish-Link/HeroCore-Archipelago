# HeroCore-Archipelago Randomizer v.1.0.0
## By MinishLink

### Setup
To connect to a server, change the values in the ConnectionInfo.ini file to match your slot name, server address/port, and password (if there is one), then launch the game and press Connect on the main menu

### Where is the Music?
While I am able to modify and distribute the source code, I may not be allowed to distribute the music files, as they are outside the source project file, So to play it safe I did not include those files.
To get the music, you will need to download the original game at https://remar.se/daniel/herocore.php .
Then just dump the music files from there into the randomizer's music folder.

## What does this randomizer change?
This randomizer turns the Blaster, Suit, Blade, and Pattern Scanner upgrades into items that get shuffled into the randomizer's item pool. Each group of Barriers surrounding each of the Generators are also added as an item that removes the barriers (10 in Normal and Hard, 3 in Annihilator.) Optionally, Computers and Level ups can also be shuffled into the item pool.

Locations that contain items include:
- Powerups after defeating a Boss
-- Sends an additional check if Level ups are shuffled
- Destroying Generators
- Computers (If their items are shuffled)

This randomizer allows you to choose any of the three difficulties as your goal, with the option to additionally require obtaining all 10 Computers for True ending (Normal and Hard difficulty only)

## Notes
This early build of the randomizer does not support displaying messages received from the server. If you wish to see items that you are sending out, or see more information about items that you are receiving, a Text client is recommended. Furthermore, this randomizer does not save your map progress between sessions. If you quit the game and reconnect later, you will not be able to see which areas you've already been to, nor warp to any saves you've visited in previous sessions (unless you have the Pattern Scanner.) These issues will be fixed in later versions of the randomizer.