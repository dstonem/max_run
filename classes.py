import pygame
import time

class Game():

    def __init__(self, menu, level):
        self.menu = menu
        self.level = level

    def play(self):
        ## need to make menu work
        #play = input("Press Enter to Play")
        pygame.display.set_caption('A bit Racey')
        if self.play == "":
            self.level = 1

class Character():

    def __init__(self, name, pos, img, speed=10, health=100,attack_power=5):
        # this init function will run for every instance of Player
        
        # since the value of self.name is a variable, we have to put 'name'
        # as an argument above
        self.name = name
        self.speed = 10
        self.health = health
        self.img = pygame.image.load("MaxRun/resources/max.png")

        self.kind = False
        self.pos = pos
        self.attack_power = attack_power
        
        print("%s instantiated at %s!" % (self.name, self.pos))

    def move(self,dir):
        if dir == "left":
            self.pos["x"] -= self.speed
        elif dir == "right":
            self.pos["x"] += self.speed
        elif dir == "up":
            self.pos["y"] += self.speed
        elif dir == "down":
            self.pos["y"] -= self.speed

    def attack(self):
        return self.attack_power

class Player(Character):
    
    def heal(self):
        self.health += 25
    def hug(self):
        self.kind = True
    
####
####
######### ENEMIES
####
####
class Enemy(Character):
    # if we want to re-initialize but inherit the properties from the 
    # parent/super class, we can use the super method and use the 
    # non-defaulted arguments (the ones that don't = something hard-coded)
    # as arguments here \/
    def __init__(self,name,pos,kind,speed):
        super().__init__(name,pos,kind)
        self.speed = speed
        self.dir = 1

    ### this is a way way extra feature
    # def roll(self):
    #     self.pos["x"] += 50
    #     #rotate image of badguy

    def move(self):
        time.sleep(0.1)
        self.pos["y"] += self.speed
        if self.kind:
            self.pos["y"] -= self.speed

    def attack(self, char):
        if (char.pos["x"] - self.pos["x"]) < 50 and (char.pos["y"] - self.pos["y"]) < 50:
            char.health -= self.attack_power

# enemy1 = Enemy("badguy1",{"x":0,"y":0},False)
# print(enemy1.pos)
# #enemy1.roll()
# print(enemy1.pos)

# max = Player("Max",{"x":60,"y":0})
# print(max.pos)
# # the function "hug" (found in class Player(Character)) runs the code that
# # changes the "kind" property to True
# # NEXT STEPS: have the logic for the enemies be "when Max hugs" change
# ## enemies' kind to True - which turns the enemies around and turns other enemies
# ### enemies to kind which turns them around
# #### WOULD BE SUPER COOL TO HAVE ALL THE ENEMIES MAX TURNED KIND PARTY WITH HIM AT THE END - by tracking how many get turned kind and generating a party scene with that many enemies dancing with Max
# max.hug()
# print(max.kind)

# print(enemy1.kind)

# # see the "attack" function within Enemy(Character) -- though this should move to the super class so all have an attack available universally (shouldn't be a defaulted value)
# enemy1.attack(max)
# print(max.health)
# # since we have the "name" argument above 
# player1 = Player("Max")
# # second instance of this class (we "instantiate" it)
# player2 = Player("Dad")

# player1.move("left")
# print("Having moved left, %s's new position is: %s" % (player1.name, player1.pos))

# player2.move("left")
# print("Having moved left, %s's new position is: %s" % (player2.name, player2.pos))
