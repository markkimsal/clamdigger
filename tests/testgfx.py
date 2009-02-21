import sys,os
if hasattr(sys, 'frozen'):
	CLMD_fullpath = os.path.join(
			os.path.dirname(os.path.abspath(sys.executable)), '..')
else:
	CLMD_fullpath = os.path.join(
			os.path.dirname(os.path.abspath(__file__)), '..')

sys.path.append( os.path.join(CLMD_fullpath ))


import pygame
import pygame.locals
from pygame.locals import *
import lib
from lib import gfx, video, level, clmd_sprite
import pygame.time

import pyengine
from pyengine import object
from pyengine.object import Sprite


game = video.GameWorld((640,480), 'The object of the game is to find parking')


foo = clmd_sprite.Player()

print foo

level = level.GameLevel("test");
print level


game.setLevel(level)


keypress = pygame.event.poll()
key = keypress.type
idx = 0
keyStatus = KEYUP
velocityDelta = 0
angleDelta = 0


timer = pygame.time.Clock()

while (True):
	timer.tick(40)

	if (key == QUIT):
			break
	if (key == KEYDOWN):
		keyStatus = KEYDOWN
		if ( keypress.key == K_ESCAPE):
			break
		if (keypress.key == K_LEFT):
			angleDelta = 10
		if (keypress.key == K_RIGHT):
			angleDelta = -10
		if (keypress.key == K_f):
			pass


		if (keypress.key == K_UP):
			if (velocityDelta < 6):
				velocityDelta += 2

		if (keypress.key == K_DOWN):
			velocityDelta = -2

	if (key == KEYUP):
		keyStatus = KEYUP
		if (keypress.key == K_LEFT and angleDelta > 0):
			angleDelta = 0
		if (keypress.key == K_RIGHT and angleDelta < 0):
			angleDelta = 0
		if (keypress.key == K_UP):
			if (velocityDelta > 0):
				velocityDelta = -1

	"""if key == MOUSEMOTION:
		rel = pygame.mouse.get_rel()
		game.camera_x += (rel[0] )
		game.camera_y += (rel[1] )
	"""

	if (foo.velocity < 0 ):
	    velocityDelta = 0
	    foo.velocity = 0


	foo.addVelocity(velocityDelta)

	foo.angle += angleDelta

	#game.screen.fill( (60,60,60)  )
	game.paintWorld()

	game.paintSprite(foo)
	foo.update()
	#pygame.display.update(( 0,0, 320,320))
	pygame.display.flip()

	keypress = pygame.event.poll()
	#for e in keylist:
	#	keypress = e
	key = keypress.type
	pygame.time.wait(0) 
	pygame.event.pump()
	idx = idx+1
	if (idx%5):
		pygame.event.clear(MOUSEMOTION)

pygame.quit()
