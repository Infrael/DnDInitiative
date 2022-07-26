class Hero:
    def __init__(self, name, location, initiative=0):
        self.name = name
        self.image_location = location
        self.initiative = initiative
        self.amount = 1

    def __repr__(self):
        return f"{str(self.name)} has rolled {self.initiative} Initiative"


class Enemy:
    def __init__(self, name, initiative, amount):
        self.name = name
        self.initiative = initiative
        self.amount = amount

    def __repr__(self):
        if self.amount == 1:
            return f" {str(self.name)} has rolled {self.initiative} Initiative"
        else:
            return f" A group of {self.amount} {str(self.name)[:-1]} have rolled {self.initiative} Initiative"
