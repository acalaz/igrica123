import pygame, sys
bc = 0
bp = 0
global yc
global yp
# pygame setup
xc = 1100
yc = 555
xp = 0
yp = 555
bcx = xc
bpx = xp
bcy = yc
bpy = yp
col = False
global shootingp
global shootingc
shootingc = False
shootingp = False
jumpc = False
jumpp = False
vel = 5
cddy = 2
acc = 1
dxc = 0
dyc = 0
pbcx = xc
pbcy = yc
pbpx = xp
pbpy = yp
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pyt3=pygame.image.load('pythonlog.png')
cp1=pygame.image.load('cpplog.png')
lbeam=pygame.image.load('laserbeam.png')
width =pyt3.get_rect().width
height = pyt3.get_rect().height
width1 =cp1.get_rect().width
height1 = cp1.get_rect().height
width2 =lbeam.get_rect().width
height3 = lbeam.get_rect().height
cp3 = pygame.transform.scale(cp1, (width1/3, height1/3))
pyt4 = pygame.transform.scale(pyt3, (width/2, height/2))
cbeam1 = pygame.transform.scale(lbeam, (width/5.5, height/5.5))
pbeam1 = pygame.transform.rotate(cbeam1, 180) 
cpp = cp3.get_rect
pyt = pyt4.get_rect
cbeam = cbeam1.get_rect
pbeam = pbeam1.get_rect
key = pygame.key.get_pressed()
dyyc = 0.5 # Brzina gravitacije 0.01
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    key = pygame.key.get_pressed()
    # RENDER YOUR GAME HERE
    if bcx == xp+200 and bcy == yp:
        bp+=1
    if bpx == xc-200 and bpy == yp:
        bc+=1
    if bp == 5:
        pygame.quit()
    if bc == 5:
        pygame.quit()

    
    if key[pygame.K_LEFT] and xc>0:
        xc-=10
    if key[pygame.K_RIGHT] and xc<1280-150:
        xc+=10
    if key[pygame.K_UP]:
        dyc = -10 # Kolko visoko skace
    
    xc += dxc
    if yc+dyc<720-166:
        yc += dyc
    dyc += dyyc
    
    if dyc > 3:  # Max brzina skakanja 0.8
        dyc = 3
    
    if key[pygame.K_a] and xp>0:
        xp-=4
    if key[pygame.K_d] and xp<1280-160:
        xp+=4
    
    if key[pygame.K_m]:
        pbcx = xc
        shootingc = True
        bcx=xc
        
        screen.blit(cbeam1, (bcx-30, yc+50))
    if shootingc == True:
        bcx-=5
        screen.blit(cbeam1, (bcx-30, yc+50))
    else:
        shootingc = False
    if key[pygame.K_q]:
        shootingp = True
        bpx=xp
        
        screen.blit(pbeam1, (bpx+150, yc+50))
    if shootingc == True:
        bpx+=3
        screen.blit(pbeam1, (bpx+150, yc+50))
    else:
        shootingc = False
    screen.blit(cp3, (xc, yc))
    screen.blit(pyt4, (xp, yp))
    pygame.display.update()

    pbcx = xc
    pbpx = xp
    clock.tick(60)  # limits FPS to 60
pygame.quit()
