import pygame
import carClass


# initialize the pygame module
pygame.init()
# load and set the logo
pygame.display.set_caption("Test Race")

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# a clock for controlling the fps later
clock = pygame.time.Clock()

car_img = pygame.image.load("01_image.png")

car_img_size = car_img.get_rect().size

car_img.set_colorkey((255, 0, 255))

def displayCar (x,y):
    screen.blit(car_img, (x, y))


car2 = carClass.Car(100,100,"01_image.png")
car2.showCar(screen)

def game_loop():
    # define the position of the smily
    xpos = screen_width/2
    ypos = screen_height/2
    # how many pixels we move our smily each frame
    step_x = 10
    step_y = 10

    # and blit it on screen
    displayCar(xpos, ypos)

    # update the screen to make the changes visible (fullscreen update)
    pygame.display.flip()

    # define a variable to control the main loop
    running = True
    left = False
    right = False
    up = False
    down = False

    # main loop
    while running:

        delta_x = 0

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left = True
                if event.key == pygame.K_RIGHT:
                    right = True
                if event.key == pygame.K_UP:
                    up = True
                if event.key == pygame.K_DOWN:
                    down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = False
                if event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_UP:
                    up = False
                if event.key == pygame.K_DOWN:
                    down = False

        # update the position of the smily
        if left: xpos -= step_x
        if right: xpos += step_x
        if up: ypos -= step_y
        if down: ypos += step_y

        if xpos > screen_width - car_img_size[0]:
            right = False
            xpos = screen_width - car_img_size[0]
        if xpos < 0:
            left = False
            xpos = 0

        if ypos > screen_height - car_img_size[1]:
            down = False
            ypos = screen_height - car_img_size[1]
        if ypos < 0:
            up = False
            ypos = 0


        screen.fill((128, 128, 128))
        # now blit the smily on screen
        displayCar(xpos, ypos)
        car2.showCar(screen)

        # and update the screen (dont forget that!)
        pygame.display.flip()
        clock.tick(60)

game_loop()
pygame.quit()
