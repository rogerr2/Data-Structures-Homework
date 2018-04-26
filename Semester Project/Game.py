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

#Game Over
def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "Asteroids!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Left and right arrow keys for movement, Spacebar to shoot", 22, WIDTH / 2, HEIGHT / 2)
    draw_text(screen,"Press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
        

#Player Sprite
img = pygame.image.load("spaceship.png")

#Mob Sprite
img1 = pygame.image.load("asteroid.png")

#Bullet Sprite
img2 = pygame.image.load("laser.png")

#initialize pygame and create window
pygame.mixer.init()
background = pygame.image.load('background.png')
background_rect = background.get_rect()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids!")
clock = pygame.time.Clock()
pygame.mixer.music.load('gamesound.wav')
pygame.mixer.music.play(loops=0, start=0.0)

font_name = pygame.font.match_font('comic sans')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()        

        self.radius = 50

        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 300
        self.speedx = 0      
    

    def update(self):
        self.speedx = 0        
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -15
       
           
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
        self.radius = int(self.rect.width)
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
        self.image = img2
        self.rect = self.image.get_rect()        
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()



#Game loop
gameover = True
running = True
while running:
    if gameover:
        show_go_screen()
        gameover = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(50):
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)
        score = 0

    
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
        score += 50
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    if hits:
        running = False
##        #show_go_screen()
##        while running == False:
##                event.type == True
##                running = True
##                waiting = True
##                show_go_screen()
##                #waiting = True
        print("Game Over' your score is: ", score) 
        
    #Draw
    screen.fill(WHITE)   
    screen.blit(background,[0,0])
    screen.blit(background,background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10 )
    #After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
