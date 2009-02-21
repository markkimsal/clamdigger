import pygame
import math
import pyengine.resource

"""module level variable to hold
loaded GraphicsSource ource objects"""

gSources = {}


def _loadGraphicsObject(source):
	"""load a GraphicsSource object from a resource
	GraphicsSource files are used for defining info about a graphic
	"""
	#print gSources
	if gSources.has_key(source):
		return gSources[source]
	
	sourceDict = {}
	execfile(pyengine.resource.fullPath("data/"+source+".py"), globals(), sourceDict)
	imageFile = pyengine.resource.fullPath(sourceDict['image'])
	sourceDict['surf'] = pygame.image.load(imageFile).convert()
	gSources[source] = sourceDict
	return sourceDict


class GraphicsObject (pygame.sprite.Sprite):
	def __init__(self, source):
		self.sourceName = source
		self.sourceObj = _loadGraphicsObject(source)
		self.__dict__.update(self.sourceObj)
		self.rect = pygame.Rect( (0,0), (self.width, self.height))
		self.rect[0]=0
		self.rect[1]=0
		self.angle=0
		self.frame=0
		#self.surf = pygame.image.load(self.image).convert()
	
	def paint(self,screen):
		screen.blit(self.surf, (self.rect[0], self.rect[1]) )

	def update(self):
		pass


class GraphicsObjectRotate(GraphicsObject):

	velocityMax = 40

	def __init__(self, source):
		pygame.sprite.Sprite.__init__(self)
		self.sourceName = source
		self.sourceObj = _loadGraphicsObject(source)
		self.image = None

		self.__dict__.update(self.sourceObj)
		#print self.width
		self.rect = pygame.Rect( (0,0), (self.width, self.height))
		self.rect[0]=0
		self.rect[1]=0
		self.angle=0
		self.frame=0
		self.velocity=0
		self.velX = 0
		self.velY = 0
		self.maskFrames = []
		self.mask = None

		# used for the rotation frames
		self.idx = 0
		self.imageFrames = []
		if(self.image):
			#car = pygame.image.load(self.image).convert()
			car = self.sourceObj['surf']
			for x in range(0,360,10):
			    imagebig = pygame.Surface ( (74,74) ).convert()
			    carrot =  pygame.transform.rotate(pygame.transform.scale2x(car), x).convert()
			    #carrot = pygame.transform.rotate(car, x)
			    rotrect = carrot.get_rect()

			    imagebig.fill( (255,0,255) )
			    imagebig.blit( carrot, ( (74 - rotrect[2] )/2, (74 - rotrect[3])/2 ) )
			    imagebig.set_colorkey( (255,0,255) )

			    self.imageFrames.append(imagebig)
			    self.maskFrames.append( pygame.mask.from_surface(imagebig) )


	def paint(self,screen):
		screen.blit(self.maskFrames[self.idx], (self.rect[0], self.rect[1]) )

	def update(self):
		if ( self.angle >= 360):
			self.angle = 0
		if ( self.angle < 0):
			self.angle = 350

		self.idx = self.angle / 10
		self.mask = self.maskFrames[self.idx]


		if (self.velocity > 0):
			self.velX = int(self.velocity * .5* math.sin( math.radians(self.angle)))
			self.velY = int(self.velocity * .5* math.cos( math.radians(self.angle)))
			self.rect[0] -= self.velX
			self.rect[1] -= self.velY

		#self.idx = self.idx+1
		#if (self.idx >= 36):
		#	self.idx = 0
		#pass

	def addVelocity(self, v):
		if (self.velocity < self.velocityMax):
			self.velocity += v
		if v < 0 and self.velocity > -10:
			self.velocity += v

