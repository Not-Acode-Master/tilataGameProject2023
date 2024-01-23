import pygame
from pygame import mixer
from fighter import Fighter
from pausemenu import pauseMenu
from button import Button
from mainmenu import mainMenu

mixer.init()
pygame.init()

#Create game window
SCREEN_WIDHT = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

#set framerated
clock = pygame.time.Clock()
FPS = 60

#Define colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]#player scores pi and p2
round_over = False
ROUND_OVER_COOLDOWN = 2000

#Define fighter variables
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

#Define menu variables


#load music and sounds
pygame.mixer.music.load("assets/audio/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
pygame.mixer.music.pause()
sword_fx = pygame.mixer.Sound("assets/audio/sword.wav")
sword_fx.set_volume(0.5)
magic_fx = pygame.mixer.Sound("assets/audio/magic.wav")
magic_fx.set_volume(0.5)



#load background image
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()
paused_menu_img = pygame.image.load("assets/images/background/pauseMenuBg.png").convert_alpha()
main_menu_img = pygame.image.load("assets/images/background/mainBg.png").convert_alpha()

#load logo
main_logo_img = pygame.image.load("assets/images/icons/logo.png").convert_alpha()

#load spriitheets
warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()

#load victory image
victory_img = pygame.image.load("assets/images/icons/victory.png").convert_alpha()
pause_text_img = pygame.image.load("assets/images/icons/pauseText.png").convert_alpha()

#load buttons with its instances
play_button_img = pygame.image.load("assets/images/buttons/play.png").convert_alpha()
quit_button_img = pygame.image.load("assets/images/buttons/quit.png").convert_alpha()

start_button_img = pygame.image.load("assets/images/buttons/start.png").convert_alpha()
quitMain_button_img = pygame.image.load("assets/images/buttons/quitMain.png").convert_alpha()

#define number of steps in each animation
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

#define font
count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)

#function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDHT, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))
    
#function for drawing fighter health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x-5, y-5, 410, 40))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))
    
    
#create two instances of fighters
fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

#create button instances
play_button = Button(SCREEN_WIDHT/2 - 2 * play_button_img.get_width(), 170, play_button_img, 4)
quit_button = Button(SCREEN_WIDHT/2 - 2 * play_button_img.get_width(), 300, quit_button_img, 4)

start_button = Button(SCREEN_WIDHT/2 - 2 * start_button_img.get_width(), 270, start_button_img, 4)
quit_main_button = Button(SCREEN_WIDHT/2 - 2 * quitMain_button_img.get_width(), 400, quitMain_button_img, 4)

#menu instanes
pause_Menu = pauseMenu(False, RED, screen, play_button, quit_button, paused_menu_img, SCREEN_WIDHT, SCREEN_HEIGHT, pause_text_img)

#Main menu instances
main_menu = mainMenu(False, "Main", screen, RED, main_logo_img, start_button, quit_main_button, main_menu_img, SCREEN_HEIGHT, SCREEN_WIDHT, 0.5)

#game loop
run = True
while run:
    
    clock.tick(FPS)
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_p:
                pause_Menu.paused = not pause_Menu.paused
    
    main_menu.update(run)
    run = main_menu.runBool
    
    if main_menu.playing == True:
        #update menu state
        pause_Menu.update(run)
        run = pause_Menu.runt
        
        #check if the game is paused
        if pause_Menu.paused == False:
            
            #draw background
            draw_bg()
            
            #show player stats
            draw_health_bar(fighter_1.health, 20, 20)
            draw_health_bar(fighter_2.health, 580, 20)
            draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
            draw_text("P2: " + str(score[1]), score_font, RED, 580, 60)
            
            pygame.mixer.music.unpause()
            
            #update countdown 
            if intro_count <= 0:
                    fighter_1.move(SCREEN_WIDHT, SCREEN_HEIGHT, screen, fighter_2, round_over, sword_fx)
                    fighter_2.move(SCREEN_WIDHT, SCREEN_HEIGHT, screen, fighter_1, round_over, magic_fx)
                    
            else:
                #display count timera
                draw_text(str(intro_count), count_font, RED, SCREEN_WIDHT / 2, SCREEN_HEIGHT / 3)
                #update count timer
                if (pygame.time.get_ticks() - last_count_update ) >= 1000:
                    intro_count -= 1
                    last_count_update = pygame.time.get_ticks()
                
            #update fighters
            fighter_1.update()
            fighter_2.update()
            
            
            #draw fighters
            fighter_1.draw(screen)
            fighter_2.draw(screen)
            
            #check for player defeat
            if round_over == False:
                if fighter_1.alive == False:
                    score[1] += 1
                    round_over = True
                    round_over_time = pygame.time.get_ticks()
                elif fighter_2.alive == False:
                    score[0] += 1
                    round_over = True
                    round_over_time = pygame.time.get_ticks()
            else:
                #display victory image
                screen.blit(victory_img, (360, 150))
                if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
                    round_over = False
                    intro_count = 4
                    fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
                    fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)
        else:
            pygame.mixer.music.pause()
    
    else:
        pygame.mixer.music.pause()
    
    
    #update display
    pygame.display.update()


#exit pygame
pygame.quit()