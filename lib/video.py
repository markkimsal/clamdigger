import pygame
import math

"""module level variables
"""
TILE_W=32
TILE_H=32

class WorldCamera:
	def __init__(this):
		pass

class Layer:

	pos_x = 0
	pos_y = 0
	z     = 0
	sprg  = None
	isTransparent = False
	needsRepaint = 0

	def __init__(this, z_index, size=(32,24)):
		this.z = z_index
		this.tilesWide = size[0]
		this.tilesHigh = size[1]
		this.surface = pygame.Surface((this.tilesWide*TILE_W,this.tilesHigh*TILE_H)).convert()
		this.tiles = [None]*this.tilesHigh
		for x in range(this.tilesHigh):
			this.tiles[x] = [None]*this.tilesWide
		this.velocity = 18 #pixels/second	
		this.pos_x=-TILE_W*2
		this.pos_y=-TILE_H*2

		this.surface.set_colorkey( (10,10,10) )
		this.tile_coords = [0,0]

	def clear(this):
		if (this.isTransparent):
			this.surface.fill( (10, 10, 10) )

	def setTransparent(this, on=True):
		this.isTransparent = on
		if (this.isTransparent):
			this.surface.set_colorkey( (10,10,10) )
			this.surface.fill( (10, 10, 10) )

	def move(this,x,y):
		this.pos_x += this.velocity * ( 1 + (timer.TICK_DIFF/100)) * x
		this.pos_y += this.velocity * (1 + (timer.TICK_DIFF/100)) * y

	def setNeedsRepaint(self, n=1):
		self.needsRepaint = n

	def checkLeft(this):
		if (this.pos_x < TILE_W*-4):
			pixelsover = ( (TILE_W*-4) - this.pos_x)
			#print " *** moving right"
			this.tile_coords[0] += 2
			this.pos_x =  ( (-TILE_W * 2)   - pixelsover)
			return True
		else:
			return False


	def checkRight(this):
		if (this.pos_x >= 0) :
			pixelsover = ( this.pos_x )

			#print " *** moving left"
			this.tile_coords[0] -= 2
			this.pos_x =  (( -TILE_W * 2 ) + pixelsover )
			return True
		else:
			return False


	def checkBottom(this):
		if (this.pos_y < TILE_H*-4):
			pixelsover = ( (TILE_H*-4) - this.pos_y)
			#pixelsover = 0

			#print " *** moving down"
			this.tile_coords[1] += 2
			#this.pos_y=  ( ( TILE_H * -2) ) + delta_y
			this.pos_y =  ( ( TILE_H * -2) + pixelsover) 
			return True
		else:
			return False



	def checkTop(this):
		if (this.pos_y >= 0) :
			pixelsover = (this.pos_y)
			#pixelsover = 0

			#print " *** moving up"
			this.tile_coords[1] -= 2
			this.pos_y=  ( ( -TILE_H *2 ) + pixelsover )
			return True
		else:
			return False

