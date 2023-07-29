# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pyt=pygame.image.load('pythonl.png')
cp1=pygame.image.load('cpplogo.png')
width =pyt.get_rect().width
height = pyt.get_rect().height
width1 =cp1.get_rect().width
height1 = cp1.get_rect().height
cpp = pygame.transform.scale(cp1, (width1/5, height1/5))
pyt1 = pygame.transform.scale(pyt, (width/2, height/2))
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    screen.blit(pyt1, (0, 550))
    screen.blit(cpp, (1100, 550))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
print(width)
print(height)
print(width1)
print(height1)