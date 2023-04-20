# File created by JT Wilcox

    # import libs
import pygame
pygame.init()
# dimensions 
screen = pygame.display.set_mode((800, 600))
# used to track certain amount of time
clock = pygame.time.Clock()
# where the countdown should start from
counter, text = 7, '7'.rjust(3)
# 1000 milliseconds in a second
pygame.time.set_timer(pygame.USEREVENT, 1000)
# font sixe and shape
font = pygame.font.SysFont('arial', 100)
# loop starts
run = True
while run:
    # return list of all current events
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            # counter goes down 1 second 
            counter -= 1
            # if counter is less than 0 it prints "you lost"
            text = str(counter).rjust(3) if counter > 0 else 'you lost'
            # quit game
        if e.type == pygame.QUIT: 
            run = False
# colors and positioning of timer
    screen.fill((255, 255, 255))
    screen.blit(font.render(text, True, (0, 0, 0)), (330, 180))
    pygame.display.flip()
    # for every second, 60 frames will pass
    clock.tick(60)