import pygame
import time

class Game():

    def __init__(self, menu, level, score):
        self.menu = menu
        self.level = level
        self.score = score

    def play(self,level,char,speed):
        pygame.display.set_caption('Max vs. The Bullies')
        if self.score == 0:
            self.level == 1
        self.level = level + 1
        char.speed = speed
    
    def add_score(self, points):
        self.score += points
    
    def end(self, char):
        self.level = -1
        char.speed = 0

    def restart(self, level, score, char, enemies):
        self.level = level
        self.score = score
        char.health = 100
        enemies.attack_power = 0

class Character():

    def __init__(self, name, pos, speed, health=100,attack_power=2):
        # this init function will run for every instance of Player
        
        # since the value of self.name is a variable, we have to put 'name'
        # as an argument above
        self.name = name
        self.speed = speed
        self.health = health
        

        self.kind = False
        self.pos = pos
        self.attack_power = attack_power
        
        # print("%s instantiated at %s!" % (self.name, self.pos))

    # def move(self,dir):
    #     if dir == "left":
    #         self.pos["x"] -= self.speed
    #     elif dir == "right":
    #         self.pos["x"] += self.speed
    #     elif dir == "up":
    #         self.pos["y"] += self.speed
    #     elif dir == "down":
    #         self.pos["y"] -= self.speed

    def attack(self):
        return self.attack_power

    def heal(self,char):
        self.health += 20
        char.health += 20

    def hug(self, char):
        if char.health > 80:
            char.kind = True
        
    
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
    def __init__(self,name,pos,kind,speed,health=100):
        super().__init__(name,pos,kind)
        self.speed = speed
        self.dir = 1

    ### this is a way way extra feature
    # def roll(self):
    #     self.pos["x"] += 50
    #     #rotate image of badguy

    def move(self):
        modifier = 1
        if self.kind:
            modifier = -1
        if self.health < 100:
            modifier = 1
        self.pos["y"] += self.speed * modifier

    def attack(self, char):
        if ((self.pos["x"]+50) - (char.pos["x"]+25)) < 100 and ((char.pos["x"]+25) - (self.pos["x"]+50)) < 100 and ((self.pos["y"]+60) - (char.pos["y"]+25)) < 100 and ((char.pos["y"]+25) - (self.pos["y"]+60)) < 100 and self.pos["y"] < 900:
            char.health -= self.attack_power
        else:
            char.health = char.health

    def dance(self):
        self.attack_power = 0

class Projectile():

    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 8

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
        self.y -= 20

    def burn(self,char):
        char.health -= 40
        

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