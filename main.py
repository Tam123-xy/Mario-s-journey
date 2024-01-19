# *********************************************************
# Program: main.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL12
# Year: 2023/24 Trimester 1
# Names: TAM XIN YI | LEW LI JUN 
# IDs: 1231100707 | 1231100952 
# Emails: 1231100707@student.mmu.edu.my | 1231100952@student.mmu.edu.my
# Phones: 011-1102-6051 | 012-721-8442
# *********************************************************

import pygame
from sys import exit

# Mario Animation 
def Mario_animation(): 
     global Mario_surf, Mario_run_index
     Mario_run_index += 0.1
     if Mario_run_index >= len(Mario_run) : Mario_run_index = 0
     Mario_surf = Mario_run[int(Mario_run_index)]

# Check player's input 
def blocker_key(key):
    global blocker_image_index , correct_key, score
    if event.type == pygame.KEYDOWN:
        if event.key == key:
            blocker_image_index +=1
            correct_key +=1
            print (correct_key)
            score +=1
        else:
            correct_key = 0
     
# Print the 6 blockes in one screen
def show_blockers(blocker):
    coordinate = 200

    while coordinate <= 700:
            screen.blit(blocker_image[blocker], (coordinate, 230))
            blocker +=1
            coordinate += 100

            if blocker == 18:
                 blocker = 0
            
# Game foundation
pygame.init()
pygame.key.get_focused()
screen = pygame.display.set_mode((800, 400))  
pygame.display.set_caption("Mario's journey") 
font = pygame.font.Font('font/font.ttf', 50)
font2 = pygame.font.Font('font/font.ttf', 40)

# Background music
from pygame import mixer
mixer.init()
mixer.music.load('audio/start.wav')
mixer.music.play(1,0.0)

background = pygame.mixer.Sound('audio/background.wav')
addtime = pygame.mixer.Sound('audio/addtime.wav')
die = pygame.mixer.Sound('audio/die.wav')
warning = pygame.mixer.Sound('audio/warning.wav')
herewego = pygame.mixer.Sound('audio/herewego.wav')
score = pygame.mixer.Sound('audio/score.wav')

# intro and score screen surface
Mario_stand = pygame.image.load('grahics/Mario_stand.png').convert_alpha()
Mario_stand_scale = pygame.transform.rotozoom(Mario_stand,0,0.8)
Maria_stand_rect = Mario_stand_scale.get_rect(center = (400,165))

game_name = font.render("Mario's journey",False, ('White'))
game_name_rect = game_name.get_rect(center=(400,50))

star_message = font2.render('Send the star to the sky by pressing arrow key UP!',False, ('White'))
star_message_rect = star_message.get_rect(center = (400,280))

mus_message = font2.render('Smack the mushroom to the ground by pressing arrow key DOWN!',False, ('White'))
mus_message_rect = mus_message.get_rect(center = (400,310))

tur_message = font2.render('Kick off the turtle by pressing arrow key RiGHT!',False, ('White'))
tur_message_rect = tur_message.get_rect(center = (400,340))

start_message = font.render('Press SPACE to start the game!',False, ('Black'))
start_message_rect = star_message.get_rect(center = (450,370))

almost_message = font.render('You are almost there!',False, ('White'))
almost_message_rect = almost_message.get_rect(center = (400,340))

try_message = font.render('Try to break your heighest score!',False, ('White'))
try_message_rect = try_message.get_rect(center = (400,300))

congr_message = font.render('Well done! You break your highest score! ',False, ('White'))
congr_message_rect = congr_message.get_rect(center = (400,340))

# Game surface
sky_surf = pygame.image.load('grahics/sky.jpg').convert()
ground_surf = pygame.image.load('grahics/ground.png').convert()

star = pygame.image.load('grahics/blockers/star.png').convert()
star_s = pygame.transform.scale(star, (70, 70))

mus = pygame.image.load('grahics/blockers/mus.png').convert()
mus_s = pygame.transform.scale(mus, (70, 70))

tur = pygame.image.load('grahics/blockers/tur.png').convert()
tur_s = pygame.transform.scale(tur, (70, 70))

