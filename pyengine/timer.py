import pygame.time


t =  pygame.time.Clock()
TICK_DIFF = 0

def tick():
	TICK_DIFF = t.tick(60)
