import pygame, sys
from settings import *
from pygame.locals import *
import random, time


WIDTH = 600
HEIGHT = 400
SPEED = 5
SCORE = 0
COL = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)
pygame.display.set_caption(TITLE)

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("enemy.png")
        self.surf = pygame.Surface((58, 58))
        self.rect = self.surf.get_rect(center = (550, 245))
      
      def move(self):
        global SCORE
        self.rect.move_ip(-SPEED, 0)
        if (self.rect.right < -58):
            SCORE += 1
            self.rect.right = 600
            self.rect.center = (658, random.randint(65, HEIGHT - 45))

 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("player.png")
        self.surf = pygame.Surface((58, 58))
        self.rect = self.surf.get_rect(center = (150, 180))
        
    def move(self):
        keys = pygame.key.get_pressed()         
        if self.rect.top > 65:
              if keys[K_UP]:
                  self.rect.move_ip(0, -5)
        if self.rect.bottom < 355:        
              if keys[K_DOWN]:
                  self.rect.move_ip(0, 5)

class Coin(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("coin.png")
    self.surf =  pygame.Surface((45, 45))
    self.rect = self.surf.get_rect(center = (550, 100))

  def move(self):
    global SCORE
    global COL
    self.rect.move_ip(-3, 0)
    if pygame.sprite.spritecollideany(player, coins):
      SCORE += 5
      COL += 1
      self.rect.right = 600
      self.rect.center = (645, random.randint(65, HEIGHT - 45))

class Background():
      def __init__(self):
            self.bgimage = pygame.image.load('track.png')
            self.rectBGimg = self.bgimage.get_rect()
 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = 0
            self.bgX2 = self.rectBGimg.width
 
            self.moving_speed = 4
         
      def update(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width
             
      def render(self):
         screen.blit(self.bgimage, (self.bgX1, self.bgY1))
         screen.blit(self.bgimage, (self.bgX2, self.bgY2))
