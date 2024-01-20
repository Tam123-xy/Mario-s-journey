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

# Mario animation 
def Mario_run_animation(): 
     global Mario_run_surf, Mario_run_index
     Mario_run_index += 0.1
     if Mario_run_index >= len(Mario_run) : Mario_run_index = 0
     Mario_run_surf = Mario_run[int(Mario_run_index)]

def Mario_score_animation():
    global Mario_score_surf, Mario_score_index
    Mario_score_index += 0.1
    if Mario_score_index >= len(Mario_score) : Mario_score_index = 0
    Mario_score_surf = Mario_score[int(Mario_score_index)]
    
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
font3 = pygame.font.Font('font/font.ttf', 60)

# Background music
from pygame import mixer
mixer.init()
mixer.music.load('audio/start.wav')
mixer.music.play(1,0.0)

background = pygame.mixer.Sound('audio/background.wav')
addtime = pygame.mixer.Sound('audio/addtime.wav')
lose = pygame.mixer.Sound('audio/lose.wav')
win = pygame.mixer.Sound('audio/Course Clear (Super Mario) - QuickSounds.com.wav')
warning = pygame.mixer.Sound('audio/warning.wav')
herewego = pygame.mixer.Sound('audio/herewego.wav')
score = pygame.mixer.Sound('audio/score.wav')

# Intro and score screen surface
Mario_stand = pygame.image.load('grahics/Mario_stand.png').convert_alpha()
Mario_stand_scale = pygame.transform.rotozoom(Mario_stand,0,0.8)
Maria_stand_rect = Mario_stand_scale.get_rect(center = (400,135))

game_name = font.render("Mario's journey",False, ('White'))
game_name_rect = game_name.get_rect(center=(400,20))

star_message = font2.render('Send the star to the sky by pressing arrow key UP !',False, ('White'))
star_message_rect = star_message.get_rect(center = (400,250))

mus_message = font2.render('Smack the mushroom to the ground by pressing arrow key DOWN !',False, ('White'))
mus_message_rect = mus_message.get_rect(center = (400,280))

tur_message = font2.render('Kick off the turtle by pressing arrow key RIGHT !',False, ('White'))
tur_message_rect = tur_message.get_rect(center = (400,310))

start_message = font.render('Press SPACE to start the game !',False, ('Black'))
start_message_rect = star_message.get_rect(center = (470,370))
start_message2 = font3.render('Press SPACE to start the game !',False, ('Black'))

almost_message = font3.render('You are almost there!',False, ('White'))
almost_message_rect = almost_message.get_rect(center = (400,60))

try_message = font3.render('Try to break your heighest score !',False, ('White'))
try_message_rect = try_message.get_rect(center = (400,130))

congr_message = font3.render('Well done ! You break your highest score ! ',False, ('White'))
congr_message_rect = congr_message.get_rect(center = (400,130))

tip_message = font2.render('Go throught 5 blockers continually will get an extra 2 seconds.',False, ('White'))
tip_message_rect = tip_message.get_rect(center = (400,340))

# Game surface
sky_surf = pygame.image.load('grahics/sky.jpg').convert()
ground_surf = pygame.image.load('grahics/ground.png').convert()

star = pygame.image.load('grahics/blockers/star.png').convert_alpha()
star_s = pygame.transform.scale(star, (70, 70))

mus = pygame.image.load('grahics/blockers/mus.png').convert()
mus_s = pygame.transform.scale(mus, (70, 70))

tur = pygame.image.load('grahics/blockers/tur.png').convert_alpha()
tur_s = pygame.transform.scale(tur, (80, 70))

blocker_image = [mus_s, tur_s, star_s, 
                 tur_s, star_s, mus_s,
                 tur_s, mus_s, star_s,
                 mus_s, star_s, tur_s,
                 star_s, mus_s, tur_s,
                 star_s, tur_s, mus_s,]

blocker_image_index = 0

