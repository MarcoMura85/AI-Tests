import pygame
import carClass
import collisionClass

# initialize the pygame module
pygame.init()
# load and set the logo
pygame.display.set_caption("Test Race")

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


# a clock for controlling the fps later
clock = pygame.time.Clock()

car = carClass.Car(100, 100, "car.png", screen)
car.showCar(screen)

def game_loop():
    xpos = screen_width/2
    ypos = screen_height/2
    car.setPos(xpos, ypos, 0)

    # update the screen to make the changes visible (fullscreen update)
    pygame.display.flip()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        screen.fill((128, 128, 128))

        p1 = (200, 200)
        p2 = (300, 500)
        pygame.draw.line(screen, (255, 0, 0), p1, p2)


        car.updatePosition(event)

        carVertices = car.getCarVertices()

        collision = collisionClass.intersect(carVertices[0],carVertices[3], p1, p2)

        print (collision)

        car.showCar(screen, collision)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
