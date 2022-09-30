"@Ohmeeky"


import pygame as pg
import sys

CAPTION = "Mouse-Rect Collision"
SCREEN_SIZE = (500, 500)
BACKGROUND_COLOR = pg.Color("darkslategrey")

  
class Sq(object):
    def __init__(self, w,h,y,x, color):
        self.w = w
        self.h = h
        self.y = y
        self.x = x
        self.color = color

    def draw(self, surface):
        pg.draw.rect(surface, self.color, [self.x, self.y, self.h, self.w])


class Circle(object):
    def __init__(self, r, center, color):
        self.r = r
        self.color = color
        self.center = center

    def draw(self, surface):
        pg.draw.circle(surface, self.color, self.center, self.r)

class Control(object):
    
    def __init__(self, center, r, can_c):
        pg.init()
        pg.display.set_caption(CAPTION)
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()
        self.FPS = 144
        self.center = center
        self.r = r
        self.color = [pg.Color("Tomato"), pg.Color("Black")]
        self.can_c = can_c
        self.done = False
        self.sq = Sq(100,100,200,200,self.color[1])

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True

    def update(self):
        self.cords = pg.mouse.get_pos()

    def render(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.sq.draw(self.screen)

    def colls(self):
        if not(self.cords[1] >= self.center[1]-self.r and self.cords[1] <= self.center[1]+self.r \
            and self.cords[0] >= self.center[0]-self.r and self.cords[0] <= self.center[0]+self.r):
            self.can_c = False
        else:
            self.can_c = True
        if self.can_c:
            self.sq.color = self.color[0]
        else:
            self.sq.color = self.color[1]
    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.render()
            self.update()
            self.colls()
            pg.display.update()
            self.clock.tick(self.FPS)

def main():
    Control((250,250), 50, False).main_loop()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()