# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items = []):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return f'{self.name, self.current_room, self.items}'
    
    def set_room(self, current_room):
        self.current_room = current_room

    def get_item(self, item):
        self.items.append(item)
        print(f'You picked up {self.items} and added it to your inventory.')
    
    def drop_item(self, item):
        self.inventory.remove(item)
# player = Player("Christine", "room", "weapon")
# print(Player.__str__(player))