#https://youtu.be/Ak_BYhV_pI0
#need to fix the death message
#add replay button
#fix the randomness of the platforms
import pygame,os,random,sys,time

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 400, 600

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Doodle Jump")
clock = pygame.time.Clock()

pygame.font.init()
SCORE_FONT = pygame.font.SysFont("comicsans", 35)
LOST_FONT = pygame.font.SysFont("comicsans", 70)
LAST_SCORE_FONT = pygame.font.SysFont("comicsans", 50)
#LOAD IMAGES
      
BG = pygame.image.load(os.path.join('assets', 'bg.png'))
BG = pygame.transform.scale(BG, (493, 773))

platimg = pygame.image.load(os.path.join('assets', 'platform1.png'))

doodleimg = pygame.image.load(os.path.join('assets', 'doodle.png')).convert_alpha()
doodleimg = pygame.transform.scale(doodleimg, (101, 79))

FPS = 60
x = 100
y = 100
dy = 0.0
h = 200
score = 0
count = 0

class Platforms:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #self.width_platform = platimg.get_width()
        #self.height_platform = platimg.get_height()

def lost_text(score):
    lost = LOST_FONT.render("YOU LOST!", 1, (255,0,0))
    last_score = LAST_SCORE_FONT.render("Score: " + str(score), 1, (0, 0, 255))         
    WINDOW.blit(lost, (WIDTH/2 - lost.get_width()/2, HEIGHT/2))
    WINDOW.blit(last_score, (WIDTH/2 - last_score.get_width()/2, HEIGHT/2 + 45))   

plates = [Platforms(random.randrange(0, WIDTH - 50), random.randrange(0, HEIGHT)) for i in range(15)]
while True:
    clock.tick(FPS)
    player_feet_x, player_feet_y = doodleimg.get_width()/2, doodleimg.get_height()
    WINDOW.blit(BG, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    for plat in plates:
        WINDOW.blit(platimg, (plat.x, plat.y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= 4
        doodleimg = pygame.transform.flip(pygame.image.load(os.path.join('assets','doodle.png')), True, False)
        doodleimg = pygame.transform.scale(doodleimg, (101, 79))
        
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x +=4
        doodleimg = pygame.image.load(os.path.join('assets','doodle.png'))
        doodleimg = pygame.transform.scale(doodleimg, (101, 79))
    
    if y < h:
        y = h
        for plat in plates:
            plat.y = plat.y - dy
            if plat.y > HEIGHT:
                plat.y = -50
                plat.x = random.randrange(0, WIDTH - 50)
                score += 1
                
    
    dy += 0.3
    y += dy
    if y > HEIGHT: 
        while count <= FPS * 100:
            WINDOW.blit(BG, (0,0))   
            lost_text(score)
            count += 1
        score = 0
        pygame.quit()
        sys.exit()
    
    for plat in plates:
        if (x + 50 > plat.x) and (x + 20 < plat.x + 68) and (y + 70 > plat.y) and (y + 70 < plat.y + 14) and dy > 0: #for staying on the platform, needs a more reliable if statement
            dy = -10

    if x <= 0 :
        x = WIDTH - 5
    elif x >= WIDTH:
        x = 0

    text = SCORE_FONT.render("Score: " + str(score), 1, (0,0,0))
    WINDOW.blit(text,(WIDTH - 10 - text.get_width(), 10))

    WINDOW.blit(doodleimg, (x,y))

    pygame.display.update()
