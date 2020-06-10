import pygame
import random

from classes import Game
from classes import Character
from classes import Enemy

pygame.init()

width = 1280
height = 960
win = pygame.display.set_mode((width,height))
pygame.display.set_caption('MaxRun')

game = Game("PLAY",1)

#play = game.play()

### Characters 

enemy = pygame.image.load("max_run/resources/badguy/run/1_000.png")
max = Character("Max",{"x":0,"y":800})
max = pygame.image.load("max_run/resources/max.png")

enemies = []

## SPAWNING ENEMIES BASED ON LEVEL
if game.level == 1:
    for i in range(1,10):
        enemy = Enemy("badguy",{"x":random.randint(1,1100),"y":random.randint(-1000,0)},False,5)
        enemies.append(enemy)
elif game.level == 2:
    for i in range(1,20):
        enemy = Enemy("badguy",{"x":random.randint(1,1100),"y":random.randint(-2000,0)},False,10)
elif game.level == 3:
    for i in range(1,30):
        enemy = Enemy("badguy",{"x":random.randint(1,1100),"y":random.randint(-3000,0)},False,20)
    
while True:
    win.fill(0)

    # 6 - draw the screen elements
    win.blit(max, (max.pos["x"],max.pos["y"]))


    index = 0
    for i in enemies:
        enemies[index].move()
        index += 1
        if index > len(enemies)-1:
            index = 0
        #print(enemies[index].pos)
        

    