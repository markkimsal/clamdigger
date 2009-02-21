import sys, os

if hasattr(sys, 'frozen'):
	CLMD_fullpath = os.path.join(
			os.path.dirname(os.path.abspath(sys.executable)), '..')
else:
	CLMD_fullpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')


sys.path.append( os.path.join(CLMD_fullpath, 'pyengine'))

import video
from video import *

import pygame.locals
import pygame.event
import pygame.image
from pygame.locals import *

import object
from object import Sprite, SpriteGroup

def loadMedia(relative):
	global CLMD_fullpath
	dirs = os.path.split(relative)
	fullpath = ''

	for x in dirs:
		fullpath = os.path.join(fullpath, x)

	fullpath = os.path.join(CLMD_fullpath, fullpath)
	return fullpath



if __name__ == "__main__":


	vram = VRAM((640,480))
	print vram
	#load resources
	img = pygame.image.load(loadMedia('media/car1.png'))
	img2 = pygame.image.load(loadMedia('media/car2.png'))
	#cloud = pygame.image.load('media/menu_head2.png')
	blank = pygame.Surface( (32,32) ).convert()
	#logo = pygame.image.load('media/pygame_tiny.gif')

	blank.fill( (0,0,0) )
	blank.set_colorkey( (0,0,0) )
	#cloud.set_colorkey( cloud.get_at( (0,0)))
	#sprite.set_colorkey( sprite.get_at( (0,0) ))

	#scope
	layer1 = vram.BG1
	layer2 = vram.BG2
	layer3 = vram.BG3
	layer4 = vram.BG4

	stopwatch = pygame.time.Clock()
	print layer1
	print layer2
	for y in range(24):
		for x in range(24):
			#print x,y
			layer2.tiles[y][x] = img2
			layer3.tiles[y][x] = blank

			if y > 10:
				layer1.tiles[y][x] = img
			else:
				layer1.tiles[y][x] = blank
	#layer3.tiles[0][0] = cloud
	layer1.update()
	layer2.update()
	layer3.update()
	print vram

	#sprites
	sprite = pygame.image.load(loadMedia('media/car1.png'))
	sp1 = Sprite(sprite);
	sp1.pos_y = 120
	sp1.pos_x = 160
	sprg = SpriteGroup()
	sprg.addObj(sp1);

	pygame.display.update()
	#loop
	bobber = 0
	ticks=0
	new_ticks=0
	delta_ticks=0
	get_ticks = pygame.time.get_ticks

	#music
	#pygame.mixer.init()
	#pygame.mixer.music.load('media/Beneath The Surface.it')
	#pygame.mixer.music.play()

	while not pygame.event.peek(QUIT):
		vram.update()
		pygame.display.update()
		timer.tick()
		#print TICK_DIFF/100.0
		pygame.event.pump()
		keystate = pygame.key.get_pressed()
		if keystate[K_LEFT]:
			vram.move(1,0)
			sp1.move(-1,0)
		if keystate[K_RIGHT]:
			vram.move(-1,0)
			sp1.move(1,0)
		if keystate[K_UP]:
			#vram.move(0,-1)
			sp1.move(0,-1)
		if keystate[K_DOWN]:
			sp1.move(0,1)
			#vram.move(0,1)

		if keystate[K_ESCAPE]:
			break	
		bobber += 1
		if (bobber >= 40 ) :
			new_ticks = get_ticks()
			delta_ticks = new_ticks - ticks
			print (40.0 / delta_ticks) * 10000.00
			ticks = new_ticks
			bobber = 0


