from room import Room
from player import Player
from item import Item
# Declare all the rooms

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
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
print("Welcome, adventurer,")
player_name = input("Pray tell, what is your name?\n")
# Make a new player object that is currently in the 'outside' room.
player = Player(player_name, room['outside'])
print(f"Welcome brave {player.name}!\nWelcome to the land of Ardamesia, \
a land of mystery and intregue.\nAre you ready to get started?\n\
Your adventure awaits!\n")

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
user_input = ""
bad_input = "Invalid Input, please try again."

while user_input != 'q' and user_input != "quit":
    print(player.location)
    user_input = input(":").lower()

    if " " in user_input:
        verb, noun = user_input.split(" ", 1)
        no_noun = False

    else:
        no_noun = True

    if no_noun:
        if user_input in ['n','s','e','w']:
            # If the user enters a cardinal direction, attempt to move to the room there.
            player.move(user_input) # move method is from in Player class, it has direction and location information
            
        elif user_input == 'i' or user_input == 'inventory':
                player.list_inventory() # list_inventory method is from Player class
        elif user_input == 'l' or user_input == 'look':
                player.location.list_items() # list_items method is from Player class
        elif user_input == 'q' or user_input == "quit":
                print("Thank you for playing!")
        else:
               print(bad_input)
    else:
        if verb == 'get':
            player.get_item(noun)
        elif verb == 'drop':
            player.drop_item(noun)
        else:
            print(bad_input)
    print()