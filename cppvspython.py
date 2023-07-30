# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
xc=1100
yc=560
xp=0
yp=560
bcx=xc
bpx=xp
col=False
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pyt=pygame.image.load('pythonlog.png')
cp1=pygame.image.load('cpplog.png')
lbeam=pygame.image.load('laserbeam.png')
width =pyt.get_rect().width
height = pyt.get_rect().height
width1 =cp1.get_rect().width
height1 = cp1.get_rect().height
width2 =lbeam.get_rect().width
height3 = lbeam.get_rect().height
cpp = pygame.transform.scale(cp1, (width1/3, height1/3))
pyt1 = pygame.transform.scale(pyt, (width/2, height/2))
beam = pygame.transform.scale(lbeam, (width/5.5, height/5.5))
pbeam = pygame.transform.rotate(beam, 180) 
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and xc>0:
        xc-=4
        bcx=xc
    if key[pygame.K_RIGHT] and xc<1280-150:
        xc+=4
        bcx=xc
    if key[pygame.K_a] and xp>0:
        xp-=4
        bpx=xp
    if key[pygame.K_d] and xp<1280-160:
        xp+=4
        bpx=xp
    if key[pygame.K_m]:
        screen.blit(beam, (bcx-30, yc+50))
    if key[pygame.K_q]:
        screen.blit(pbeam, (bpx+150, yc+50))
    screen.blit(cpp, (xc, yc))
    screen.blit(pyt1, (xp, yp))
    # flip() the display to put your work on screen
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()