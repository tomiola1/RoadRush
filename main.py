import pygame, sys
from pygame.locals import *
import random, time
from pygame import mixer
from settings import *
from sprites import *

 
#initialising
pygame.init()
 
#Setting up Fonts
font = pygame.font.SysFont("Calibri", 60)
font_small = pygame.font.SysFont("Calibri", 20)
game_over = font.render("Game Over", True, BLACK)
#highscore = font.render()
 
#Create a white screen 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)
pygame.display.set_caption(TITLE)
 
 
class Enemy(pygame.sprite.Sprite): #enemy class
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("enemy.png")
        self.surf = pygame.Surface((58, 58))
        self.rect = self.surf.get_rect(center = (550, 245))
      
      def move(self):
        global SCORE
        self.rect.move_ip(-SPEED, 0)
        if (self.rect.right < -58):#if off screen to the left
            SCORE += 1 #the score value is adapted accordingly
            self.rect.right = 600
            self.rect.center = (658, random.randint(70, HEIGHT - 50)) #back to end of x, random position on y



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
    if pygame.sprite.spritecollideany(player, coins): #if player collects coin
      pygame.mixer.Sound('power.wav').play()
      SCORE += 5
      COL += 1 #the value for coins collected is adapted
      self.rect.right = 600
      self.rect.center = (645, random.randint(70, HEIGHT - 50))
    if (self.rect.right < -45):#if off screen to the left without colliding
      self.rect.right = 600 #still respawn randomly 
      self.rect.center = (645, random.randint(70, HEIGHT - 50))

class Pot(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("pothole.png")
    self.surf = pygame.Surface((30, 17))
    self.rect = self.surf.get_rect(center = (550, 310))

  def move(self):
    global SCORE 
    global MIN
    self.rect.move_ip(-2, 0)
    if pygame.sprite.spritecollideany(player, pots):
      pygame.mixer.Sound('neg.wav').play()
      SCORE -= 3
      MIN += 3
      self.rect.right = 600
      self.rect.center = (630, random.randint(70, HEIGHT - 50))
    if (self.rect.right < -30):
      self.rect.right = 600
      self.rect.center = (630, random.randint(70, HEIGHT - 50))


#Setting up Sprites        
player = Player()
enemy = Enemy()
coin = Coin()
pothole = Pot()
 
bg = Background()
 
#sprite groups for collision
enemies = pygame.sprite.Group()
enemies.add(enemy)
coins = pygame.sprite.Group()
coins.add(coin)
pots = pygame.sprite.Group()
pots.add(pothole)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin)
all_sprites.add(pothole)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT 
pygame.time.set_timer(INC_SPEED, 1000)

'''mixer.init()
mixer.music.load('power.wav')
mixer.music.play()'''

 
#Game Loop
while True:
       
    #Cycles through all occurring events   
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
 
    bg.update()
    bg.render()
 
    score = font_small.render("Score: " + str(SCORE), True, WHITE)
    col = font_small.render("Collected: " + str(COL), True, GOLD)
    min = font_small.render("MINUS: -" + str(MIN), True, RED)
    #highscore = font_small.render(str(HS), True, WHITE )
    screen.blit(score, (10,10))
    screen.blit(col, (110,10))
    screen.blit(min, (250, 10))
 
    #moves and redraws all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

 
    #runs if player and enemy collide      
    if pygame.sprite.spritecollideany(player, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(1) #time delay
                    
          screen.fill(BGCOLOUR)
          screen.blit(game_over, (140,150))
          #screen.blit(highscore, (140, 200))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(5)
          pygame.quit()
          sys.exit()
         
    pygame.display.update()
    clock.tick(FPS)
