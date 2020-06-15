import sys
import os
import pygame
import random

from classes_RUNNER import Game
from classes_RUNNER import Character
from classes_RUNNER import Enemy
from classes_RUNNER import Projectile

################################
### GAME SETUP
################################

fps   = 60  # frame rate
ani   = 4   # animation cycles
clock = pygame.time.Clock()
pygame.init()
timer = 0

width = 800
height = 800
win = pygame.display.set_mode((width,height))
backgrounds = [pygame.image.load("/Users/dylan/dc_projects/max_run/resources/lava.png"),pygame.image.load("/Users/dylan/dc_projects/max_run/resources/underwater.png"),pygame.image.load("/Users/dylan/dc_projects/max_run/resources/wall.png"),pygame.image.load("/Users/dylan/dc_projects/max_run/resources/beach.png"),pygame.image.load("/Users/dylan/dc_projects/max_run/resources/Battleground1.png"),pygame.image.load("/Users/dylan/dc_projects/max_run/resources/spooky.png"),pygame.image.load("/Users/dylan/dc_projects/max_run/resources/fh.jpeg"),pygame.image.load("/Users/dylan/dc_projects/max_run/resources/IMG_3540.jpg"),pygame.image.load("/Users/dylan/dc_projects/max_run/resources/trees.jpeg"),pygame.image.load("/Users/dylan/dc_projects/max_run/resources/map02_preview-01.png")]
backgroundbox = win.get_rect()
pygame.display.set_caption('Max vs. The Bullies')
# pygame.mixer.music.load('resources/maximum.mp3')
# pygame.mixer.music.play(0)

keys = [False, False, False, False]

##### GAME
game = Game("PLAY",0,0)

################################
### TEXT
################################

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

################################
### CHARACTERS
################################

max_img = pygame.image.load("/Users/dylan/dc_projects/max_run/resources/max.png")
max_img = pygame.transform.scale(max_img, (100,125))
max_img = pygame.transform.flip(max_img,0,180)
max = Character("Max",{"x":width/2,"y":height/4*3},(game.level*50)/2)

# list containing every bully he hugged
new_friends = []
friend = Enemy("badguy",{"x":random.randint(1,width-100),"y":random.randint(0,height)},True,0)

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

# animation for when enemies get knocked out
counter_ones = 0
counter_tens = 0
badguy_ko = []
for i in range(1,43):
    badguy_ko.append(pygame.image.load(f"/Users/dylan/dc_projects/max_run/resources/badguy/KO/4_0{counter_tens}{counter_ones}.png"))
    counter_ones += 1
    if counter_ones > 9:
        counter_ones = 0
        counter_tens += 1
run_count = 0

### consider using a dictionary to track the position of the badguys
################################
## SPAWNING ENEMIES BASED ON LEVEL
################################

index = 0
enemy_img = pygame.image.load("/Users/dylan/dc_projects/max_run/resources/badguy/run/1_000.png")

def spawn(level,num_badguys,level_length,enemy_speed):
    if game.level == level:
        for i in range(0,num_badguys):
            enemy = Enemy("badguy",{"x":random.randint(0,3)*(width/3)+100,"y":random.randint(-level_length,0)},False,enemy_speed)
            enemies.append(enemy)

levels = [1,2,3,4,5,6,7,8,9,10]
lvl_index = 0
for i in levels:
    if lvl_index > 0:
        spawn(lvl_index,lvl_index+10,lvl_index*1000,lvl_index+3)
        lvl_index += 1

