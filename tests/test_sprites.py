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
import pyengine.object
#from pyengine import object

game = video.GameWorld((800,600), 'The object of the game is to find parking')


foo = clmd_sprite.Player()

level = level.GameLevel("test");
print level


game.setLevel(level)


keypress = pygame.event.poll()
key = keypress.type
idx = 0
keyStatus = KEYUP
velocityDelta = 0
angleDelta = 0

sprg = pyengine.object.SpriteGroup()
enemy1 = lib.gfx.GraphicsObjectRotate('car2')
enemy1.rect[0] = 80
enemy1.rect[1] = 104
enemy1.angle  =  340
enemy1.update()
sprg.add(enemy1)
print enemy1.maskFrames[enemy1.idx].get_at((3,3))

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
	game.doCollisions(sprg, foo)

	#pygame.draw.rect( game.screen, ( 0, 10, 255 ), (enemy1.rect[0] - game.camera_x, enemy1.rect[1] - game.camera_y, enemy1.rect[2], enemy1.rect[3]) )
	game.screen.blit(enemy1.imageFrames[enemy1.idx], (enemy1.rect[0] - game.camera_x, enemy1.rect[1] - game.camera_y) )
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
