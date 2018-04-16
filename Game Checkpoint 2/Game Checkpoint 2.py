import pygame
import random
from os import path

pygame.init()


WIDTH = 1280
HEIGHT = 760
FPS = 60

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#Player Sprite
img = pygame.image.load('spaceship.png')

#Mob Sprite
img1 = pygame.image.load('asteroid.png')

#initialize pygame and create window
pygame.mixer.init()
background = pygame.image.load('background.png')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids!")
clock = pygame.time.Clock()
pygame.mixer.music.load('gamesound.wav')
pygame.mixer.music.play(loops=0, start=0.0)


class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((20, 50))
##        self.image.fill(BLUE)
##        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 300
        self.speedx = 0      
    

    def update(self):
        self.speedx = 0        
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -15
       # if keystate[pygame.K_UP]:#Working on up and down keys
           
        if keystate[pygame.K_RIGHT]:
            self.speedx = 15
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0     
            
    
    def shoot(self):       
        bullet = Bullet(self.rect.centerx, self.rect.top)      
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = img1
        self.rect = self.image.get_rect()
        
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((30, 40))
##        self.image.fill(RED)
##        self.rect = self.image.get_rect()
##        self.rect.x = random.randrange(WIDTH - self.rect.width)
##        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)   

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(30):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

#Game loop
running = True
while running:    
    #keep loop running at the right speed
    clock.tick(FPS)
    #Process input (events)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
                
    #Update
    all_sprites.update()

    #check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = True
        print("You Lose!")

    #Draw
    screen.fill(WHITE)   
    screen.blit(background,[0,0])
    all_sprites.draw(screen)
    #After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
