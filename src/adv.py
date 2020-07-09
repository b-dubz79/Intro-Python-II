from room import Room
from player import Player

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
print(room['outside'].n_to)
#
# Main
#
# Plan: 
# Ask user to play
# Instantiate Person in 'outside' room
# Offer player to move into the cave
# If yes, change player's current room to 'foyer'
# From here, give player cardinal options based on what is available
# Change current room of player based on choice and print name/description
# If player doesn't type accepted command,  ask again

# Create the input command parser in adv.py which allows the program to receive player input and commands to move to rooms in the four cardinal directions. #
question = input("do you want to play y/n")
isPlaying = False

if question.lower().strip() == 'y':
    isPlaying = True
#   Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# Setting player variable to Player class instance. Player takes in currentRoom as an argument.  In this case it's "outside" which is defined above. 'room' is the dictionary name and 'outside' is a key that has a value of a 'Room' class instance. The Room class takes in name and description which is defined above in the Room instance.
player = Player(room['outside'])
while isPlaying:
    # start player outside
    print('butts',player.currentRoom)
    question = input('Would you like to go e, w, s, n, q?')
    if question == 'n':
        player.move(question)
    elif question == 'e':
        player.move(question)
    elif question == 'w':
        player.move(question)
    elif question == 's':
        player.move(question)
    elif question == 'q':
        isPlaying = False
    else:
        print('enter valid direction')
    
    

    


# * Waits for user input and decides what to do.

    
    






#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

###  name code if i want it for later ###
# playerName = input('What is your name, hero?')
    # player = Player(playerName, ' ')
    # print(f"Good luck in there {playerName} , I coded this cave with 3 days experience.")

    # question = input("Would you like to enter the beckoning cave? y/n")
    # if question.lower().strip() == 'y':
    #     # Make a new player object that is currently in the 'outside' room.
    #     player = Player({playerName}, room['outside'] )
    #     print(player)
