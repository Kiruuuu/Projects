import pygame as pg
from pygame.locals import *

# Global variables for easy changes
screen_width = 600
screen_height = 600
timer = None
window = None
fps = 30
bg = pg.Color(255, 255, 255)

# PyGame initialization
pg.init()
timer = pg.time.Clock()
window = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Testing out PyGame!")

# Game Loop
finish = False
while finish == False:
	window.fill(bg)
	for event in pg.event.get():
		if event.type == QUIT:
			finish = True
			# Closes program if X button clicked in top right
	pg.display.update()
	timer.tick(fps)



