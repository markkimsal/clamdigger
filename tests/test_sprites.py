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
from lib import gfx, video, level, clmd_sprite, world
import pygame.time

import pyengine
import pyengine.object

from copy import deepcopy

#from pyengine import object

game = world.GameWorld((800,600), 'The object of the game is to find parking')
#worldRect = Rect(-32, -32, 1670, 1220)


foo = clmd_sprite.Player()
foo.angle  =  200
game.setPlayerSprite(foo)

level = level.GameLevel("test");
print level
worldRect = level.getRect()
print worldRect


game.setLevel(level)


keypress = pygame.event.poll()
key = keypress.type
idx = 0
keyStatus = KEYUP
velocityDelta = 0
angleDelta = 0

sprg = pyengine.object.SpriteGroup()
enemy1 = lib.gfx.GraphicsObjectRotate('car2')
enemy1.rect[0] = 240
enemy1.rect[1] =  75
enemy1.angle  =  270
enemy1.update()
sprg.add(enemy1)

timer = pygame.time.Clock()

def doCollisions(group, sprite):
	collide = pygame.sprite.spritecollide(sprite,  group, False)
	if len(collide) >0:
		#print "rectangle"
		sprites = group.sprites()
		for spr in sprites:
			pass
			if(pygame.sprite.spritecollide(sprite,  group, False, pygame.sprite.collide_mask)):
				currentSpriteRect = sprite.rect
				sprite.velocity = sprite.velocity * -1
				sprite.update()
				sprite.velocity = .1


while (True):
	timer.tick(40)

	if (key == QUIT):
			break
	if (key == KEYDOWN):
		keyStatus = KEYDOWN
		if ( keypress.key == K_ESCAPE):
			break
		if (keypress.key == K_LEFT):
			if velocityDelta >= 1:
				angleDelta = 10
			else:
				angleDelta = 2
		if (keypress.key == K_RIGHT):
			if velocityDelta >= 1:
				angleDelta = -10
			else:
				angleDelta = -2
		if (keypress.key == K_f):
			pass


		if (keypress.key == K_UP):
			if (velocityDelta < 6):
				velocityDelta += 1

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

	foo.update()
	currentSpriteRect = foo.rect
	for sprx in (0,1):
		if worldRect[sprx] > currentSpriteRect[sprx]:
			foo.rect[sprx] = worldRect[sprx]

	if worldRect.right < currentSpriteRect[0] + foo.width:
		foo.rect[0] = worldRect.right - foo.width

	if worldRect.bottom < currentSpriteRect[1] + foo.height:
		foo.rect[1] = worldRect.bottom - foo.height

	doCollisions(sprg, foo)

	game.updateWorld()
	game.paintWorld()
	#game.paintSprite(foo)

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
