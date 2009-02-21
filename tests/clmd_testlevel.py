import pygame
from pygame.locals import *

# the following line is not needed if pgu is installed
import sys; sys.path.insert(0, "..")

from pgu import tilevid, timer

SW,SH = 450,320
TW,TH = 32,32
SPEED = 4
FPS = 32



##A few functions are added to handle player/tile hits
##::
def tile_block(g,t,a):
    c = t.config
    if (c['top'] == 1 and a._rect.bottom <= t._rect.top and a.rect.bottom > t.rect.top):
        a.rect.bottom = t.rect.top
    if (c['left'] == 1 and a._rect.right <= t._rect.left and a.rect.right > t.rect.left):
        a.rect.right = t.rect.left
    if (c['right'] == 1 and a._rect.left >= t._rect.right and a.rect.left < t.rect.right):
        a.rect.left = t.rect.right
    if (c['bottom'] == 1 and a._rect.top >= t._rect.bottom and a.rect.top < t.rect.bottom):
        a.rect.top = t.rect.bottom

##




##Here I initialize the image data.  The columns are (name,file_name,shape)
##::
idata = [
    ('car1','media/car1.png',(0,0,32,32)),
    ]
##
##Here I initialize the code data.  The columns are (function, config).
##::
cdata = {
    0:(tile_block,(0,0,32,32)),
}
##
 

##Here I initialize the tile data.  The columns are (groups,function,config)
##::
tdata = {
    0x01:('car1',tile_block,{'top':1,'bottom':1,'left':1,'right':1}),
    0x02:('car1',tile_block,{'top':1,'bottom':1,'left':1,'right':1}),
    }
##


##This is the initialization function I created for
##the game.
##
##I use the tga_ methods to load up the tiles and level I created.
##::
def init():
    g = tilevid.Tilevid()

    g.screen = pygame.display.set_mode((SW,SH),SWSURFACE)
    
    g.tga_load_tiles('media/clmd_tiles.tga',(TW,TH), tdata)
    g.tga_load_level('media/clmd_level_1.tga',1)

    ##In init(), loading in the sprite images.
    ##::
    g.load_images(idata)
    ##
    
    ##In init(), running the codes for the initial screen.
    ##::
    #g.run_codes(cdata,(0,0,25,17))
    #g.run_codes(cdata, (0,0,25,10))
    ##
 
    return g
##
    
##This is the run function I created for the game.  In this example,
##the level is displayed, but there is no interaction (other than allowing the
##user to quit via ESC or the QUIT signal.
##::
def run(g): 
    g.quit = 0
    
    g.paint(g.screen)
    pygame.display.flip()
    t = timer.Timer(FPS)
    
    while not g.quit:
        for e in pygame.event.get():
            if e.type is QUIT: g.quit = 1
            if e.type is KEYDOWN and e.key == K_ESCAPE: g.quit = 1
        
        ##In run(), each frame I move the view to the right by SPEED pixels.
        ##::
        #g.view.x += SPEED
        ##

        #g.run_codes(cdata,(g.view.right/TW,0,1,1))

	#g.screen.fill( (0,0,0) )
        #g.paint(g.screen)
        g.loop()
        updates = g.update(g.screen)
        pygame.display.update(updates)


        ##In run(), at the end of each frame, I give the timer a tick.  The timer will delay the 
        ##appropriate length.
        ##::
        t.tick()
        ##
 
##    
    
run(init())
