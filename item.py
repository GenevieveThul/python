import random


class Item:

    def __init__(self, name, healing, description):
        self.name = name
        self.healing = healing
        self.description = description



items = [
    Item("Comp Coin", 100, "You use the overwhelming power of the Comp Coin! +100 health!"),
    Item("Kaitlin", 8, "Kaitlin uses her MIT coding skills to help you out and gives you +8 health."),
    Item("The Game Grumps", 3, "You take out your phone and watch some game grumps. Your moral is restored and you gain +3 health!"),
    Item("Your Squad", 5, "Your squad give you some words of encouragement. They inspire you with the power of friendship! +5 health!"),
    Item("Friend Doggo", 4, "Friend doggo heals you with sunggles. You are overwhelmed by cuteness and gain +4 health!"),
    Item("Yourself", 1, "You sell your soul and use yourself. It doesn't help much. You gain +1 health out of pitty."),
    Item("Love", 15, " Love heals all! +15 health!"),
    Item("Dog Treats", 2, "You eat a dog treat....it's effective, i guess? +2 health"),
    Item("Dr.Bees", 3, "His breifcase full of bees aught to fix this! +3 health"),
    Item("Garfield", 3, "He's lazy, and loves lasagna. You can relate and gain +3 health"),
    Item("Meatball Sub", 15, " You eat your meatball sub. It's perfect, of course. You feel full and ready to fight! +15 health"),
]

def getRandomItem():
    return random.choice(items)

def getDescription(item):
    for i in items:
        if i.name == item:
            return i.description
