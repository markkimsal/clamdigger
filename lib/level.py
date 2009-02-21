import pygame
import gfx
import pygame.font

import math
import pyengine

"""module level variable for holding loaded level sources
"""
lSources = {}


""" module level function for loading a level from a .txt file
"""
def _loadLevelSource(source):
	if lSources.has_key(source):
		return lSources[source]
	
	sourceDict = {}

	dataFile = pyengine.resource.fullPath("data/levels/"+source+".py")
	execfile(dataFile, globals(), sourceDict)
	lSources[source] = sourceDict
	return sourceDict
	pass


class GameLevel:

	mapTiles = {}

	def __init__(self, name, tilesize = (32,32)):
		self.name = name
		self.sourceObj = _loadLevelSource(name)
		self.__dict__.update(self.sourceObj)

		self.tileSize = tilesize
		pygame.font.init()	
		self.fuglyfont = pygame.font.SysFont( pygame.font.get_default_font(), 16)
		#self.surf = pygame.Surface(size)
		#self.paintLevel()


	def paintLevel(self, gX=0, gY=0):
		y=0
		for line in self.ldata:
			x=0
			for char in line:
				pygame.draw.rect( self.surf, ( 0, 10 * x, 255 ), (x*self.tileSize[0], y*self.tileSize[1], 32, 32) )
				if ( self.ldata[y][x] == '.'):
					tile = gfx.GraphicsObject("plot_empty")
					self.surf.blit(tile.surf, (x*self.tileSize[0], y*self.tileSize[1] ))
				if ( self.ldata[y][x] == '>'):
					tile = gfx.GraphicsObject("plot_left")
					self.surf.blit(tile.surf, (x*self.tileSize[0], y*self.tileSize[1] ))
				if ( self.ldata[y][x] == '<'):
					tile = gfx.GraphicsObject("plot_right")
					self.surf.blit(tile.surf, (x*self.tileSize[0], y*self.tileSize[1] ))

				x+=1
			y+=1

	def paintOnLayer(self, layer):
		"""Use the layer's "tile_coords" to find the right tiles"""
		visibleTilesX=36
		visibleTilesY=25
		layer.surface.fill( (100,100,255))
		#paint a visible square where this layer "thinks" the camera viewport is

		#paint entire layer first for debugging purposes
		#for y in range (layer.tilesHigh):
		#	for x in range (layer.tilesWide):
		#		pygame.draw.rect( layer.surface, ( 0, 10 * x, 255 ), (x*self.tileSize[0], y*self.tileSize[1], 32, 32) )

		self.initMapTiles()
#		print coords
		gTileY = layer.tile_coords[1]
		gTileX = layer.tile_coords[0]
		#print "gtilex ",gTileX
		#print "gtiley ",gTileY

		if (gTileX < 0):
			gTileX = 0
		if (gTileY < 0):
			gTileY = 0


		gTileOffsX = gTileX + visibleTilesX
		gTileOffsY = gTileY + visibleTilesY

		#if (gTileOffsX < 0):
		#	gTileOffsX =0
		#if (gTileOffsY < 0):
		#	gTileOffsY =0

		if (gTileOffsX > len(self.ldata[0])):
			gTileOffsX =len(self.ldata[0])
		if (gTileOffsY > len(self.ldata)):
			gTileOffsY =len(self.ldata)

		y=0
		for row in range(gTileY, gTileOffsY):
			try:
				line = self.ldata[row]
			except IndexError:
				y+=1
				continue

#			print line
			x=0
			for quantum in range(gTileX, gTileOffsX):
				#numtile = self.fuglyfont.render("" +`gTileX`+", "+`gTileY`, 0, (255,255,255))
				try:
					char = line[quantum]
				except IndexError:
					x+=1
					continue
				if ( char == '.'):
					tile = self.mapTiles['emptyTile']
					#layer.surface.blit(emptyTile.surf, (x*self.tileSize[0], y*self.tileSize[1] ))
					#pygame.draw.rect(layer.surface, (255,0,0), (x*self.tileSize[0], y*self.tileSize[1], 32, 32) ,1)
#					str = ''.join([x.__str__(), ',',y.__str__()])
#					layer.surface.blit(fuglyfont.render( str,0, (255,255,255)).convert(), (x*self.tileSize[0],y*self.tileSize[1]))
				if ( char == '>'):
					tile = self.mapTiles['leftTile']
					#layer.surface.blit(tile.surf, (x*self.tileSize[0], y*self.tileSize[1] ))
				if ( char == '<'):
					tile = self.mapTiles['rightTile']
					#layer.surface.blit(tile.surf, (x*self.tileSize[0], y*self.tileSize[1] ))

				if ( char == '+'):
					tile = self.mapTiles['crossTile']
				if ( char == '|'):
					tile = self.mapTiles['vertTile']
					#layer.surface.blit(vertTile.surf, (x*self.tileSize[0], y*self.tileSize[1] ))
				if ( char == '-'):
					tile = self.mapTiles['horizTile']
					#layer.surface.blit(horizTile.surf, (x*self.tileSize[0], y*self.tileSize[1] ))

				layer.surface.blit(tile.surf, (x*self.tileSize[0], y*self.tileSize[1] ))

				#layer.surface.blit(numtile, (x*self.tileSize[0], y*self.tileSize[1] ))
				x+=1
			y+=1

		#pygame.draw.rect(layer.surface, (0,255,0), (32,32, 640, 480), 2)

	def initMapTiles(self):
		if len(self.mapTiles) < 1:
			self.mapTiles['emptyTile'] = gfx.GraphicsObject("plot_empty")
			self.mapTiles['crossTile'] = gfx.GraphicsObject("plot_cross")
			self.mapTiles['vertTile']  = gfx.GraphicsObject("plot_vert")
			self.mapTiles['horizTile'] = gfx.GraphicsObject("plot_horiz")
			self.mapTiles['leftTile']  = gfx.GraphicsObject("plot_left")
			self.mapTiles['rightTile'] = gfx.GraphicsObject("plot_right")
