class Hero:
    def __init__(self, name, location):
        self.name = name
        self.image_location = location


class Enemy:
    def __init__(self, name, initiative, amount, hp, hero_check):
        self.name = name
        self.initiative = initiative
        self.amount = amount
        self.hp = hp
        self.is_hero = hero_check
