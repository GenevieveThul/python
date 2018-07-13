import random, enemy

descriptions = ["Spoopy", "Lovely", "Inspiring", "Mesmerizing", "Beautiful", "Calm", "Boolin", "Comp", "Hopeless", "Haunted"]
location_types = ["Forest", "River", "Cave", "McDonalds", "Burger King", "Valley", "Park", "Camp", "Place", "Mansion", "Taco Time", "Subway"]

class Location:
    def __init__(self, seed):
        self.seed = seed
        random.seed(seed)
        self.description = random.choice(descriptions)
        self.location_type = random.choice(location_types)
        self.name = "{} {}".format(
                self.description, self.location_type
        )
        self.enemy = enemy.get()

        if self.isShop():
            self.manager =  enemy.Manager("Manager", 2, 40 )

    def isShop(self):
        return self.location_type in ["McDonalds" , "Burger King" , "Taco Time" , "Subway"]
