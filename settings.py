import pygame

FPS = 60
clock = pygame.time.Clock()
TITLE = "ROAD RUSH!"

#other variables
WIDTH = 600
HEIGHT = 400
SPEED = 5
SCORE = 0
COL = 0
MIN = 0
HS = "highscore.txt"
 
#colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)
GREEN = (72, 111, 56)
GREY = (128, 128, 128)
GOLD = (255, 215, 0)
BGCOLOUR = GREEN
LINECOLOUR = WHITE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)
pygame.display.set_caption(TITLE)

#button colours
LIGHT = (170,170,170)
DARK = (100,100,100)

LANE1 = (150, 100) 
LANE2 = (150, 170)
LANE3 = (150, 245)
LANE4 = (150, 320)
 
