#################################
# file to encapsulate video
# capabilities of pygame for
# a 2d scroller
################################

import pygame
import pygame.display
import pygame.time
import timer
import object
import pygame.locals
from pygame.locals import *


TILE_X = 16
TILE_Y = 16
SHIFT_TILE_X = 4
SHIFT_TILE_Y = 4
TICK_DIFF = 0

class VRAM:

	def __init__(this,size,title='pyengine alpha'):
		if pygame.display.get_init():
			this.surf = pygame.display.get_surface()
		else :
			pygame.display.init()
			this.screen = pygame.display.set_mode( size , DOUBLEBUF , 16)
			this.layers = []
		this.surf = pygame.Surface((320,240)).convert()
		this.screen.fill( (40,40,40))
		pygame.display.update()
		this.rect = this.surf.get_rect().move( (160,120) )
		pygame.display.set_caption(title)
		this.camera_x = 0
		this.camera_y = 0
		this.initLayers()


	def update(this):
		this.surf.fill( (0,0,0) )
		this.surf.blit(this.BG2.surface,(this.BG2.pos_x,this.BG2.pos_y))
		this.surf.blit(this.BG1.surface,(this.BG1.pos_x,this.BG1.pos_y))
		#object.draw(this.surf)
		this.surf.blit(this.BG3.surface,(this.BG3.pos_x,this.BG3.pos_y))
		this.screen.blit(this.surf, (160,120))
		pygame.display.update(this.rect)

		pass

	def initLayers(this):
		this.BG1 = Layer()
		this.BG2 = Layer()
		this.BG3 = Layer()
		this.BG4 = Layer()
		this.BG1.velocity = 2
		this.BG2.velocity = 1
		this.BG3.velocity = 0
		this.BG4.velocity = 0

	def move(this,x,y):
		this.BG1.move(x,y)
		this.BG2.move(x,y)
		this.BG3.move(x,y)


class Layer:

	def __init__(this,size=(24,24)):
		this.size = size
		this.surface = pygame.Surface((size[0]*TILE_X,size[1]*TILE_Y)).convert()
		this.tiles = [None]*size[1]
		for x in range(size[1]):
			this.tiles[x] = [None]*size[0]
		this.velocity = 18 #pixels/second	
		this.pos_x=0
		this.pos_y=0
		this.surface.set_colorkey( (0,0,0) )

	def update(this):
		cy =0
		cx = 0
		for y in range(this.size[1]):
			cy = y<<SHIFT_TILE_Y
			for x in range(this.size[0]):
				cx = x<<SHIFT_TILE_X
				this.surface.blit(this.tiles[y][x],(cx,cy))

	def move(this,x,y):
		this.pos_x += this.velocity * ( 1 + (timer.TICK_DIFF/100)) * x
		this.pos_y += this.velocity * (1 + (timer.TICK_DIFF/100)) * y



class OBJRAM:

	def __init__(this):
		this.sprites = []

	def checkCollisions(this):
		for obj in this.sprites:
			print obj

	def addSprite(this,sprite):
		this.sprites.append(sprite)


#testing
if __name__ == "__main__":

	import pygame.locals
	import pygame.event
	import pygame.image
	from pygame.locals import *
	import object
	from object import Sprite

	vram = VRAM((640,480))
	#load resources
	img = pygame.image.load('media/test.gif')
	img2 = pygame.image.load('media/tile2.gif')
	cloud = pygame.image.load('media/cloud.gif')
	blank = pygame.Surface( (16,16) ).convert()
	logo = pygame.image.load('media/pygame_tiny.gif')
	blank.fill( (0,0,0) )
	blank.set_colorkey( (0,0,0) )
	cloud.set_colorkey( cloud.get_at( (0,0)))

	#init layers
	vram.initLayers()
	layer1 = vram.BG1
	layer2 = vram.BG2
	layer3 = vram.BG3
	layer1.velocity = 2
	layer2.velocity = 1
	layer3.velocity = 5
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
	layer3.tiles[10][6] = cloud
	layer3.tiles[4][15] = cloud
	layer1.update()
	layer2.update()
	layer3.update()
	print vram



	vram.screen.blit(logo, (220,10) )
	pygame.display.update()
	#loop
	while not pygame.event.peek(QUIT):
		vram.update()
		pygame.display.update()
		timer.tick()
		#print TICK_DIFF/100.0
		pygame.event.pump()
		keystate = pygame.key.get_pressed()
		if keystate[K_LEFT]:
			vram.move(1,0)
		if keystate[K_RIGHT]:
			vram.move(-1,0)
		if keystate[K_UP]:
			vram.move(0,-1)
		if keystate[K_DOWN]:
			vram.move(0,1)

		if keystate[K_ESCAPE]:
			break

