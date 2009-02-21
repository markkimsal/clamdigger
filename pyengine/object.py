#########################
# file for handling 
# sprites in a pygame
# game engine
#########################

import pygame
import pygame.locals
import pygame.sprite
import timer

class Sprite(pygame.sprite.Sprite):

	def __init__(this,i):
		pygame.sprite.Sprite.__init__(this)
		this.image = i
		this.velocity_x = 2
		this.velocity_y = 2
		this.velocity_z = 0
		this.pos_x = 0
		this.pos_y = 0

	def move (this,x,y):
		this.pos_x += this.velocity_x * (1+ (timer.TICK_DIFF/100)) * x
		this.pos_y += this.velocity_y * (1+ (timer.TICK_DIFF/100)) * y


class SpriteGroup(pygame.sprite.Group):

	def draw(self, surface):
		"""draw(surface)
		draw all sprites onto the surface

		Draws all the sprites onto the given surface."""

		sprites = self.sprites()
		surface_blit = surface.blit
		for spr in sprites:
			self.spritedict[spr] = surface_blit(spr.image, (s.pos_x, s.pos_y))
		self.lostsprites = []

	def addObj(self, o):
		pygame.sprite.Group.add(self, o)
		#self.sprites().append(o)

	def update():
		TICK_DIFF = pyengine.timer.TICK_DIFF
		sprites = self.sprites()
		for s in sprites:
			s.move(x,y)

