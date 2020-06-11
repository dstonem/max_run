import sys
import os
import pygame
import random

from classes import Game
from classes import Character
from classes import Enemy


### GAME SETUP
fps   = 60  # frame rate
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

##### GAME
game = Game("PLAY",0,0)
#play = game.play()

### TEXT
def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def message_display(text, textSize, textPos):
    largeText = pygame.font.Font('freesansbold.ttf',textSize)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (textPos)
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

### consider using a dictionary to track the position of the badguys

## SPAWNING ENEMIES BASED ON LEVEL
index = 0
enemy_img = pygame.image.load("/Users/dylan/dc_projects/max_run/resources/badguy/run/1_000.png")
level = 0

def spawn(level):
    game.level = level
    if game.level == 1:
        for i in range(1,30):
            enemy = Enemy("badguy",{"x":random.randint(1,1100),"y":random.randint(-1000,0)},False,10)
            enemies.append(enemy)

            
            # if index == len(enemies):
            #     index = 0
    elif game.level == 2:
        for i in range(1,60):
            enemy = Enemy("badguy",{"x":random.randint(1,1100),"y":random.randint(-2000,0)},False,15)
            enemies.append(enemy)
            enemy_img = pygame.image.load("/Users/dylan/dc_projects/max_run/resources/badguy/run/1_000.png")
    elif game.level == 3:
        for i in range(1,100):
            enemy = Enemy("badguy",{"x":random.randint(1,1100),"y":random.randint(-3000,0)},False,20)
            enemies.append(enemy)
            enemy_img = pygame.image.load("/Users/dylan/dc_projects/max_run/resources/badguy/run/1_000.png")

### GAME LOOP
main = True
while main:
    win.fill(0)
    variables_display(f"Level: {game.level}",100)
    variables_display(f"Health: {max.health}",150)
    variables_display(f"Score: {game.score}",200)

    if game.level == 0:
        message_display("Max vs. The Bullies",115,(width/2,400))
        message_display("Press '8' to Start",28,(width/2,500))

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
            elif event.key==pygame.K_8:
                game.play(level)
                spawn(game.level)
            elif event.key==pygame.K_0:
                pass
                # start over somehow
            elif event.key == ord('p'):
                pygame.quit()
                sys.exit()
                main = False
            ########## NEXT STEPS -- make this work for every enemy, not just
            ########## the first enemy (use a for loop probably)
            ########## then make it so the kind badguys turn other badguys
            ########## then have the score go up (by more than a fireball)
            ########## for each badguy that gets turned kind
            if event.key==pygame.K_h:
                message_display("I LOVE YOU!",115,(max.pos["x"],max.pos["y"]))
                for enemy in enemies:
                    if ((max.pos["x"]+50) - (enemy.pos["x"]+25)) < 100 and ((enemy.pos["x"]+25) - (max.pos["x"]+50)) < 100 and ((max.pos["y"]+60) - (enemy.pos["y"]+25)) < 100 and ((enemy.pos["y"]+25) - (max.pos["y"]+60)) < 100 and enemy.pos["y"] < height:
                        max.hug(enemy)
                        max.heal()
                        game.add_score(20)
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
    

    for enemy in enemies:
        enemies[index].move()
        enemies[index].attack(max)
        index += 1
        if index > len(enemies)-1:
            index = 0


    ### ADDITIONAL SCORING THINGS
    for enemy in enemies:
        if enemy.pos["y"] <= 10 and enemy.pos["y"] >= -10 and game.level > 0:
            game.add_score(1)
        elif enemy.pos["y"] <= 970 and enemy.pos["y"] >= 950 and game.level > 0:
            game.add_score(5)
    
    ### LEVEL 
    if game.score >= 1000 and game.score < 3000:
        game.level = 2
    elif game.score >= 3000 and game.score <= 8000:
        game.level = 3

    #### LOSING
    if max.health >= -10 and max.health < 5:
        message_display("GAME OVER",115,(width/2,400))
        message_display("Press 'p' To Play Again",28,(width/2,500))
        message_display(f"Score: {game.score}",115,(width/2,200))
        for enemy in enemies:
            enemy.dance()
        count = 0
        for i in range(0,100):
            max_img = pygame.transform.scale(max_img, (count+100,125))
            count -= 1

    pygame.display.flip()
    clock.tick(fps) 