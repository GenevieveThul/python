import location, player, item, enemy, random
from datetime import datetime
seed = input("Enter a seed: ")

tile = location.Location(seed + "0,0")

user = player.Player(input("What is your name: "))


x = 0
y = 0
tiles = {}
searched_tiles = []
def move(direction):
    global x, y
    if direction == "n":
        y += 1
    elif direction == "e":
        x += 1
    elif direction == "s":
        y -= 1
    elif direction == "w":
        x -= 1
    key = "{},{}".format(x, y)
    if key in tiles:
        return tiles [key]
    else:
        newtile = location.Location(seed + key)
        tiles [key] = newtile
        return newtile

running = True
while running and user.isAlive():
    print("You are in the {}".format(tile.name))
    print("(move) (search) (items) (health) (heal + name of item)", end='')
    if tile.isShop():
        print(" (shop)")
    else:
        print()
    if tile.enemy and tile.enemy.isAlive():
        print ("A new enemy has appeared! It's {} They have {} health!".format(tile.enemy.name, tile.enemy.health))
    command = input("> ")
    if command == "items":
        if user.inventory:
            print("You have: {}".format(user.getItems()))
        else:
            print("You have no items")

    elif command == "health":
            print("You have {} health!".format(user.health))

    elif command == "easter egg":
        print("Good job, you found an easter egg! Gold Star!")
    elif command == "hello":
        print("Don't talk to me.")
    elif command == "hi":
        print("Stop.")
    elif command == "how are you":
        print("I'm good, you?")
    elif command == "good":
        print("That's good :)")
    elif command == "sup":
        print("nmu?")
    elif command == "nm":
        print("cool cool")
    elif command == "adam":
        print("Hi, Welcome to Chilli's!")
    elif command == "pet friend doggo":
        print("Friend Doggo recieves pet and wags tail. He seems happy.")
    elif command == "ok":
        print("Now move around!")
    elif command == "cool":
        print("yee")
    elif command == "frisk":
        print("Did you mean: 'Chara'?")
    elif command == "chara":
        print("Did you mean: 'Frisk'?")
    elif command == "undertale":
        print("The game understands how simular it is to undertale, but assures you that its totally different. You feel determined.")
    elif command.startswith("move "):
        _, direction = command.split(" ", 1)
        if direction[0].lower() == "n":
            print("Go North")
            tile = move("n")
        elif direction[0].lower() == "e":
            print ("Go East")
            tile = move("e")
        elif direction[0].lower() == "s":
            print ("Go South")
            tile = move("s")
        elif direction[0].lower() == "w":
            print ("Go West")
            tile = move("w")

    elif command == "move":
        direction = input("N/E/S/W > ")[0].lower()
        if direction[0].lower() == "n":
            print("Go North")
            tile = move("n")
        elif direction == "e":
            print ("Go East")
            tile = move("e")
        elif direction == "s":
            print ("Go South")
            tile = move("s")
        elif direction == "w":
            print ("Go West")
            tile = move("w")

        else:
            print("Moving Cancelled")
    elif command == "search":
        if tile.seed in searched_tiles:
            print("You've already searched here")
            continue
        random.seed(seed + str(x) + str(y))
        if random.randint(1, 3) == 1:
            print("You seem to have found something!")
            user.addItem(item.getRandomItem())
        else:
            print("You search for a while, but find nothing.")
        searched_tiles.append(tile.seed)
    elif command == "fight":
        random.seed(datetime.now())
        print("(punch) (kick) (curb stomp) (magic attack) (slap) (spray)")
        while tile.enemy.isAlive() and user.isAlive():
            print("You have {} health!".format(user.health))
            command = input("FIGHT CLUB MODE > ")
            if command == "punch":
                if random.randint(1,5) < 5:
                    print(" Ya socked 'em man!'")
                    tile.enemy.health -= 3
                else:
                    print("You missed and lowkey embarassed yourself. Sad.")
            elif command == "curb stomp":
                if random.randint(1,5) == 1:
                    print("Wow! What a champ!")
                    tile.enemy.health -= 10
                else:
                    print("You stomp on your own foot instead of the enemy, ouch.")
            elif command == "kick":
                    if random.randint(1,5) < 5:
                        print("JACKIE CHAN SKILLS!!!")
                        tile.enemy.health -= 4
                    else:
                        print("You miss and somehow manage to trip yourself. Yikes.")

            elif command == "magic attack":
                    if random.randint(1,5) == 1:
                        print("You sommon all the power within, and blast them into oblivion!!")
                        tile.enemy.health -= 20
                    else:
                        print("You're not a wizard, you're just Harry!")

            elif command == "slap":
                    if random.randint(1,2) == 1:
                        print("*Slaps with glove* You challenge him to a duel!")
                        tile.enemy.health -= 2
                    else:
                        print("You slap them, but they remain unphased. They do not accept your duel.")

            elif command == "spray":
                    if random.randint(1,4) == 1:
                        print("You break out some bug spray and go crazy!")
                        tile.enemy.health -= 5
                    else:
                        print("You break out some bug spray, but the can is empty.")

            if tile.enemy.health > 0:
                user.health -= tile.enemy.damage
    elif command.startswith("heal"):
        _, i = command.split(" ", 1)
        if user.hasItem(i):
            print("{}".format(i))
            user.use(i)
            user.removeItem(i)
        else:
            print("You don't have {}".format(item))

    elif command == "shop":
        if tile.isShop():
            random.seed(datetime.now())
            print("Hello, how may I help you?")
            print("(buy) (sell) (what kind of shop is this?) (talk to manager)")
            command = input("SHOPPING MODE > ")
            if command == "what kind of shop is this?":
                if random.randint(1,5) < 5:
                    print(" *A wild Rhi appears, looking salty!* I know right? They won't even refund me!")
                else:
                    print("Sorry for the inconvienence. No refunds.")

            if command == "buy":
                print("the ice-cream machine is broken.")
            elif command == "sell":
                print("...this is a fast food establishment. Not a pawn shop.")
            elif command == "talk to manager":
                print("(my food was cold) (apply for job) (expired coupon)")
                command = input("MANAGER MODE > ")
                if command == "my food was cold":
                    if random.randint(1,5) < 5:
                        print(" Oh, so sorry to hear that, no refunds.")
                        tile.manager.health -= 3
                    else:
                        print("It's still warm. Don't lie.")

                elif command == "apply for job":
                    if random.randint(1,2) < 5:
                        print(" We'll keep in touch. ")
                        tile.manager.health -= 1
                    else:
                        print("We're not hiring at the moment, but we'll keep your resume.....in the trash.")

                elif command == "expired coupon":
                    if random.randint(1,6) < 5:
                        print(" You played your expired coupon and they didn't notice! ")
                        tile.manager.health -= 3
                    else:
                        print("You played your expired coupon and they noticed. They rip it up in front of you. Rude. ")

                elif command == "slap manager":
                    print("You go to slap the manager but they catch your hand mid-slap! They stare into your soul, an empty look in their eyes....you're gonna have a bad time.")

                    elif command == "punch manager":
                    print("You chicken out and decide a punch might be a bit much. Maybe try a slap ?")

                elif command == "kick manager":
                    print("You wind up for a kick then look down at the managers legs, they're made of steel! They must work out. You should work out more.... Anyways, No way you could go up against that. Maybe try a magic attack?")

                elif command == "curb stomp manager":
                    print("You are in a restaurant. There is not a curb in sight to stomp with! Maybe try something smaller like a kick?")

                elif command == "fight manager":
                    print("You cannot fight the manager. You'll get kicked out! ....but just between you and me, the fight commands are (punch manager) (kick manager) (curb stomp manager) (magic attack manager) and (slap manager) ")

                elif command == "magic attack manager":
                    print("You sommon all the power within, which isn't much. You see Gandolf in the distance, looking at you, dissapointed. You lose your confidence and decide not to attack with magic.")

                if tile.manager.health > 0:
                    user.health -= tile.manager.damage

    else:
        print("I...I don't know what to say to that...")
