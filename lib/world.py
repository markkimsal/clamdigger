import pygame
import pygame.locals
from pygame.locals import *
import lib
from lib import gfx, video, level, clmd_sprite
from lib.video import Layer
import pygame.time


class GameWorld:
	"""Define a game world, rules, sprites, levels, etc."""

	def __init__(this,size,title='Gameworld Screen'):
		if pygame.display.get_init():
			this.screen = pygame.display.get_surface()
		else :
			pygame.display.init()
			this.screen = pygame.display.set_mode( size , pygame.locals.DOUBLEBUF , 16)
		this.size = size
		this.layers = []
		this.initLayers()
		this.screen.fill( (40,40,40))
		pygame.display.update()
		pygame.display.set_caption(title)
		this.camera_x = 0
		this.camera_y = 0
		this.currentLevel = None


	def initLayers(this):
		this.BG1 = Layer()
		this.BG2 = Layer()
		this.BG3 = Layer()
		this.BG4 = Layer()


	def setLevel(self, l):
		self.currentLevel = l
		self.currentLevel.paintOnLayer(self.BG1)
		self.currentLevel.paintOnLayer(self.BG2, 2)


	def paintWorld(self):
#		self.screen.fill( (0,0,0) )
		self.screen.blit(self.BG1.surface, (self.BG1.pos_x, self.BG1.pos_y))
		self.screen.blit(self.BG3.surface, (self.BG3.pos_x, self.BG3.pos_y))
		self.screen.blit(self.BG2.surface, (self.BG2.pos_x, self.BG2.pos_y))

	def moveCamera(self,delta_x=0, delta_y=0):
		self.camera_y +=  delta_y
		self.camera_x +=  delta_x
		"""
		if (self.camera_y < 0 ):
			self.camera_y = 0
		if (self.camera_x < 0 ):
			self.camera_x = 0
			"""


		self.BG1.pos_x -= delta_x
		self.BG1.pos_y -= delta_y

		self.BG2.pos_x -= delta_x
		self.BG2.pos_y -= delta_y

		#print self.BG1.pos_x
		#print "camera x ", self.camera_x, "         camera y ", self.camera_y
		#print "bg1 x ", self.BG1.pos_x, "        bg1 y ", self.BG1.pos_y
		if (self.BG1.checkLeft()):
			self.currentLevel.paintOnLayer(self.BG1)

		if (self.BG1.checkRight()):
			self.currentLevel.paintOnLayer(self.BG1)


		if (self.BG1.checkBottom()):
			self.currentLevel.paintOnLayer(self.BG1)

		if (self.BG1.checkTop()):
			self.currentLevel.paintOnLayer(self.BG1)

	def paintSprite(self, sprite):
		"""adjust the camera movement to keep the sprite in view
		"""
		#__FIXME__ use tilesize * 4 instead of 128
		if sprite.rect[0] > (self.camera_x + self.size[0] - 128) and sprite.velX < 0:
			self.moveCamera( (130 + (sprite.rect[0] - self.camera_x - self.size[0]) ), 0)

		if sprite.rect[1] > (self.camera_y + self.size[1] - 128) and sprite.velY < 0:
			self.moveCamera(0, (130 + (sprite.rect[1] - self.camera_y - self.size[1]) ) )
			
		if sprite.rect[0] < (self.camera_x + 70) and self.camera_x > 0 and sprite.velX > 0:
			self.moveCamera(  -64+(sprite.rect[0] - self.camera_x ), 0)

		if sprite.rect[1] < (self.camera_y + 70) and self.camera_y > 0 and sprite.velY > 0:
			self.moveCamera(0, -64+( sprite.rect[1] - self.camera_y ))

			#print "sprite ", sprite.rect[0], sprite.rect[1]
			#print "vel ", sprite.velX, sprite.velY
			#print "camera ", self.camera_x, self.camera_y
		#pygame.draw.rect( self.screen, ( 0, 10, 255 ), (sprite.rect[0] - self.camera_x, sprite.rect[1] - self.camera_y, sprite.rect[2], sprite.rect[3]) )
		self.screen.blit(sprite.imageFrames[sprite.idx], (sprite.rect[0] - self.camera_x, sprite.rect[1] - self.camera_y) )
	
