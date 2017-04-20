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
	"wins": 0
}


goblin = {
	"x": 200,
	"y": 200,
	"speed": 10
}

screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)

# Whatever you put in here shows up at the top of the window when the game is opened
pygame.display.set_caption("Goblin Chase")
background_image = pygame.image.load('images/background.png')
hero_image = pygame.image.load('images/hero.png')
hero_image_scaled = pygame.transform.scale(hero_image, (32,32))
goblin_image = pygame.image.load('images/goblin.png')



# /////////////////////MAIN GAME LOOP/////////////////////////
# /////////////////////MAIN GAME LOOP/////////////////////////
# /////////////////////MAIN GAME LOOP/////////////////////////
game_on = True
# 4. Create the game loop (while 1)
while game_on:
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

	# Update hero postion
	if keys_down['up']:
		hero['y'] -= hero['speed']
	elif keys_down['down']:
		hero['y'] += hero['speed']
	if keys_down['left']:
		hero['x'] -= hero['speed']
	elif keys_down['right']:
		hero['x'] += hero['speed']

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
		hero['wins'] += 1


	# -----RENDER-----
	# blit takes 2 arguments
	# 1. What?
	# 2. Where?
	# Screen.fill (pass bg_color)
	pygame_screen.blit(background_image, [0,0])

	# Draw the hero wins on the screen
	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins: %d" % (hero['wins']), True, (0,0,0))
	pygame_screen.blit(wins_text, [40,40])

	#draw the hero
	pygame_screen.blit(hero_image_scaled, [hero['x'],hero['y']])

	pygame_screen.blit(goblin_image, [goblin['x'],goblin['y']])

	# clear the screen for the next time
	pygame.display.flip()

# 7. Flip the screen and start ove4








