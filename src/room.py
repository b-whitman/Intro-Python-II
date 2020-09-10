# Implement a class to hold room information. This should have name and
# description attributes.

class Room():

    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items

    def add_item(self, item):
        self.items.append(item) 

    def rem_item(self, item):
        self.items.remove(item)

    def print_items(self):
        print('Items you can see:')
        for i in self.items:
            print(i)

    def __str__(self):
        return f'Name: {self.name}\nDescription: {self.description}'