# def spawn(level):
#     if game.level == 1:
#         for i in range(1,11):
#             enemy = Enemy("badguy",{"x":random.randint(0,3)*(width/3)+100,"y":random.randint(-1000,0)},False,2)
#             enemies.append(enemy)
#     elif game.level == 2:
#         for i in range(1,11):
#             enemy = Enemy("badguy",{"x":random.randint(0,3)*(width/3)+100,"y":random.randint(-1000,0)},False,3)
#             enemies.append(enemy)
#     elif game.level == 3:
#         for i in range(1,16):
#             enemy = Enemy("badguy",{"x":random.randint(0,3)*(width/3)+100,"y":random.randint(-1000,0)},False,3)
#             enemies.append(enemy)
#     elif game.level == 4:
#         for i in range(1,21):
#             enemy = Enemy("badguy",{"x":random.randint(0,3)*(width/3)+100,"y":random.randint(-2000,0)},False,4)
#             enemies.append(enemy)
#     elif game.level == 5:
#         for i in range(1,11):
#             enemy = Enemy("badguy",{"x":random.randint(0,3)*(width/3)+100,"y":random.randint(-1000,0)},False,5)
#             enemies.append(enemy)
#     elif game.level == 6:
#         for i in range(1,41):
#             enemy = Enemy("badguy",{"x":random.randint(0,3)*(width/3)+100,"y":random.randint(-3000,0)},False,5)
#             enemies.append(enemy)

bullets = []
extra_counter = 0

################################################################

################################
### GAME LOOP
################################

################################################################