# Mario gif pictures
Mario_run_surf1 = pygame.image.load('grahics/run/frame_00_delay-0.1s.png').convert_alpha()
Mario_run_scale1 = pygame.transform.scale(Mario_run_surf1, (200, 200))

Mario_run_surf2 = pygame.image.load('grahics/run/frame_01_delay-0.1s.png').convert_alpha()
Mario_run_scale2 = pygame.transform.scale(Mario_run_surf2, (200, 200))

Mario_run_surf3 = pygame.image.load('grahics/run/frame_02_delay-0.1s.png').convert_alpha()
Mario_run_scale3 = pygame.transform.scale(Mario_run_surf3, (200, 200))

Mario_run_surf4 = pygame.image.load('grahics/run/frame_03_delay-0.1s.png').convert_alpha()
Mario_run_scale4 = pygame.transform.scale(Mario_run_surf4, (200, 200))

Mario_run_surf5 = pygame.image.load('grahics/run/frame_04_delay-0.1s.png').convert_alpha()
Mario_run_scale5 = pygame.transform.scale(Mario_run_surf5, (200, 200))

Mario_run_surf6 = pygame.image.load('grahics/run/frame_05_delay-0.1s.png').convert_alpha()
Mario_run_scale6 = pygame.transform.scale(Mario_run_surf6, (200, 200))

Mario_run_surf7 = pygame.image.load('grahics/run/frame_06_delay-0.1s.png').convert_alpha()
Mario_run_scale7 = pygame.transform.scale(Mario_run_surf7, (200, 200))

Mario_run_surf8 = pygame.image.load('grahics/run/frame_07_delay-0.1s.png').convert_alpha()
Mario_run_scale8 = pygame.transform.scale(Mario_run_surf8, (200, 200))

Mario_run_surf9 = pygame.image.load('grahics/run/frame_08_delay-0.1s.png').convert_alpha()
Mario_run_scale9 = pygame.transform.scale(Mario_run_surf9, (200, 200))

Mario_run_surf10 = pygame.image.load('grahics/run/frame_09_delay-0.1s.png').convert_alpha()
Mario_run_scale10 = pygame.transform.scale(Mario_run_surf10, (200, 200))

Mario_run_surf11 = pygame.image.load('grahics/run/frame_10_delay-0.1s.png').convert_alpha()
Mario_run_scale11 = pygame.transform.scale(Mario_run_surf11, (200, 200))

Mario_run_surf12 = pygame.image.load('grahics/run/frame_11_delay-0.1s.png').convert_alpha()
Mario_run_scale12 = pygame.transform.scale(Mario_run_surf12, (200, 200))

Mario_run =[Mario_run_scale1, Mario_run_scale2, Mario_run_scale3, Mario_run_scale4, Mario_run_scale5,
            Mario_run_scale6, Mario_run_scale7, Mario_run_scale8, Mario_run_scale9, Mario_run_scale10,
            Mario_run_scale11, Mario_run_scale12]

Mario_run_index =0
Mario_run_surf = Mario_run[Mario_run_index]

Mario_score_surf1 = pygame.image.load('grahics/score/frame_0_delay-0.1s.png').convert_alpha()
Mario_score_scale1 = pygame.transform.scale(Mario_score_surf1, (300,300))

Mario_score_surf2 = pygame.image.load('grahics/score/frame_1_delay-0.1s.png').convert_alpha()
Mario_score_scale2 = pygame.transform.scale(Mario_score_surf2, (300,300))

Mario_score_surf3 = pygame.image.load('grahics/score/frame_2_delay-0.1s.png').convert_alpha()
Mario_score_scale3 = pygame.transform.scale(Mario_score_surf3, (300,300))

Mario_score_surf4 = pygame.image.load('grahics/score/frame_3_delay-0.1s.png').convert_alpha()
Mario_score_scale4 = pygame.transform.scale(Mario_score_surf4, (300,300))

