import pygame as pg

FPS = 60

pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()

class Button:
   def __init__(self, color, x, y, width, height):
    self.color = color
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    
   def draw(self):
        print('hello from draw')
    
btn_yes = Button()

running = True
while running:
    clock.tick(FPS)
    
    list_events = pg.event.get()
    for event in list_events:
        if event.type == pg.QUIT:
            running = False
    print(list_events)
    
    pg.display.update()

pg.quit()