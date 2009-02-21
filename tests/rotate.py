import pygame
from pygame.locals import *

import sys, os

if hasattr(sys, 'frozen'):
	CLMD_fullpath = os.path.join(
			os.path.dirname(os.path.abspath(sys.executable)), '..')
else:
	CLMD_fullpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')


sys.path.append( os.path.join(CLMD_fullpath, 'pyengine'))

import video
from video import *

import object
from object import Sprite

def loadMedia(relative):
	global CLMD_fullpath
	dirs = os.path.split(relative)
	fullpath = ''

	for x in dirs:
		fullpath = os.path.join(fullpath, x)

	fullpath = os.path.join(CLMD_fullpath, fullpath)
	return fullpath





def main():
	pygame.init()
	screen = pygame.display.set_mode([640, 480], pygame.HWSURFACE| pygame.DOUBLEBUF)
	pygame.display.set_caption("I can dig more clams than you, stupid.")
	print pygame.display.get_driver() + " driver init."
	myinfo = pygame.display.Info()
	print myinfo


	car = pygame.image.load(loadMedia('media/car1.png'));
	carB = pygame.image.load(loadMedia('media/car2.png'));
	carC = pygame.image.load(loadMedia('media/carx.png'));
	car.set_colorkey( (255,0,255) )
	carB.set_colorkey( (255,0,255) )
	carC.set_colorkey( (255,0,255) )



	key = pygame.event.poll().type
	cars = []
	carsB = []
	carsC = []
	for x in range(0,360,10):
	    carbig = pygame.Surface ( (74,74) )
	    carrot =  pygame.transform.rotate(pygame.transform.scale2x(car), x) 
	    #carrot = pygame.transform.rotate(car, x)
	    rotrect = carrot.get_rect()

	    carbig.fill( (255,0,255) )
	    carbig.blit( carrot, ( (74 - rotrect[2] )/2, (74 - rotrect[3])/2 ) )
	    carbig.set_colorkey( (255,0,255) )

	    cars.append(carbig)


	for x in range(0,360,10):
	    carbig = pygame.Surface ( (74,74) )
	    carrot =  pygame.transform.rotate(pygame.transform.scale2x(carB), x) 
	    rotrect = carrot.get_rect()
	    carbig.fill( (255,0,255) )
	    carbig.blit( carrot, ( (74 - rotrect[2] )/2, (74 - rotrect[3])/2 ) )
	    carbig.set_colorkey( (255,0,255) )

	    carsB.append(carbig)

	for x in range(0,360,10):
	    carbig = pygame.Surface ( (74,74) )
	    carrot =  pygame.transform.rotate(pygame.transform.scale2x(carC), x) 
	    rotrect = carrot.get_rect()
	    carbig.fill( (255,0,255) )
	    carbig.blit( carrot, ( (74 - rotrect[2] )/2, (74 - rotrect[3])/2 ) )
	    carbig.set_colorkey( (255,0,255) )

	    carsC.append(carbig)




	idx = 0
	while key != KEYDOWN:
	    screen.fill( (60,60,60)  )
	    screen.blit( cars[idx], (0,0))
	    screen.blit( carsB[idx], (0,74))
	    screen.blit( carsC[idx], (0,148))
	    pygame.display.update()
	    idx += 1
	    if (idx >= 36):
		    idx = 0



	    key = pygame.event.poll().type
    	    pygame.time.wait(40) 

if __name__ == "__main__":
	main()
	#profile.run('main()')

