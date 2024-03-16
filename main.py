import pygame as pg
from math import dist
import sys
pg.init()

# ~~~~~~~~~~~~~~~ Window setup ~~~~~~~~~~~~~~~ 
winW, winH = 700, 1000
WIN = pg.display.set_mode((winW, winH))
pg.display.set_caption("Color Picker")
FPS = 180
clock = pg.time.Clock()

font = pg.font.SysFont('Calibri Bold', 30)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Slider():
    def __init__(self, x, y, rad, color):
        self.x = x
        self.y = y
        self.val = 0
        self.rad = rad
        self.color = color
        self.inSlide = False

    def draw(self):
        # Draw line
        pg.draw.line(WIN, BLACK, (50, self.y), (winW-50, self.y), 3)

        # Draw circle
        pg.draw.circle(WIN, self.color, (self.x, self.y), self.rad)
        pg.draw.circle(WIN, BLACK, (self.x, self.y), self.rad, 3)

        # Draw text
        text = font.render(str(self.val), True, BLACK)
        textW, textH = font.size(str(self.val))

        WIN.blit(text, (self.x - (textW/2), self.y+(self.rad*1.2)))

    def hover(self):
        x, y = pg.mouse.get_pos()
        return dist((x, y), (self.x, self.y)) <= self.rad

def draw():
    WIN.fill(WHITE)
    red.draw()
    green.draw()
    blue.draw()
    pg.draw.rect(WIN, (red.val, green.val, blue.val), (50, 50, 600, 600))
    pg.draw.rect(WIN, BLACK, (50, 50, 600, 600), 3)

red = Slider(50, 775, 20, (255, 0, 0))
green = Slider(50, 850, 20, (0, 255, 0))
blue = Slider(50, 925, 20, (0, 0, 255))
sliders = [red, green, blue]

while True:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            for slider in sliders:
                if slider.hover():
                    slider.inSlide = True
        if event.type == pg.MOUSEBUTTONUP:
            for slider in sliders:
                slider.inSlide = False

    # Move slider and update value
    for slider in sliders:
        if slider.inSlide:
            if pg.mouse.get_pressed()[0]:
                x, y = pg.mouse.get_pos()
                if x < 50:
                    x = 50
                elif x > winW-50:
                    x = winW-50
                slider.x = x
                slider.val = round((slider.x - 50)/2.35294118)

    draw()
    pg.display.update()
