import random


class Enemy:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health
    def isAlive(self):
        return self.health > 0
class Manager:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health
    def isAlive(self):
        return self.health > 0

enemies = [
    Enemy("Just Monika.", 10, 10 ),
    Enemy("Responsability, the most fearful enemy of all.", 5, 5 ),
    Enemy("Fishbro. Half fish. Half bro.", 3, 7 ),
    Enemy("a Swarm of bees!!", 2, 8 ),
    Enemy("Monday.", 1, 3 ),
    Enemy("Waluigi.", 3, 5 ),
    Enemy("Plankton, he's after the secret formula!", 2, 6),
    Enemy("Brett", 6, 10 ),
    Enemy("Coding error. Just a total jerk of an enemy.", 4, 7),
    Enemy("Garry. He's risen form the dead!",2, 5),
    Enemy("Depression",4, 5),
]


def get():
    if random.randint(1, 4) == 1:
        return random.choice(enemies)
    else:
        return None
