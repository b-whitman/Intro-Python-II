class Item():

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}:\t{self.description}'

    def __repr__(self):
        return self.name    
    