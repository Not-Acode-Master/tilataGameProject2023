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
clicked = False
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

SAMURAI_SIZE = 200
SAMURAI_SCALE = 3
SAMURAI_OFFSET = [85, 62]
SAMURAI_DATA = [SAMURAI_SIZE, SAMURAI_SCALE, SAMURAI_OFFSET]

MAN_SIZE = 150
MAN_SCALE = 4
MAN_OFFSET = [65, 50]
MAN_DATA = [MAN_SIZE, MAN_SCALE, MAN_OFFSET]

#Define menu variables


#load music and sounds
pygame.mixer.music.load("assets/audio/music.mp3")
pygame.mixer.music.set_volume(0.5)
sword_fx = pygame.mixer.Sound("assets/audio/sword.wav")
sword_fx.set_volume(0.5)
magic_fx = pygame.mixer.Sound("assets/audio/magic.wav")
magic_fx.set_volume(0.5)
button_fx = pygame.mixer.Sound("assets/audio/button.mp3")
button_fx.set_volume(0.5)



#load background image
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()
settingsMainBg_image = pygame.image.load("assets/images/background/settingsMainBg.png").convert_alpha()
paused_menu_img = pygame.image.load("assets/images/background/pauseMenuBg.png").convert_alpha()
main_menu_img = pygame.image.load("assets/images/background/mainBg.png").convert_alpha()

#load logo
main_logo_img = pygame.image.load("assets/images/icons/logo.png").convert_alpha()
keys_spritesheet_img = pygame.image.load("assets/images/icons/keys.png").convert_alpha()
#load spriitheets
warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()
samurai_sheet = pygame.image.load("assets/images/samurai/Sprites/spritesheet.png").convert_alpha()
man_sheet = pygame.image.load("assets/images/mainChar/Sprites/spritesheet.png").convert_alpha()

#load victory image
victory_img = pygame.image.load("assets/images/icons/victory.png").convert_alpha()
pause_text_img = pygame.image.load("assets/images/icons/pauseText.png").convert_alpha()

#load buttons with its instances
play_button_img = pygame.image.load("assets/images/buttons/play.png").convert_alpha()
quit_button_img = pygame.image.load("assets/images/buttons/quit.png").convert_alpha()
settings_button_img = pygame.image.load("assets/images/buttons/settingsMain.png").convert_alpha()
back_button_img = pygame.image.load("assets/images/buttons/back.png").convert_alpha()
github_button_img = pygame.image.load("assets/images/buttons/github.png").convert_alpha()
controls_button_img = pygame.image.load("assets/images/buttons/controls.png").convert_alpha()
char1_button_img = pygame.image.load("assets/images/buttons/enemy1.png").convert_alpha()
char2_button_img = pygame.image.load("assets/images/buttons/enemy2.png").convert_alpha()


#define number of steps in each animation
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]
SAMURAI_ANIMATION_STEPS = [8, 8, 2, 6, 6, 4, 6]
MAN_ANIMATION_STEPS = [8, 8, 2, 4, 4, 4, 6]

#define font
count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)
setttings_font = pygame.font.Font("assets/fonts/turok.ttf", 60)

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
fighter_1 = Fighter(1, 200, 310, False, MAN_DATA, man_sheet, MAN_ANIMATION_STEPS, sword_fx)

fighter_2 = Fighter(2, 700, 310, True, SAMURAI_DATA, samurai_sheet, SAMURAI_ANIMATION_STEPS, sword_fx)
PLAYERS_COLLECTION = [[MAN_DATA, man_sheet, MAN_ANIMATION_STEPS], 
                      [SAMURAI_DATA, samurai_sheet, SAMURAI_ANIMATION_STEPS], 
                      [SAMURAI_DATA, samurai_sheet, SAMURAI_ANIMATION_STEPS]]

fighter_3 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

players_list = [fighter_1, fighter_2, fighter_3]

#create button instances for pause menu
play_button = Button(SCREEN_WIDHT/2 - play_button_img.get_width()/2*0.6, 170, play_button_img, 0.6)
quit_button = Button(SCREEN_WIDHT/2 - play_button_img.get_width()/2*0.6, 270, quit_button_img, 0.6)

#create button instances for main menu
back_button = Button(SCREEN_WIDHT/2 - back_button_img.get_width()/2*0.6, 460, back_button_img, 0.6)
back_button_controls = Button(SCREEN_WIDHT/2 - back_button_img.get_width()/2*0.6, 460, back_button_img, 0.6)