Mario_score_surf5 = pygame.image.load('grahics/score/frame_4_delay-0.1s.png').convert_alpha()
Mario_score_scale5 = pygame.transform.scale(Mario_score_surf5, (300,300))

Mario_score_surf6 = pygame.image.load('grahics/score/frame_5_delay-0.1s.png').convert_alpha()
Mario_score_scale6 = pygame.transform.scale(Mario_score_surf6, (300,300))

Mario_score_surf7 = pygame.image.load('grahics/score/frame_6_delay-0.1s.png').convert_alpha()
Mario_score_scale7 = pygame.transform.scale(Mario_score_surf7, (300,300))

Mario_score_surf8 = pygame.image.load('grahics/score/frame_7_delay-0.1s.png').convert_alpha()
Mario_score_scale8 = pygame.transform.scale(Mario_score_surf8, (300,300))

Mario_score =[Mario_score_scale1, Mario_score_scale2, Mario_score_scale3, Mario_score_scale4, Mario_score_scale5,
              Mario_score_scale6, Mario_score_scale7, Mario_score_scale8]

Mario_score_index =0
Mario_score_surf = Mario_score[Mario_score_index]


# Timer
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT,1000)
text = '15'.rjust(3)

# Index initialize
game_active= False
correct_key = 0
score = 0
highest_score = 0
difference = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # game_active = True, means game is start
        if game_active: 

            # Timer
            if event.type == pygame.USEREVENT:
                        time -=1
                        text = str (time).rjust(3)
            
            # Successfully passed through 5 blockers continually, an extra 2 seconds will be added in the timer
            if correct_key == 5:
                correct_key = 0
                time +=2
                text = str (time).rjust(3)
                print('Extra time! +2s')
                addtime.play()
            
            # Sound effects for some conditions
            if time == 3:
                warning.play()

            if time <=3:
                background.stop()

            if time >3:
                warning.stop()

# Input
                
            # Check player's input 
            if blocker_image_index == 17: blocker_key(pygame.K_DOWN)

            elif blocker_image_index == 16: blocker_key(pygame.K_RIGHT)

            elif blocker_image_index == 15: blocker_key(pygame.K_UP)

            elif blocker_image_index == 14: blocker_key(pygame.K_RIGHT)

            elif blocker_image_index == 13: blocker_key(pygame.K_DOWN)

            elif blocker_image_index == 12: blocker_key(pygame.K_UP)

            elif blocker_image_index == 11: blocker_key(pygame.K_RIGHT)

            elif blocker_image_index == 10: blocker_key(pygame.K_UP)

            elif blocker_image_index == 9: blocker_key(pygame.K_DOWN)

            elif blocker_image_index == 8: blocker_key(pygame.K_UP)

            elif blocker_image_index == 7: blocker_key(pygame.K_DOWN)

            elif blocker_image_index == 6: blocker_key(pygame.K_RIGHT)

            elif blocker_image_index == 5: blocker_key(pygame.K_DOWN)

            elif blocker_image_index == 4: blocker_key(pygame.K_UP)

            elif blocker_image_index == 3: blocker_key(pygame.K_RIGHT)

            elif blocker_image_index == 2: blocker_key(pygame.K_UP)

            elif blocker_image_index == 1: blocker_key(pygame.K_RIGHT)

            else: blocker_key(pygame.K_DOWN)

            # initialize blocker_image_index when player is fully go throught the blocker_image list
            if blocker_image_index == 18:
                blocker_image_index = 0
                        
            # Compare the score is beggest than highest score every single blocker loop
            while score > highest_score:
             highest_score = score
             difference += 1
 
        # game_active = False, means game not start yet and the surface will go to intro or lose or win screen
        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 

                # Press SPACE to start the game 
                game_active = True 

                # Initialize the indexs again
                score = 0
                time = 16
                correct_key = 0
                blocker_image_index = 0
                difference = 0
                previous_score = 0
                previous_score = score
                print("Here we go!")
                
                # Sound effects
                herewego.play()
                background.play(loops = -1)
                mixer.music.stop()
                lose.stop()
                win.stop()
                
                # File save score
                def save_previous_score(previous_score):
                    with open("score2.txt", "w") as file:
                        file.write(str(previous_score))
                def load_previous_score():
                    try:
                        with open('score2.txt', 'r') as file:
                            previous_score = int(file.read().strip())
                            previous_score = score
                            save_previous_score(previous_score)
                            return previous_score
                    except FileNotFoundError:
                        return  0
                previous_score = score
                previous_score = load_previous_score()

                def save_score(score, highest_score):
                    with open("score.txt", "w") as file:
                        file.write(f"{score}\n{highest_score}")  
                def load_score():
                    try:
                        with open("score.txt", "r") as file:
                            lines = file.readlines()
                            if len(lines) >= 2 :
                                score = 0
                                highest_score = int(lines[1].strip())
                                return score, highest_score
                            else:
                                return 0, 0
                    except FileNotFoundError:                        
                        return 0, 0
                score, highest_score = load_score()
    
