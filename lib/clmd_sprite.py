import pygame
import gfx


class Player(gfx.GraphicsObjectRotate):
	def __init__(self):
		gfx.GraphicsObjectRotate.__init__(self,"car1")
		#print self
