import pygame
from sys import exit

# Animation Mario
def Mario_animation():
     global Mario_surf, Mario_run_index
     Mario_run_index += 0.1
     if Mario_run_index >= len(Mario_run) : Mario_run_index = 0
     Mario_surf = Mario_run[int(Mario_run_index)]

def mus_blocker():
    global i , correct_key
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            i +=1
            correct_key +=1
            print (correct_key)
        else:
            correct_key = 0

def tur_blocker():
    global i , correct_key
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            i +=1
            correct_key +=1
            print (correct_key)
        else:
            correct_key = 0

def star_blocker():
    global i , correct_key
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP: 
            i +=1
            correct_key +=1
            print (correct_key)
        else:
            correct_key = 0

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

blocker_image = [mus_s, tur_s, star_s, 
                 tur_s, star_s, mus_s,
                 tur_s, mus_s, star_s,
                 mus_s, star_s, tur_s,
                 star_s,tur_s, mus_s,
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
time = 10
text = '10'.rjust(3)

# Index, initialize
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
            if i == 17: tur_blocker()

            elif i == 16: mus_blocker()

            elif i == 15: star_blocker()

            elif i == 14: mus_blocker()

            elif i == 13: tur_blocker()

            elif i == 12: star_blocker()

            elif i == 11: tur_blocker()

            elif i == 10: star_blocker()

            elif i == 9: mus_blocker()

            elif i == 8: star_blocker()

            elif i == 7: mus_blocker()

            elif i == 6: tur_blocker()

            elif i == 5: mus_blocker()

            elif i == 4: star_blocker()

            elif i == 3: tur_blocker()

            elif i == 2: star_blocker()

            elif i == 1: tur_blocker()

            else: mus_blocker()
            
            # Initialize i when player is fully go throught the blocker list
            if i == 18:
                i = 0
            
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                game_active = True
                time = 11
                correct_key = 0

    if game_active:          
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        screen.blit(font.render(f'Time: {text}',True,('White')),(32,48))
        Mario_animation()
        screen.blit(Mario_surf, (20, 150))
        
        if i == 17:
            screen.blit(blocker_image[17], (200, 230))
            screen.blit(blocker_image[0], (300, 230))
            screen.blit(blocker_image[1], (400, 230))
            screen.blit(blocker_image[2], (500, 230))
            screen.blit(blocker_image[3], (600, 230))
            screen.blit(blocker_image[4], (700, 230))

        elif i == 16:
            screen.blit(blocker_image[16], (200, 230))
            screen.blit(blocker_image[17], (300, 230))
            screen.blit(blocker_image[0], (400, 230))
            screen.blit(blocker_image[1], (500, 230))
            screen.blit(blocker_image[2], (600, 230))
            screen.blit(blocker_image[3], (700, 230))

        elif i == 15:
            screen.blit(blocker_image[15], (200, 230))
            screen.blit(blocker_image[16], (300, 230))
            screen.blit(blocker_image[17], (400, 230))
            screen.blit(blocker_image[0], (500, 230))
            screen.blit(blocker_image[1], (600, 230))
            screen.blit(blocker_image[2], (700, 230))

        elif i == 14:
            screen.blit(blocker_image[14], (200, 230))
            screen.blit(blocker_image[15], (300, 230))
            screen.blit(blocker_image[16], (400, 230))
            screen.blit(blocker_image[17], (500, 230))
            screen.blit(blocker_image[0], (600, 230))
            screen.blit(blocker_image[1], (700, 230))

        elif i == 13:
            screen.blit(blocker_image[13], (200, 230))
            screen.blit(blocker_image[14], (300, 230))
            screen.blit(blocker_image[15], (400, 230))
            screen.blit(blocker_image[16], (500, 230))
            screen.blit(blocker_image[17], (600, 230))
            screen.blit(blocker_image[0], (700, 230))

        elif i == 12:
            screen.blit(blocker_image[12], (200, 230))
            screen.blit(blocker_image[13], (300, 230))
            screen.blit(blocker_image[14], (400, 230))
            screen.blit(blocker_image[15], (500, 230))
            screen.blit(blocker_image[16], (600, 230))
            screen.blit(blocker_image[17], (700, 230))

        elif i == 11:
            screen.blit(blocker_image[11], (200, 230))
            screen.blit(blocker_image[12], (300, 230))
            screen.blit(blocker_image[13], (400, 230))
            screen.blit(blocker_image[14], (500, 230))
            screen.blit(blocker_image[15], (600, 230))
            screen.blit(blocker_image[16], (700, 230))

        elif i == 10:
            screen.blit(blocker_image[10], (200, 230))
            screen.blit(blocker_image[11], (300, 230))
            screen.blit(blocker_image[12], (400, 230))
            screen.blit(blocker_image[13], (500, 230))
            screen.blit(blocker_image[14], (600, 230))
            screen.blit(blocker_image[15], (700, 230))

        elif i == 9:
            screen.blit(blocker_image[9], (200, 230))
            screen.blit(blocker_image[10], (300, 230))
            screen.blit(blocker_image[11], (400, 230))
            screen.blit(blocker_image[12], (500, 230))
            screen.blit(blocker_image[13], (600, 230))
            screen.blit(blocker_image[14], (700, 230))

        elif i == 8:
            screen.blit(blocker_image[8], (200, 230))
            screen.blit(blocker_image[9], (300, 230))
            screen.blit(blocker_image[10], (400, 230))
            screen.blit(blocker_image[11], (500, 230))
            screen.blit(blocker_image[12], (600, 230))
            screen.blit(blocker_image[13], (700, 230))

        elif i == 7:
            screen.blit(blocker_image[7], (200, 230))
            screen.blit(blocker_image[8], (300, 230))
            screen.blit(blocker_image[9], (400, 230))
            screen.blit(blocker_image[10], (500, 230))
            screen.blit(blocker_image[11], (600, 230))
            screen.blit(blocker_image[12], (700, 230))

        elif i == 6:
            screen.blit(blocker_image[6], (200, 230))
            screen.blit(blocker_image[7],(300, 230))
            screen.blit(blocker_image[8], (400, 230))
            screen.blit(blocker_image[9], (500, 230))
            screen.blit(blocker_image[10], (600, 230))
            screen.blit(blocker_image[11], (700, 230))

        elif i == 5:
            screen.blit(blocker_image[5], (200, 230))
            screen.blit(blocker_image[6], (300, 230))
            screen.blit(blocker_image[7], (400, 230))
            screen.blit(blocker_image[8], (500, 230))
            screen.blit(blocker_image[9], (600, 230))
            screen.blit(blocker_image[10], (700, 230))

        elif i == 4:
            screen.blit(blocker_image[4], (200, 230))
            screen.blit(blocker_image[5], (300, 230))
            screen.blit(blocker_image[6], (400, 230))
            screen.blit(blocker_image[7], (500, 230))
            screen.blit(blocker_image[8], (600, 230))
            screen.blit(blocker_image[9], (700, 230))

        elif i == 3:
            screen.blit(blocker_image[3], (200, 230))
            screen.blit(blocker_image[4], (300, 230))
            screen.blit(blocker_image[5], (400, 230))
            screen.blit(blocker_image[6], (500, 230))
            screen.blit(blocker_image[7], (600, 230))
            screen.blit(blocker_image[8], (700, 230))

        elif i == 2:
            screen.blit(blocker_image[2], (200, 230))
            screen.blit(blocker_image[3], (300, 230))
            screen.blit(blocker_image[4], (400, 230))
            screen.blit(blocker_image[5], (500, 230))
            screen.blit(blocker_image[6], (600, 230))
            screen.blit(blocker_image[7], (700, 230))

        elif i == 1:
            screen.blit(blocker_image[1], (200, 230))
            screen.blit(blocker_image[2], (300, 230))
            screen.blit(blocker_image[3], (400, 230))
            screen.blit(blocker_image[4], (500, 230))
            screen.blit(blocker_image[5], (600, 230))
            screen.blit(blocker_image[6], (700, 230))

        else:
            screen.blit(blocker_image[0], (200, 230))
            screen.blit(blocker_image[1], (300, 230))
            screen.blit(blocker_image[2], (400, 230))
            screen.blit(blocker_image[3], (500, 230))
            screen.blit(blocker_image[4], (600, 230))
            screen.blit(blocker_image[5], (700, 230))

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