# Output
                
    # game_active = True, means game is start. 
    if game_active:       

        # Game surface
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        screen.blit(Mario_run_surf, (-15, 100))
        Mario_run_animation()
        screen.blit(font.render(f'Score: {score}',True,('White')),(630,48))
        screen.blit(font.render(f'Highest score: {highest_score - difference}',True,('White')),(510,18))
        screen.blit(font.render(f'Time: {text}',True,('White')),(32,48))

        save_previous_score(previous_score)
        save_score(score, highest_score)

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
        

        # If the timmer reaches zero the game will end and go to lose or win screen
        if time == 0:
            game_active = False
            
            # Sound effects for lose and win screen
            if difference == 0 and score != 0:
                lose.play()

            elif difference > 0 :
                win.play()

    # game_active = False, means game not start yet and the surface will go to intro or lose or win screen
    else:   
        screen.fill((94,129,162)) 

        score_message = font3.render(f'Your score is {score}' ,False, ('White'))
        score_message_rect = score_message.get_rect(center = (400,270))

        highest_score_message = font3.render(f'Your highest score is {highest_score}' ,False, ('White'))
        highest_score_message_rect = highest_score_message.get_rect(center = (400,200))

        last_highest_score_message = font3.render(f'Your previous highest score is {score - difference}' ,False, ('White'))
        last_highest_score_message_rect = last_highest_score_message.get_rect(center = (465,200))

        score_break_highest_message = font3.render(f'Your highest score is {score}' ,False, ('White'))
        score_break_highest_message_rect = score_break_highest_message.get_rect(center = (465,270))
        
        # intro screen
        if score == 0:
            screen.blit(Mario_stand_scale,Maria_stand_rect)
            screen.blit(mus_message,mus_message_rect)
            screen.blit(star_message,star_message_rect)
            screen.blit(tur_message,tur_message_rect)
            screen.blit(game_name,game_name_rect)
            screen.blit(start_message,start_message_rect)
            screen.blit(tip_message,tip_message_rect)
        
        # lose screen
        elif difference == 0 and score != 0: 
            screen.blit(Mario_score_surf, (-50,80))
            Mario_score_animation()
            screen.blit(almost_message,almost_message_rect)
            screen.blit(score_message,score_message_rect)
            screen.blit(highest_score_message,highest_score_message_rect)
            screen.blit(try_message,try_message_rect)
            screen.blit(start_message2,(120,340))
            
        # win screen
        elif difference > 0 : 
            screen.blit(Mario_score_surf, (-50, 95))
            Mario_score_animation()
            screen.blit(congr_message,congr_message_rect)
            screen.blit(score_break_highest_message, score_break_highest_message_rect)
            screen.blit(last_highest_score_message,last_highest_score_message_rect)
            screen.blit(start_message2,(170,340))

    pygame.display.update()
    clock.tick(60)