import pygame


# initialize the pygame module
pygame.init()
# load and set the logo

pygame.display.set_caption("Test Race")

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# a clock for controlling the fps later
clock = pygame.time.Clock()

image = pygame.image.load("01_image.png")

image.set_colorkey((255, 0, 255))

bgd_image = pygame.image.load("background.png")

# blit image(s) to screen
screen.blit(bgd_image, (0, 0))  # first background

# define the position of the smily
xpos = 50
ypos = 50
# how many pixels we move our smily each frame
step_x = 10
step_y = 10

# and blit it on screen
screen.blit(image, (xpos, ypos))

# update the screen to make the changes visible (fullscreen update)
pygame.display.flip()

# define a variable to control the main loop
running = True

# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False
        # check for keypress and check if it was Esc
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # check if the smily is still on screen, if not change direction
    if xpos > screen_width - 64 or xpos < 0:
        step_x = -step_x
    if ypos > screen_height - 64 or ypos < 0:
        step_y = -step_y
    # update the position of the smily
    xpos += step_x  # move it to the right
    ypos += step_y  # move it down

    screen.blit(bgd_image, (0, 0))
    # now blit the smily on screen
    screen.blit(image, (xpos, ypos))
    # and update the screen (dont forget that!)
    pygame.display.update()

    # this will slow it down to xx fps, so you can watch it,
    # otherwise it would run too fast
    clock.tick(60)
pygame.quit()
