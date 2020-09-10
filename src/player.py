# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():

    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        self.items = items

    def add_item(self, item):
        self.items.append(item) 

    def rem_item(self, item):
        self.items.remove(item)

    def print_items(self):
        print('Items you are holding:')
        for i in self.items:
            print(i)

    def __str__(self):
        return f"Name: {self.name}\nCurrent Room: {self.current_room}"
    