# Write a class to hold player information, e.g. what room they are in
# currently.
# Fill out Player and Room classes in player.py and room.py #
class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
    def move(self, direction):
        newRoom = getattr(self.currentRoom, f'{direction}_to')
        if newRoom:
            self.currentRoom = newRoom
        else:
            print("can't do it")
    def __str__(self):
        return f'Player is in the {self.currentRoom}' 