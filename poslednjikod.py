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
#\/ varijable za skakanje
dxc = 0
dyc = 0
dxp = 0
dyp = 0
#/\ varijable za skakanje
pbcx = xc #pomocne promenljive za pucanje da ne bi metak leteo kada neko skoci
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
cpp = cp3.get_rect()     #ovo je za collision koje sad probam
pyt = pyt4.get_rect()
cbeam = cbeam1.get_rect()
cbeam.left = 500
pbeam = pbeam1.get_rect()
pbeam.left = 800
                        #ovo je za collision koje sad probam
key = pygame.key.get_pressed() #za tastatu
dyyc = 0.5 # Brzina gravitacije 0.01
dyyp = 0.5 #

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
    #if cpp.collidedict(pbeam):######nije gotovo. Ovo je da li je pythonov metak pogodio cpp
        #bc+=1
    #print(pbeam.left)
    #if pygame.Rect(xp,yp, 166, 166).colliderect(pygame.Rect(bcx, pbcy, 116,71)):  #od 64 do 73 linije proverava da li je metak pogdio u cpp odnosno python
    #    pbcy = -300
    #    bp+=1            
    
    #if pygame.Rect(xc,yc, 166, 166).colliderect(pygame.Rect(bpx, pbpy, 116,71)):  #od 64 do 73 linije proverava da li je metak pogdio u cpp odnosno python
    #    pbpy = -300
    #    bc+=1            
        
    
    

    
    if key[pygame.K_LEFT] and xc>0:   #pomeranje cpp
        xc-=10
    if key[pygame.K_RIGHT] and xc<1280-150:
        xc+=10
    if key[pygame.K_UP]:             #skakanje
        dyc = -10 # Kolko visoko skace
    
    xc += dxc
    if yc+dyc<=720-165:
        yc += dyc
    dyc += dyyc
    
    if dyc > 3:  # Max brzina skakanja 0.8
        dyc = 3
    
    if key[pygame.K_a] and xp>0:    #pomeranje pythona
        xp-=4
    if key[pygame.K_d] and xp<1280-160:
        xp+=4
    if key[pygame.K_w]:
        dyp = -10
    xp += dxp
    if yp+dyp<=720-165:
        yp += dyp
    dyp+=dyyp
    if dyp > 3:
        dyp = 3
    # /\ sve ovo je skakanje pythona
    if key[pygame.K_m]:
        pbcy = yc
        shootingc = True
        bcx=xc
        bcy = yc
    
    #pucanje cpp
        screen.blit(cbeam1, (xc-30, pbcy+50))
    if shootingc == True:
        bcx-=5
        screen.blit(cbeam1, (bcx-30, pbcy+50))
    else:
        shootingc = False
    #pucanje cpp
    #\/ pucanje pythona
    if key[pygame.K_q]:
        pbpy = yp
        shootingp = True
        bpx=xp
        bpy = yp
        screen.blit(pbeam1, (xp+150, pbpy+50))
    if shootingc == True:
        bpx+=3
        screen.blit(pbeam1, (bpx+150, pbpy+50))
    else:
        shootingc = False
    #/\ pucanje pythona
    screen.blit(cp3, (xc, yc))#prikazianje
    screen.blit(pyt4, (xp, yp))
    pygame.display.update()
    print(bpy)
    pbcx = xc
    pbpx = xp
    for j in range(720):
        if bcx == xp and bcy == j:
            bc+=1
        else:
            continue
    for i in range(720):
        if bpx == xc and bpy == i:
            bp+=1
        else:
            continue
    if bp == 5:
        pygame.quit()
        exit()
    if bc == 5:
        pygame.quit()
        exit()
    
    clock.tick(60)  # limits FPS to 60
pygame.quit()
