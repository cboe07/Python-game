import pygame

# bring in the math module to use absolute value
from math import fabs

# Get the randon module
from random import randint

# in order to use pygame, we have to run init method
# 2. Init pygame
pygame.init()


# 3. Create a screen with a size
screen = {
    "height": 512,
    "width": 480
}

keys = {
    "right": 275,
    "left": 276,
    "up": 273,
    "down": 274
}

keys_down = {
    "right": False,
    "left": False,
    "up": False,
    "down": False
}

hero = {
    "x": 100,
    "y": 100,
    "speed": 20,
    "kills": 0,
    "lives": 5
}

goblin = {
    "x": randint(0,screen['height'] - 32),
    "y": randint(0,screen['width'] - 32),
    "speed": 2,
    "direction": "N"
}

monster = {
    "x": randint(0,screen['height'] - 32),
    "y": randint(0,screen['width'] - 32),
    "speed": 1,
}

directions = ['N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW']

screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)

# Whatever you put in here shows up at the top of the window when the game is opened
pygame.display.set_caption("Space Goblin Chase")
background_image = pygame.image.load('images/space_background.png')
hero_image = pygame.image.load('images/spaceship.png')
hero_image_scaled = pygame.transform.scale(hero_image, (32,32))
goblin_image = pygame.image.load('images/goblin.png')
monster_image = pygame.image.load('images/monster.png')


# Add music files
pygame.mixer.music.load('./sounds/music.wav')
pygame.mixer.music.play(-1)

win_sound = pygame.mixer.Sound('./sounds/win.wav')
lose_sound = pygame.mixer.Sound('./sounds/lose.wav')

tick = 0

# /////////////////////MAIN GAME LOOP/////////////////////////
# /////////////////////MAIN GAME LOOP/////////////////////////
# /////////////////////MAIN GAME LOOP/////////////////////////
game_on = True
# 4. Create the game loop (while 1)
while game_on:
    tick += 1
    # we are inside the main game loop it will run as long as game_on is true
    # -----EVENTS-----
    for event in pygame.event.get():
        # Looping through all events that happened this game loop cycle
        # 5. Add a quit event (requires sys)
        if event.type == pygame.QUIT:
            # the user clicked on the red X to leave the game
            game_on = False
            # update our boolean so pygame can escape loop
        elif event.type == pygame.KEYDOWN:
            if event.key == keys['up']:
                keys_down['up'] = True
            elif event.key == keys['down']:
                keys_down['down'] = True
            elif event.key == keys['left']:
                keys_down['left'] = True
            elif event.key == keys['right']:
                keys_down['right'] = True
        elif event.type == pygame.KEYUP:
            if event.key == keys['up']:
                # the user let go of a key... and that key was the up arrow
                keys_down['up'] = False
            if event.key == keys['down']:
                keys_down['down'] = False
            if event.key == keys['left']:
                keys_down['left'] = False
            if event.key == keys['right']:
                keys_down['right'] = False

    if hero['lives'] > 0:
        # Update hero postion
        if keys_down['up']:
            hero['y'] -= hero['speed']
        elif keys_down['down']:
            hero['y'] += hero['speed']
        if keys_down['left']:
            hero['x'] -= hero['speed']
        elif keys_down['right']:
            hero['x'] += hero['speed']

    # Goblin position
    # get random direction (up down left or right)
    # move goblin in that direction 
        if (goblin['direction'] == 'N'):
            goblin['y'] -= goblin['speed']
        elif (goblin['direction'] == 'S'):
            goblin['y'] += goblin['speed']
        elif (goblin['direction'] == 'E'):
            goblin['x'] += goblin['speed']
        elif (goblin['direction'] == 'W'):
            goblin['x'] += goblin['speed']
        elif (goblin['direction'] == 'NE'):
            goblin['x'] -= goblin['speed']
            goblin['y'] += goblin['speed']  
        elif (goblin['direction'] == 'NW'):
            goblin['x'] -= goblin['speed']
            goblin['y'] -= goblin['speed']  
        elif (goblin['direction'] == 'SE'):
            goblin['x'] += goblin['speed']
            goblin['y'] += goblin['speed']
        elif (goblin['direction'] == 'SW'):
            goblin['x'] += goblin['speed']
            goblin['y'] -= goblin['speed']  

        if (tick % 20 == 0):
            new_dir_index = randint(0, len(directions) - 1)
            goblin['direction'] = directions[new_dir_index]

        if (goblin['x'] > screen['width']):
            goblin['x'] = 0
        elif (goblin['x'] < 0):
            goblin['x'] = screen['width']
        if (goblin['y'] > screen['height']):
            goblin['y'] = 0
        elif (goblin['y'] < 0):
            goblin['y'] = screen['height']


    # Monster Chasing Hero
        if hero['lives'] > 0:
            if hero['x'] > monster['x']:
                monster['x'] += monster['speed']
            if hero['x'] < monster['x']:
                monster['x'] -= monster['speed']
            if hero['y'] > monster['y']:
                monster['y'] += monster['speed']
            if hero['y'] < monster['y']:
                monster['y'] -= monster['speed']

    # COLLISION DETECTION
    distance_between = fabs(hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])
    if (distance_between < 32):
        # the hero and goblin are touching!
        # print ("Collision!!")
        # Generate random X > 0, X < screen['width']
        # Generate random Y >0, Y < screen['hieght']
        rand_x = randint(0,screen['width'] -32)
        rand_y = randint(0,screen['height'] -32)
        goblin['x'] = rand_x
        goblin['y'] = rand_y
        # Update the hero's wins
        hero['kills'] += 1
        win_sound.play()

    distance_between_monster = fabs(hero['x'] - monster['x']) + fabs(hero['y'] - monster['y'])
    if (distance_between_monster < 32):
        rand_x = randint(0,screen['width'] -32)
        rand_y = randint(0,screen['height'] -32)
        monster['x'] = rand_x
        monster['y'] = rand_y
        hero['lives'] -= 1

    pygame_screen.blit(background_image, [0,0])
    font = pygame.font.Font(None, 25)

    # GAME OVER MESSAGE
    if hero['lives'] <= 0:
        screen_text = font.render("GAME OVER! YOU LOOSE!", True, (255,0,0))
        pygame_screen.blit(screen_text,[150, 200])
        
    # -----RENDER-----
    # blit takes 2 arguments
    # 1. What?
    # 2. Where?
    # Screen.fill (pass bg_color)


    # Draw the hero wins on the screen
    wins_text = font.render("Kills: %d" % (hero['kills']), True, (255,255,255))
    lives_text = font.render("Lives: %d" % (hero['lives']), True, (255,255,255))
    pygame_screen.blit(wins_text, [40,40])
    pygame_screen.blit(lives_text, [120, 40])

    #draw the hero
    pygame_screen.blit(hero_image_scaled, [hero['x'],hero['y']])

    pygame_screen.blit(goblin_image, [goblin['x'],goblin['y']])

    pygame_screen.blit(monster_image, [monster['x'],monster['y']])

    # clear the screen for the next time
    pygame.display.flip()

# 7. Flip the screen and start ove4