blocker_image = [mus_s, mus_s, star_s, 
                 tur_s, star_s, mus_s,
                 tur_s, mus_s, star_s,
                 star_s, tur_s, tur_s,
                 mus_s, star_s, tur_s,
                 star_s, mus_s, tur_s]

blocker_image_index = 0

# Mario running gif pictures
Mario_run_surf1 = pygame.image.load('grahics/Mario/1.png').convert()
Mario_run_scale1 = pygame.transform.scale(Mario_run_surf1, (150, 150))

Mario_run_surf2 = pygame.image.load('grahics/Mario/2.png').convert()
Mario_run_scale2 = pygame.transform.scale(Mario_run_surf2, (150, 150))

Mario_run_surf3 = pygame.image.load('grahics/Mario/3.png').convert()
Mario_run_scale3 = pygame.transform.scale(Mario_run_surf3, (150, 150))

Mario_run_surf4 = pygame.image.load('grahics/Mario/4.png').convert()
Mario_run_scale4 = pygame.transform.scale(Mario_run_surf4, (150, 150))

Mario_run_surf5 = pygame.image.load('grahics/Mario/5.png').convert()
Mario_run_scale5 = pygame.transform.scale(Mario_run_surf5, (150, 150))

Mario_run_surf6 = pygame.image.load('grahics/Mario/6.png').convert()
Mario_run_scale6 = pygame.transform.scale(Mario_run_surf6, (150, 150))

Mario_run_surf7 = pygame.image.load('grahics/Mario/7.png').convert()
Mario_run_scale7 = pygame.transform.scale(Mario_run_surf7, (150, 150))

Mario_run_surf8 = pygame.image.load('grahics/Mario/8.png').convert()
Mario_run_scale8 = pygame.transform.scale(Mario_run_surf8, (150, 150))

Mario_run_surf9 = pygame.image.load('grahics/Mario/9.png').convert()
Mario_run_scale9 = pygame.transform.scale(Mario_run_surf9, (150, 150))

Mario_run_surf10 = pygame.image.load('grahics/Mario/10.png').convert()
Mario_run_scale10 = pygame.transform.scale(Mario_run_surf10, (150, 150))

Mario_run_surf11 = pygame.image.load('grahics/Mario/11.png').convert()
Mario_run_scale11 = pygame.transform.scale(Mario_run_surf11, (150, 150))

Mario_run_surf12 = pygame.image.load('grahics/Mario/12.png').convert()
Mario_run_scale12 = pygame.transform.scale(Mario_run_surf12, (150, 150))

Mario_run =[Mario_run_scale1, Mario_run_scale2, Mario_run_scale3, Mario_run_scale4, Mario_run_scale5,
            Mario_run_scale6, Mario_run_scale7, Mario_run_scale8, Mario_run_scale9, Mario_run_scale10,
            Mario_run_scale11, Mario_run_scale12]

Mario_run_index =0
Mario_surf = Mario_run[Mario_run_index]

# Timer
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT,1000)
time = 7
text = '7'.rjust(3)

