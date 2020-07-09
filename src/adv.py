from room import Room
from player import Player
from items import Item
from random import seed
from random import randint

# Items
seed(1)
for _ in range(10):
    value= randint(0,10)

coin = Item('Gold Coin', 'Round gold color coin', value)
food = Item('Apple', "Yummy red juicy apple", value)
treasure_chest = Item('Treasure Chest','Chest full of gold and gems', 200)
weapon = Item('Sword', 'Bright shiny sword to defeat your enemies!', value)
potion = Item('Restore health potion','Use this potion to give you full health!', value)

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [potion]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [weapon, coin]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [food, coin]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [potion]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [treasure_chest]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Player1', room['outside'])
print(f'{player.current_room}')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    move = input("\nWhich way would you like to move? Enter 'n', 's' 'e' or 'w'?").split()
    if move[0] in ('n', 's', 'e', 'w'):
        if hasattr(player.current_room, f'{move[0]}_to'):
            player.set_room(getattr(player.current_room, f'{move[0]}_to'))
            print(f'You are now in {player.current_room.name}\n')
            print(f'{player.current_room.description}')
            print(f'{player.items}')
        
    elif move[0] == 'q':
        exit()

    else:
        print("Sorry invalid entry please enter 'n' for North, 's' for South, 'e' for East, 'w' for West, or 'q' for quit" )

