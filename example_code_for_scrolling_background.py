import pgzrun


#screen
WIDTH = 800
HEIGHT = 600

#variables
scroll_speed = 3

#actors
#images must be same height and width as screen
scroll1 = Actor('bg', center = (WIDTH/2,HEIGHT/2))
scroll2 = Actor('bg', center = (WIDTH/2,0-HEIGHT/2))


def update():
    #move the background
    scroll1.y += scroll_speed
    scroll2.y += scroll_speed

    #move the background to the top when it reaches the bottom
    if scroll1.y > HEIGHT*1.5:
        scroll1.y = 0-HEIGHT/2
    
    if scroll2.y > HEIGHT*1.5:
        scroll2.y = 0-HEIGHT/2

def draw():
    scroll1.draw()
    scroll2.draw()

pgzrun.go()