import sys
import os
import pygame
import random

from classes import Game
from classes import Character
from classes import Enemy


### GAME SETUP
fps   = 30  # frame rate
ani   = 4   # animation cycles
clock = pygame.time.Clock()
pygame.init()

width = 1280
height = 960
win = pygame.display.set_mode((width,height))
backdrop = pygame.image.load("/Users/dylan/dc_projects/max_run/resources/fireballs/1/1.png").convert()
backdropbox = win.get_rect()
pygame.display.set_caption('MaxRun')

keys = [False, False, False, False]
game = Game("PLAY",1,0)
#play = game.play()

### TEXT
def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width/2),(height/2))
    win.blit(TextSurf, TextRect)

def variables_display(text,posY):
    largeText = pygame.font.Font('freesansbold.ttf',28)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((100),(posY))
    win.blit(TextSurf, TextRect)

### CHARACTERS


max_img = pygame.image.load("/Users/dylan/dc_projects/max_run/resources/max.png")
max_img = pygame.transform.scale(max_img, (100,125))
max_img = pygame.transform.flip(max_img,0,180)
max = Character("Max",{"x":600,"y":650},25)

enemies = []
badguy_running = []
counter_ones = 0
counter_tens = 0
# append the images to enable the running visual effect
for i in range(1,43):
    badguy_running.append(pygame.image.load(f"/Users/dylan/dc_projects/max_run/resources/badguy/run/1_0{counter_tens}{counter_ones}.png"))
    counter_ones += 1
    if counter_ones > 9:
        counter_ones = 0
        counter_tens += 1
run_count = 0

## SPAWNING ENEMIES BASED ON LEVEL
index = 0
if game.level == 1:
    for i in range(1,10):
        enemy = Enemy("badguy",{"x":random.randint(1,1100),"y":random.randint(-1000,0)},False,10)
        enemies.append(enemy)

        enemy_img = pygame.image.load("/Users/dylan/dc_projects/max_run/resources/badguy/run/1_000.png")
        # if index == len(enemies):
        #     index = 0
elif game.level == 2:
    for i in range(1,20):
        enemy = Enemy("badguy",{"x":random.randint(1,1100),"y":random.randint(-2000,0)},False,15)
        enemies.append(enemy)
        enemy_img = pygame.image.load("/Users/dylan/dc_projects/max_run/resources/badguy/run/1_000.png")
elif game.level == 3:
    for i in range(1,30):
        enemy = Enemy("badguy",{"x":random.randint(1,1100),"y":random.randint(-3000,0)},False,20)
        enemies.append(enemy)
        enemy_img = pygame.image.load("/Users/dylan/dc_projects/max_run/resources/badguy/run/1_000.png")

### GAME LOOP
while True:
    win.fill(0)
    variables_display(f"Level: {game.level}",100)
    variables_display(f"Health: {max.health}",150)
    variables_display(f"Score: {game.score}",200)

    win.blit(backdrop, backdropbox)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_w:
                keys[0]=True
            elif event.key==pygame.K_a:
                keys[1]=True
            elif event.key==pygame.K_s:
                keys[2]=True
            elif event.key==pygame.K_d:
                keys[3]=True
            elif event.key == ord('p'):
                pygame.quit()
                sys.exit()
                main = False
            ########## NEXT STEPS -- make this work for every enemy, not just
            ########## the first enemy (use a for loop probably)
            ########## then make it so the kind badguys turn other badguys
            ########## then have the score go up (by more than a fireball)
            ########## for each badguy that gets turned kind
            if event.key==pygame.K_SPACE:
                message_display("I LOVE YOU!")
                max.hug(enemy)
                # if len(bullets) < 5:  # This will make sure we cannot exceed 5 bullets on the screen at once
                #     bullets.append(projectile(round(max.x+max.width//2), round(max.y + max.height//2), 6, (0,0,0))) 
# This will create a bullet starting at the middle of the character
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False

        
            # 9 - Move player
        if keys[0]:
            max.pos["y"]-=max.speed
        elif keys[2]:
            max.pos["y"]+=max.speed
        if keys[1]:
            max.pos["x"]-=max.speed
        elif keys[3]:
            max.pos["x"]+=max.speed
        
    # - draw the screen elements
    win.blit(max_img, (max.pos["x"],max.pos["y"]))
    
    for i in enemies:
        for i in badguy_running:
            win.blit(badguy_running[run_count], (enemies[index].pos["x"],enemies[index].pos["y"])) 
            enemy_img.fill(0)
            run_count += 1
            if run_count == len(badguy_running)-1:
                run_count = 0
        index += 1
        if index > len(enemies)-1:
            index = 0
    
    
    for i in enemies:
        enemies[index].move()
        enemies[index].attack(max)
        index += 1
        if index > len(enemies)-1:
            index = 0
        #print(enemies[index].pos)
        
    pygame.display.flip()
    clock.tick(fps)
    