# Index initialize
game_active= False
correct_key = 0
score = 0
highest_score = 0
abc = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:

            # Timer
            if event.type == pygame.USEREVENT:
                        time -=1
                        text = str (time).rjust(3)
            
            # Successfully passed through 6 blockers continually, an extra 2 seconds will be added in the timer
            if correct_key == 6:
                correct_key = 0
                time +=2
                text = str (time).rjust(3)
                print('Extra time! +2s')

            # Check player's input 
            if blocker_image_index == 17: blocker_key(pygame.K_RIGHT)

            elif blocker_image_index == 16: blocker_key(pygame.K_DOWN)

            elif blocker_image_index == 15: blocker_key(pygame.K_UP)

            elif blocker_image_index == 14: blocker_key(pygame.K_RIGHT)

            elif blocker_image_index == 13: blocker_key(pygame.K_UP)

            elif blocker_image_index == 12: blocker_key(pygame.K_DOWN)

            elif blocker_image_index == 11: blocker_key(pygame.K_RIGHT)

            elif blocker_image_index == 10: blocker_key(pygame.K_RIGHT)

            elif blocker_image_index == 9: blocker_key(pygame.K_UP)

            elif blocker_image_index == 8: blocker_key(pygame.K_UP)

            elif blocker_image_index == 7: blocker_key(pygame.K_DOWN)

            elif blocker_image_index == 6: blocker_key(pygame.K_RIGHT)

            elif blocker_image_index == 5: blocker_key(pygame.K_DOWN)

            elif blocker_image_index == 4: blocker_key(pygame.K_UP)

            elif blocker_image_index == 3: blocker_key(pygame.K_RIGHT)

            elif blocker_image_index == 2: blocker_key(pygame.K_UP)

            elif blocker_image_index == 1: blocker_key(pygame.K_DOWN)

            else: blocker_key(pygame.K_DOWN)

            # initialize blocker_image_index when player is fully go throught the blocker_image list
            if blocker_image_index == 18:
                blocker_image_index = 0

            while score > highest_score:
             highest_score = score
             abc += 1

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                game_active = True
                score = 0
                time = 8
                correct_key = 0
                blocker_image_index = 0
                abc = 0
                print("Here we go!")
                herewego.play()
                background.play()
            
    if game_active:          
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        screen.blit(Mario_surf, (20, 150))
        Mario_animation()
        screen.blit(font.render(f'Score: {score}',True,('White')),(630,48))
        screen.blit(font.render(f'Time: {text}',True,('White')),(32,48))
        
        # Print the 6 blockes in one screen
        if blocker_image_index == 17: show_blockers(17)

        elif blocker_image_index == 16: show_blockers(16)
    
        elif blocker_image_index == 15: show_blockers(15)
            
        elif blocker_image_index == 14: show_blockers(14)
        
        elif blocker_image_index == 13: show_blockers(13)
            
        elif blocker_image_index == 12: show_blockers(12)
            
        elif blocker_image_index == 11: show_blockers(11)
           
        elif blocker_image_index == 10: show_blockers(10)
            
        elif blocker_image_index == 9: show_blockers(9)
           
        elif blocker_image_index == 8: show_blockers(8)
            
        elif blocker_image_index == 7: show_blockers(7)
            
        elif blocker_image_index == 6: show_blockers(6)
           
        elif blocker_image_index == 5: show_blockers(5)
            
        elif blocker_image_index == 4: show_blockers(4)
            
        elif blocker_image_index == 3: show_blockers(3)
            
        elif blocker_image_index == 2: show_blockers(2)
            
        elif blocker_image_index == 1: show_blockers(1)
            
        else: show_blockers(0)
     
        if time == 0:
            game_active = False
            die.play()
            background.stop()

    else: 
        screen.fill((94,129,162))
        screen.blit(Mario_stand_scale,Maria_stand_rect)
        screen.blit(game_name,game_name_rect)
        screen.blit(start_message,start_message_rect)

        score_message = font.render(f'Your score is {score}' ,False, ('White'))
        score_message_rect = score_message.get_rect(center = (400,280))

        highest_score_message = font.render(f'Your highest score is {highest_score}' ,False, ('White'))
        highest_score_message_rect = highest_score_message.get_rect(center = (400,310))

        last_highest_score_message = font.render(f'Your previous highest score is {highest_score - abc}' ,False, ('White'))
        last_highest_score_message_rect = last_highest_score_message.get_rect(center = (400,340))

        score_break_highest_message = font.render(f'Your highest score is {score}' ,False, ('White'))
        score_break_highest_message_rect = score_break_highest_message.get_rect(center = (400,310))

        if score == 0:
            screen.blit(mus_message,mus_message_rect)
            screen.blit(star_message,star_message_rect)
            screen.blit(tur_message,tur_message_rect)
        
        #lose
        elif score < highest_score: 
            screen.blit(score_message,score_message_rect)
            screen.blit(highest_score_message,highest_score_message_rect)
            screen.blit(try_message,try_message_rect)
            screen.blit(almost_message,almost_message_rect)

        #win
        elif score ==  highest_score and score!= 0: 
            screen.blit(score_break_highest_message, score_break_highest_message_rect)
            screen.blit(last_highest_score_message,last_highest_score_message_rect)
            screen.blit(congr_message,congr_message_rect)
            
    pygame.display.update()
    clock.tick(60)