main = True
won = False
while main:
    timer += 1
    win.fill(0)
    bg_counter = game.level
    backgrounds[bg_counter].scroll(0,1)
    win.blit(backgrounds[bg_counter], backgroundbox)
    extra_counter += 1
    if game.level > 0:
        variables_display(f"Level: {game.level}",100)
        variables_display(f"Health: {max.health}",150)
        variables_display(f"Score: {game.score}",200)

    if game.level == 0:
        message_display("Max vs. The Bullies",80,(width/2,height/3))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                keys[0]=True
            elif event.key==pygame.K_LEFT:
                keys[1]=True
            elif event.key==pygame.K_DOWN:
                keys[2]=True
            elif event.key==pygame.K_RIGHT:
                keys[3]=True
    #### ADVANCE LEVEL
            elif event.key==pygame.K_8:
                game.play(game.level,max,25)
                spawn(game.level,game.level+10,1000,game.level+2)
    #### RESTART
            elif event.key==pygame.K_0:
                ind = 0
                for i in enemies:
                    game.restart(0,0,max,enemies[ind])
                    ind += 1
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
                message_display("HUGZ!",115,(max.pos["x"],max.pos["y"]))
                for enemy in enemies:
                    if ((max.pos["x"]+50) - (enemy.pos["x"]+25)) < 100 and ((enemy.pos["x"]+25) - (max.pos["x"]+50)) < 100 and ((max.pos["y"]+60) - (enemy.pos["y"]+25)) < 100 and ((enemy.pos["y"]+25) - (max.pos["y"]+60)) < 100 and enemy.pos["y"] < height:
                        max.hug(enemy)
                        max.heal(enemy)
                        message_display(f"{enemy.health}",115,(enemy.pos["x"],enemy.pos["y"]))
                        game.add_score(20)
    ### FIREBALLS
            if event.key==pygame.K_SPACE:    
                # if len(bullets) < 5:  # This will make sure we cannot exceed 5 bullets on the screen at once
                bullets.append(Projectile(max.pos["x"], max.pos["y"], 6, (255,255,255)))
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            elif event.key==pygame.K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_RIGHT:
                keys[3]=False

        
        
            # 9 - Move player
        if keys[0]:
            max.pos["y"]-=max.speed
        elif keys[2]:
            max.pos["y"]+=max.speed
        if keys[1]:
            max.pos["x"]-=width/3
        elif keys[3]:
            max.pos["x"]+=width/3

        if max.pos["x"] > width:
            if keys[3]:
                max.pos["x"] -= width/3
        if max.pos["x"] < 0:
            if keys[1]:
                max.pos["x"] += width/3
        
    # - draw the screen elements
    win.blit(max_img, (max.pos["x"],max.pos["y"]))
    index=0
    for bullet in bullets:
        
        bullet.draw(win)
        ### the code below had a bug "list index out of range" if bullets were 
        ### shot at the end of the level... now Max knows his bullets can harm
        ### people if he fires flippantly

        if bullets[index].y < -10 and len(bullets)>0:
            del bullets[index]
    
    for i in enemies:
        for i in badguy_running:
            win.blit(badguy_running[run_count], (enemies[index].pos["x"],enemies[index].pos["y"])) 
            enemy_img.fill(0)
            if extra_counter % 3 == 0:
                run_count += 1
            if run_count == len(badguy_running)-1:
                run_count = 0
        index += 1
        if index > len(enemies)-1:
            index = 0
    
    for enemy in enemies:
        for bullet in bullets:
            if ((bullet.x+3) - (enemy.pos["x"]+3)) < 100 and ((enemy.pos["x"]+3) - (bullet.x+3)) < 100 and ((bullet.y+3) - (enemy.pos["y"]+3)) < 100 and ((enemy.pos["y"]+3) - (bullet.y+3)) < 100 and enemy.pos["y"] < height:
                bullet.burn(enemy)
                message_display(f"{enemy.health}",56,(enemy.pos["x"],enemy.pos["y"]))
                del bullets[index]
    
    
    for enemy in enemies:
        enemies[index].move()
        enemies[index].attack(max)
        if enemy.health < 1:
            enemy.speed = -1
            for i in badguy_running:
                extra_counter += 1
                if extra_counter % 10000 == 0:
                    run_count += 1
                win.blit(badguy_ko[run_count], (enemy.pos["x"],enemy.pos["y"]))
                
                if run_count == len(badguy_running)-1:
                    run_count = 0
            
            # if index > len(new_friends)-1:
            #     index = 0
            del enemies[index]
        ### add bullies to celebrate with Max at the end
        elif enemy.pos["y"] > height:
            del enemies[index]
        elif enemy.pos["y"] < -150 and enemy.kind:
            new_friends.append(enemy)
            del enemies[index]
        
        index += 1
        if index > len(enemies)-1:
            index = 0

    if enemies == [] and won == False:
        message_display("Press '8' to Advance",28,(width/2,height/2))

    ### ADDITIONAL SCORING THINGS
    for enemy in enemies:
        if enemy.pos["y"] <= 10 and enemy.pos["y"] >= -10 and game.level > 0:
            game.add_score(5)
        if enemy.pos["y"] <= height+10 and enemy.pos["y"] >= height-10 and game.level > 0:
            game.add_score(5)

    #### LOSING
    if max.health < 5:
        game.end(max)
    if game.level == -1:    
        message_display("GAME OVER",115,(width/2,400))
        message_display("Press '0' To Play Again",28,(width/2,500))
        message_display(f"Score: {game.score}",115,(width/2,200))
        for enemy in enemies:
            enemy.dance()
        max_img = pygame.transform.rotate(max_img, 90)

    if game.level > 0 and enemies == [] and new_friends:
        index = 0
        
        position_counterx = 0
        position_countery = 0
        for i in new_friends:
            new_friends[index] = Enemy("badguy",{"x":index*50,"y":game.level*80},True,0)
            index += 1
            position_counterx += 1
            column = 0
            if position_counterx > 10:
                column += 1
            position_countery += 1
            if position_countery > 10:
                position_countery = 1
            
            for i in badguy_running:
                win.blit(badguy_running[run_count], ((position_counterx+column*50),(position_countery*60)))
                run_count += 1
                if run_count == len(badguy_running)-1:
                    run_count = 0
            if index > len(new_friends)-1:
                index = 0
            
        if new_friends:
            message_display("New Friends!",80,(width/2,500))
            message_display(f"Score: {game.score}",80,(width/2,50))
            message_display("Go Max!",28,((position_counterx)+120,(position_countery*60)+20))
    
    if game.level > len(levels):
        won = True

    if won:
        message_display("You Win!",180,(width/2,100))
        message_display(f"Score: {game.score}",80,(width/2,250))

    print(new_friends)
    pygame.display.flip()
    clock.tick(fps)