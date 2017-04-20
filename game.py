import pygame

# in order to use pygame, we have to run init method

# 2. Init pygame
pygame.init()

# 3. Create a screen with a size
screen = {
	"height": 512,
	"width": 480
}

screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)

# Whatever you put in here shows up at the top of the window when the game is opened
pygame.display.set_caption("Goblin Chase")

game_on = True
# 4. Create the game loop (while 1)
while game_on:
	# we are inside the main game loop it will run as long as game_on is true
	for event in pygame.event.get():
		# Looping through all events that happened this game loop cycle
		if event.type == pygame.QUIT:
			# the user clicked on the red X to leave the game
			game_on = False
			# update our boolean so pygame can escape loop

# 5. Add a quit event (requires sys)
# 6. Screen.fill (pass bg_color)
# 7. Flip the screen and start ove4
