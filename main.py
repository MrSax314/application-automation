import pyautogui as pg
import time 
 # Default Settings
pg.PAUSE = 0.5
width, height = pg.size() 
x = width/2
y = height/2
time.sleep(2)

def GTRI():
    ## Personal details
    # scroll to bottom, select image (continue)
    pg.leftClick(x,y)
    pg.scroll(-10000) # DOWN
    handleImage('images/continue.png',5,10)

    ## EU
    handleImage('images/eu.png',25,50)
    pg.scroll(-10000)
    handleImage('images/continue.png',5,10)

    ## Job QUesiotnaire
    # Yes - drop down none
    # No
    # continue

    ## Documents
    # most recent
    # cont.

    ## Education
    # scroll to bottom 
    # cont.

    ## Ethniciy
    # male 
    # hispanics
    # cont.

    ## Vet
    # Scroll, not prot vet. cont. 


    # DIsability
    # scroll , no , cont.

    ## FInal
    # dropdown, career website , submit
def handleImage(image,xOffset,yOffset):
    time.sleep(1)
    (l, t, w, h) = pg.locateOnScreen(image)
    pg.leftClick(l+xOffset,t+yOffset)

GTRI()