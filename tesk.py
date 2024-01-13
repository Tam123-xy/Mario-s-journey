import pygame
from sys import exit

# Mario Animation 
def Mario_animation():
     global Mario_surf, Mario_run_index
     Mario_run_index += 0.1
     if Mario_run_index >= len(Mario_run) : Mario_run_index = 0
     Mario_surf = Mario_run[int(Mario_run_index)]

# Check player's input 
def blocker_key(type_key):
    global i , correct_key
    if event.type == pygame.KEYDOWN:
        if event.key == type_key:
            i +=1
            correct_key +=1
            print (correct_key)
        else:
            correct_key = 0

# Print the 6 blockes in one screen
def show_blockers(blocker):
    show_blocker = 0
    coordinate = 200

    while show_blocker <= 6:
            screen.blit(blocker_image[blocker], (coordinate, 230))
            blocker +=1
            show_blocker +=1
            coordinate += 100

            if blocker == 18:
                 blocker = 0
            

# Game foundation
pygame.init()
pygame.mixer.init()
pygame.key.get_focused()
screen = pygame.display.set_mode((800, 400))  
pygame.display.set_caption("Mario's journey") 
font = pygame.font.Font('font/font.ttf', 50)
font2 = pygame.font.Font('font/font.ttf', 40)

# Intro screen surface
Mario_stand = pygame.image.load('grahics/Mario_stand.png').convert()
Mario_stand_scale = pygame.transform.rotozoom(Mario_stand,0,0.8)
Maria_stand_rect = Mario_stand_scale.get_rect(center = (400,165))

game_name = font.render("Mario's journey",False, ('White'))
game_name_rect = game_name.get_rect(center=(400,50))

game_message = font2.render('Send the star to the sky by pressing arrow key UP!',False, ('White'))
game_message_rect = game_message.get_rect(center = (400,280))

game_message2 = font2.render('Smack the mushroom to the ground by pressing arrow key DOWN!',False, ('White'))
game_message2_rect = game_message2.get_rect(center = (400,310))

game_message3 = font2.render('Kick off the turtle by pressing arrow key RIGHT!',False, ('White'))
game_message3_rect = game_message3.get_rect(center = (400,340))

game_message4 = font.render('Press SPACE to start the game!',False, ('Black'))
game_message4_rect = game_message3.get_rect(center = (450,370))

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
time = 20
text = '20'.rjust(3)

# Index initialize
game_active= False
correct_key = 0
score = 0

i=0
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
            
            # Successfully passed through 5 blockers continually
            if correct_key == 5:
                correct_key = 0
                time +=5
                text = str (time).rjust(3)
                print('Extra time! +5s')

            # Check player's input 
            if i == 17: blocker_key(pygame.K_RIGHT)

            elif i == 16: blocker_key(pygame.K_DOWN)

            elif i == 15: blocker_key(pygame.K_UP)

            elif i == 14: blocker_key(pygame.K_RIGHT)

            elif i == 13: blocker_key(pygame.K_UP)

            elif i == 12: blocker_key(pygame.K_DOWN)

            elif i == 11: blocker_key(pygame.K_RIGHT)

            elif i == 10: blocker_key(pygame.K_RIGHT)

            elif i == 9: blocker_key(pygame.K_UP)

            elif i == 8: blocker_key(pygame.K_UP)

            elif i == 7: blocker_key(pygame.K_DOWN)

            elif i == 6: blocker_key(pygame.K_RIGHT)

            elif i == 5: blocker_key(pygame.K_DOWN)

            elif i == 4: blocker_key(pygame.K_UP)

            elif i == 3: blocker_key(pygame.K_RIGHT)

            elif i == 2: blocker_key(pygame.K_UP)

            elif i == 1: blocker_key(pygame.K_DOWN)

            else: blocker_key(pygame.K_DOWN)
            
            # Initialize i when player is fully go throught the blocker_key list
            if i == 18:
                i = 0
            
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                game_active = True
                time = 21
                correct_key = 0
                i = 0
                print("Let's go")

    if game_active:          
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        screen.blit(font.render(f'Time: {text}',True,('White')),(32,48))
        Mario_animation()
        screen.blit(Mario_surf, (20, 150))

        # Print the 6 blockes in one screen
        if i == 17: show_blockers(17)

        elif i == 16: show_blockers(16)
    
        elif i == 15: show_blockers(15)
            
        elif i == 14: show_blockers(14)
        
        elif i == 13: show_blockers(13)
            
        elif i == 12: show_blockers(12)
            
        elif i == 11: show_blockers(11)
           
        elif i == 10: show_blockers(10)
            
        elif i == 9: show_blockers(9)
           
        elif i == 8: show_blockers(8)
            
        elif i == 7: show_blockers(7)
            
        elif i == 6: show_blockers(6)
           
        elif i == 5: show_blockers(5)
            
        elif i == 4: show_blockers(4)
            
        elif i == 3: show_blockers(3)
            
        elif i == 2: show_blockers(2)
            
        elif i == 1: show_blockers(1)
            
        else: show_blockers(0)
            
        if time == 0:
            game_active = False

    else:
        screen.fill((94,129,162))
        screen.blit(Mario_stand_scale,Maria_stand_rect)
        screen.blit(game_name,game_name_rect)
        screen.blit(game_message,game_message_rect)
        screen.blit(game_message2,game_message2_rect)  
        screen.blit(game_message3,game_message3_rect)  
        screen.blit(game_message4,game_message4_rect)  
        #####
        # screen.fill((94,129,162))
        # screen.blit(Mario_stand_scale,Maria_stand_rect)
        # screen.blit(game_name,game_name_rect)

        # if score == 0:
        #     screen.blit(game_message,game_message_rect)
        #     screen.blit(game_message2,game_message2_rect)
        #     screen.blit(game_message3,game_message3_rect)
        #     screen.blit(game_message4,game_message4_rect)

        #elif score <= highest score:
        #elif scre > highest score:
        
    
    pygame.display.update()
    clock.tick(60) 