main_play_button = Button(SCREEN_WIDHT/2 - play_button_img.get_width()/2*0.6, 260, play_button_img, 0.6)
quit_main_button = Button(SCREEN_WIDHT/2 - quit_button_img.get_width()/2*0.6, 460, quit_button_img, 0.6)
settings_main_button = Button(SCREEN_WIDHT/2 - settings_button_img.get_width()/2*0.6, 360, settings_button_img, 0.6)
github_button = Button(SCREEN_WIDHT/2 - github_button_img.get_width()/2*0.6, 260, github_button_img, 0.6)
controls_button = Button(SCREEN_WIDHT/2 - controls_button_img.get_width()/2*0.6, 360, controls_button_img, 0.6)
char1_button = Button(SCREEN_WIDHT/3 - char1_button_img.get_width()*6, 260, char1_button_img, 6)
char2_button = Button(SCREEN_WIDHT/2 - char2_button_img.get_width()/2, 260, char2_button_img, 6)

#menu instanes
pause_Menu = pauseMenu(False, RED, screen, play_button, quit_button, paused_menu_img, SCREEN_WIDHT, SCREEN_HEIGHT, pause_text_img)

#Main menu instances
main_menu = mainMenu(False, "Main", screen, RED, main_logo_img, main_play_button, quit_main_button, settings_main_button, 
                     back_button, github_button, controls_button, back_button_controls, char1_button, char2_button, main_menu_img, settingsMainBg_image, keys_spritesheet_img, button_fx,
                     SCREEN_HEIGHT, SCREEN_WIDHT, 0.5)

#game loop
run = True
while run:
    
    clock.tick(FPS)
    
    main_menu.update(run, clicked, setttings_font)
    run = main_menu.runBool
    clicked = main_menu.clicked
    
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
            draw_health_bar(players_list[1].health, 580, 20)
            draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
            draw_text("P2: " + str(score[1]), score_font, RED, 580, 60)
            
            #update countdown 
            if intro_count <= 0:
                    fighter_1.move(SCREEN_WIDHT, SCREEN_HEIGHT, screen, players_list[main_menu.charIndex], round_over, sword_fx)
                    players_list[main_menu.charIndex].move(SCREEN_WIDHT, SCREEN_HEIGHT, screen, fighter_1, round_over, magic_fx)
                    
            else:
                #display count timera
                draw_text(str(intro_count), count_font, RED, SCREEN_WIDHT / 2, SCREEN_HEIGHT / 3)
                #update count timer
                if (pygame.time.get_ticks() - last_count_update ) >= 1000:
                    intro_count -= 1
                    last_count_update = pygame.time.get_ticks()
                
            #update fighters
            fighter_1.update()
            players_list[main_menu.charIndex].update()
            
            
            #draw fighters
            fighter_1.draw(screen)
            players_list[main_menu.charIndex].draw(screen)
            
            #check for player defeat
            if round_over == False:
                if fighter_1.alive == False:
                    score[1] += 1
                    round_over = True
                    round_over_time = pygame.time.get_ticks()
                elif players_list[main_menu.charIndex].alive == False:
                    score[0] += 1
                    round_over = True
                    round_over_time = pygame.time.get_ticks()
                ##if score[0] >= 1 or score[1] >= 1:
                    ##main_menu.menu_state = "EnemySelection"
                    ##main_menu.playing = False
                    #score[0] = 0
                    #score[1] = 0
                    #players_list[main_menu.charIndex] = Fighter(2, 700, 310, True, PLAYERS_COLLECTION[main_menu.charIndex][0], 
                                                                #PLAYERS_COLLECTION[main_menu.charIndex][1], 
                                                               # PLAYERS_COLLECTION[main_menu.charIndex][2], magic_fx)
            else:
                #display victory image
                screen.blit(victory_img, (360, 150))
                if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
                    round_over = False
                    intro_count = 4
                    fighter_1 = Fighter(1, 200, 310, False, MAN_DATA, man_sheet, MAN_ANIMATION_STEPS, sword_fx)
                    players_list[main_menu.charIndex] = Fighter(2, 700, 310, True, PLAYERS_COLLECTION[main_menu.charIndex][0], 
                                                                PLAYERS_COLLECTION[main_menu.charIndex][1], 
                                                                PLAYERS_COLLECTION[main_menu.charIndex][2], magic_fx)
                    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_p:
                pause_Menu.paused = not pause_Menu.paused
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
    
    
    #update display
    pygame.display.update()


#exit pygame
pygame.quit()