# Implement a class to hold room information. This should have name and
# description attributes.
from items import Item 
class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None


    def __str__(self):
        return f'{self.name} - Description: {self.description}. You see the following items: {self.items}'

    