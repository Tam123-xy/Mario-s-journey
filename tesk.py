import pygame
from sys import exit

def player_animation():
     global Mario_surf, Mario_run_index
     Mario_run_index += 0.1
     if Mario_run_index >= len(Mario_run) : Mario_run_index = 0
     Mario_surf = Mario_run[int(Mario_run_index)]

#Game foundation
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 400))  
pygame.display.set_caption("Mario's journey") 
font = pygame.font.Font('font/font.ttf', 50)
font2 = pygame.font.Font('font/font.ttf', 40)
pygame.key.get_focused()

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

#game surface
sky_surf = pygame.image.load('grahics/sky.jpg').convert()
ground_surf = pygame.image.load('grahics/ground.png').convert()

star = pygame.image.load('grahics/blockers/star.png').convert()
star_s = pygame.transform.scale(star, (70, 70))

mus = pygame.image.load('grahics/blockers/mus.png').convert()
mus_s = pygame.transform.scale(mus, (70, 70))

tur = pygame.image.load('grahics/blockers/tur.png').convert()
tur_s = pygame.transform.scale(tur, (70, 70))

blocker_image = [mus_s, tur_s, star_s, mus_s, star_s, tur_s]


#Mario run gif
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

#Timer
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT,1000)
counter = 10
text = '10'.rjust(3)

#Index
game_active= False
start_time = 0
correct_key_5times = 0
loop_th_index = 0
#score = 0


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 

        if game_active:
            if event.type == pygame.USEREVENT:
                        counter -=1
                        text = str (counter).rjust(3)

            if correct_key_5times == 5:
                correct_key_5times = 0
                counter +=5
                text = str (counter).rjust(3)
                print('Time up! +5s')
                
            for loop_th in range (5,599,6):
                if event.type == pygame.KEYDOWN:
                    if loop_th_index == loop_th and event.key == pygame.K_RIGHT:    
                            loop_th_index +=1
                            correct_key_5times +=1
                            print(correct_key_5times)
                            #score +=1
                    elif loop_th_index == loop_th and event.key != pygame.K_RIGHT:
                         correct_key_5times =0
                         break

            for loop_th in range (4,598,6):
                if event.type == pygame.KEYDOWN:
                    if loop_th_index == loop_th and  event.key == pygame.K_UP: 
                            loop_th_index +=1
                            correct_key_5times +=1
                            print(correct_key_5times)
                            #score +=1
                    elif loop_th_index == loop_th and event.key != pygame.K_UP:
                         correct_key_5times =0
                         break

            for loop_th in range (3,597,6):
                if event.type == pygame.KEYDOWN:
                    if loop_th_index == loop_th and event.key == pygame.K_DOWN:
                        loop_th_index +=1
                        correct_key_5times +=1
                        print(correct_key_5times)
                        #score +=1
                    elif loop_th_index == loop_th and event.key != pygame.K_DOWN:
                         correct_key_5times =0
                         break

            for loop_th in range (2,596,6):
                if event.type == pygame.KEYDOWN:
                    if loop_th_index == loop_th and  event.key == pygame.K_UP: 
                            loop_th_index +=1
                            correct_key_5times +=1
                            print(correct_key_5times)
                            #score +=1
                    elif loop_th_index == loop_th and event.key != pygame.K_UP:
                         correct_key_5times =0
                         break

            for loop_th in range (1,595,6):
                if event.type == pygame.KEYDOWN:
                    if loop_th_index == loop_th and event.key == pygame.K_RIGHT:    
                            loop_th_index +=1
                            correct_key_5times +=1
                            print(correct_key_5times)
                            #score +=1
                    elif loop_th_index == loop_th and event.key != pygame.K_RIGHT:
                         correct_key_5times =0
                         break

            for loop_th in range (0,594,6):
                if event.type == pygame.KEYDOWN:
                    if loop_th_index == loop_th and event.key == pygame.K_DOWN:
                        loop_th_index +=1 
                        correct_key_5times +=1
                        print(correct_key_5times)
                        #score +=1
                    elif loop_th_index == loop_th and event.key != pygame.K_DOWN:
                         correct_key_5times =0

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                game_active = True
                counter = 11
                correct_key_5times = 0
                       

                    
    if game_active:          
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        screen.blit(font.render(f'Time: {text}',True,('White')),(32,48))
        player_animation()
        screen.blit(Mario_surf, (20, 150))
        
        

        for loop_th in range (0,594,6):
            if loop_th_index == loop_th:
                screen.blit(blocker_image[0], (200, 230))
                screen.blit(blocker_image[1], (300, 230))
                screen.blit(blocker_image[2], (400, 230))
                screen.blit(blocker_image[3], (500, 230))
                screen.blit(blocker_image[4], (600, 230))
                screen.blit(blocker_image[5], (700, 230))
                break

        for loop_th in range (1,595,6):
            if loop_th_index == loop_th:
                screen.blit(blocker_image[1], (200, 230))
                screen.blit(blocker_image[2], (300, 230))
                screen.blit(blocker_image[3], (400, 230))
                screen.blit(blocker_image[4], (500, 230))
                screen.blit(blocker_image[5], (600, 230))
                screen.blit(blocker_image[0], (700, 230))
                break

        for loop_th in range (2,596,6):
            if loop_th_index == loop_th:
                screen.blit(blocker_image[2], (200, 230))
                screen.blit(blocker_image[3], (300, 230))
                screen.blit(blocker_image[4], (400, 230))
                screen.blit(blocker_image[5], (500, 230))
                screen.blit(blocker_image[0], (600, 230))
                screen.blit(blocker_image[1], (700, 230))
                break

        for loop_th in range (3,597,6):
            if loop_th_index == loop_th:
                screen.blit(blocker_image[3], (200, 230))
                screen.blit(blocker_image[4], (300, 230))
                screen.blit(blocker_image[5], (400, 230))
                screen.blit(blocker_image[0], (500, 230))
                screen.blit(blocker_image[1], (600, 230))
                screen.blit(blocker_image[2], (700, 230))
                break
                
        for loop_th in range (4,598,6):
            if loop_th_index == loop_th:
                screen.blit(blocker_image[4], (200, 230))
                screen.blit(blocker_image[5], (300, 230))
                screen.blit(blocker_image[0], (400, 230))
                screen.blit(blocker_image[1], (500, 230))
                screen.blit(blocker_image[2], (600, 230))
                screen.blit(blocker_image[3], (700, 230))
                break

        for loop_th in range (5,599,6):
            if loop_th_index == loop_th:
                screen.blit(blocker_image[5], (200, 230))
                screen.blit(blocker_image[0], (300, 230))
                screen.blit(blocker_image[1], (400, 230))
                screen.blit(blocker_image[2], (500, 230))
                screen.blit(blocker_image[3], (600, 230))
                screen.blit(blocker_image[4], (700, 230))
                

        if counter == 0:
            game_active = False

    else:
        screen.fill((94,129,162))
        screen.blit(Mario_stand_scale,Maria_stand_rect)
        screen.blit(game_name,game_name_rect)
        screen.blit(game_message,game_message_rect)
        screen.blit(game_message2,game_message2_rect)  #过后要删的
        screen.blit(game_message3,game_message3_rect)  #过后要删的
        screen.blit(game_message4,game_message4_rect)  #过后要删的
        # if score == 0:
        #     screen.blit(game_message,game_message_rect)
        #     screen.blit(game_message2,game_message2_rect)
        #     screen.blit(game_message3,game_message3_rect)
        #     screen.blit(game_message4,game_message4_rect)
        
        # else:
        #     #output分数
        
    
    pygame.display.update()
    clock.tick(60)