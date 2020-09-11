from room import Room
from player import Player
from item import Item

# Declare all the rooms

item = {
    'coin':    Item('Gold Coin',
                        '''A simple gold coin. You wonder why the adventurers
                        left it behind.''')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been mostly emptied by
earlier adventurers. The only exit is to the south.""", [item['coin']]),
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

if __name__ == "__main__":
    
    player_name = input("Your name: ")

    player = Player(name=player_name, current_room=room['outside'], items=[])

    command = None

    while command != 'q':
        
        print(player.current_room)
        if player.current_room.items:
            player.current_room.print_items()
        else:
            print('You don\'t see any items.')
        command = input("> ")
        if len(command.split()) == 1:
            try:
                if command == 'n':
                    player.current_room = player.current_room.n_to
                elif command == 's':
                    player.current_room = player.current_room.s_to
                elif command == 'e':
                    player.current_room = player.current_room.e_to
                elif command == 'w':
                    player.current_room = player.current_room.w_to
            except AttributeError:
                print("You can't go that way")
        
        elif len(command.split()) == 2 and command.split()[0] == 'take':
            player.current_room.rem_item(item[command.split()[1]])
            player.add_item(item[command.split()[1]])

        elif len(command.split()) == 2 and command.split()[0] == 'drop':
            player.current_room.add_item(item[command.split()[1]])
            player.rem_item(item[command.split()[1]])


    exit()
