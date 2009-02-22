import pygame
import math

"""module level variables
"""
TILE_W=32
TILE_H=32

class WorldCamera:
	def __init__(this):
		pass

class GameWorld:

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


	def paintWorld(self):
#		self.screen.fill( (0,0,0) )
		self.screen.blit(self.BG1.surface, (self.BG1.pos_x, self.BG1.pos_y))

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


		#print self.BG1.pos_x
		#print "camera x ", self.camera_x, "         camera y ", self.camera_y
		#print "bg1 x ", self.BG1.pos_x, "        bg1 y ", self.BG1.pos_y
		if (self.BG1.pos_x < TILE_W*-4):
			#print "camera x ", self.camera_x, "         camera y ", self.camera_y
			#print "bg1 x ", self.BG1.pos_x, "        bg1 y ", self.BG1.pos_y
			pixelsover = ( (TILE_W*-4) - self.BG1.pos_x)
			#print "pixels over edge ", pixelsover
			#print " *** moving right"
			self.BG1.tile_coords[0] += 2
			self.currentLevel.paintOnLayer(self.BG1)
			self.BG1.pos_x =  ( (-TILE_W * 2)   - pixelsover)
			#self.camera_x += pixelsover

		if (self.BG1.pos_x > 0) :
			#print "camera x ", self.camera_x, "         camera y ", self.camera_y
			#print "bg1 x ", self.BG1.pos_x, "        bg1 y ", self.BG1.pos_y
			pixelsover = ( self.BG1.pos_x )
			#print "pixels over edge ", pixelsover

			#print " *** moving left"
			self.BG1.tile_coords[0] -= 2
			self.currentLevel.paintOnLayer(self.BG1)
			self.BG1.pos_x =  (( -TILE_W * 2 ) + pixelsover )
			#self.camera_x -= self.BG1.pos_x

		if (self.BG1.pos_y < TILE_H*-4):
			#print "camera x ", self.camera_x, "         camera y ", self.camera_y
			#print "bg1 x ", self.BG1.pos_x, "        bg1 y ", self.BG1.pos_y
			pixelsover = ( (TILE_H*-4) - self.BG1.pos_y)
			#print "pixels over edge ", pixelsover

			#print " *** moving down"
			self.BG1.tile_coords[1] += 2
			self.currentLevel.paintOnLayer(self.BG1)
			#self.BG1.pos_y=  ( ( TILE_H * -2) ) + delta_y
			self.BG1.pos_y =  ( ( TILE_H * -2) - pixelsover) 
			#self.camera_y -= pixelsover

		if (self.BG1.pos_y > 0) :
			#print "camera x ", self.camera_x, "         camera y ", self.camera_y
			#print "bg1 x ", self.BG1.pos_x, "        bg1 y ", self.BG1.pos_y
			pixelsover = (self.BG1.pos_y)
			#print "pixels over edge ", pixelsover

			#print " *** moving up"
			self.BG1.tile_coords[1] -= 2
			self.currentLevel.paintOnLayer(self.BG1)
			self.BG1.pos_y=  ( ( -TILE_H *2 ) + pixelsover )
			#self.camera_y += pixelsover


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
	
class Layer:

	pos_x = 0
	pos_y = 0

	def __init__(this,size=(32,24)):
		this.tilesWide = size[0]
		this.tilesHigh = size[1]
		this.surface = pygame.Surface((this.tilesWide*TILE_W,this.tilesHigh*TILE_H)).convert()
		this.tiles = [None]*this.tilesHigh
		for x in range(this.tilesHigh):
			this.tiles[x] = [None]*this.tilesWide
		this.velocity = 18 #pixels/second	
		this.pos_x=-TILE_W*2
		this.pos_y=-TILE_H*2

		this.surface.set_colorkey( (0,0,0) )
		this.tile_coords = [0,0]

#	def update(this):
#		cy =0
#		cx = 0
#		for y in range(this.size[1]):
#			cy = y<<SHIFT_TILE_H
#			for x in range(this.size[0]):
#				cx = x<<SHIFT_TILE_W
#				this.surface.blit(this.tiles[y][x],(cx,cy))

	def move(this,x,y):
		this.pos_x += this.velocity * ( 1 + (timer.TICK_DIFF/100)) * x
		this.pos_y += this.velocity * (1 + (timer.TICK_DIFF/100)) * y

