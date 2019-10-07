import pygame
import carClass
import collisionClass
import distanceSensors
import rewardGates

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
point_list = []
outer = []
inner = []

def draw_circuit( point_list, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if not pygame.mouse.get_pos() in point_list:
            point_list.append(pygame.mouse.get_pos())


def game_loop():
    xpos = screen_width/2
    ypos = screen_height/2
    car.setPos(xpos-345, ypos, 0)

    # update the screen to make the changes visible (fullscreen update)
    pygame.display.flip()

    # define a variable to control the main loop
    running = True

    with open("outerCircuit.txt", "r") as f:
       for line in f:
            outer =[tuple(map(int, i.split(','))) for i in f]
    with open("innerCircuit.txt", "r") as f:
        for line in f:
            inner = [tuple(map(int, i.split(','))) for i in f]

    circuit = inner + outer

    # gatesDict = {}
    # for pointOut in range(len(outer)):
    #     distPrev = float('inf')
    #     for pointIn in range(len(inner)):
    #         dist = distanceSensors.distance(inner[pointIn], outer[pointOut])
    #         if dist < distPrev:
    #             distPrev = dist
    #             gatesDict[pointOut] = pointIn
    #
    # d2 = {v: k for k, v in gatesDict.items()}  # exchange keys, values
    # gatesDict = {v: k for k, v in d2.items()}

    circuitGates = rewardGates.RewardGates(13, car.rect, screen)
    circuitGates.loadRewardGates(inner, outer)

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            #if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            #    with open("innerCircuit.txt", "w") as f:
            #        f.write('\n'.join('%s , %s' % x for x in point_list))

        screen.fill((128, 128, 128))

        pygame.draw.polygon(screen, (200, 200, 200), outer, 0)
        pygame.draw.polygon(screen, (128, 128, 128), inner, 0)

       # draw_circuit(point_list, event)

        #if len(point_list) > 1:
            #pygame.draw.lines(screen, (255, 0, 0), False, point_list, 1)

        #car.updatePositionOnKeyboardEvent(event)
        car.updatePositionByAgent();

        carVertices = car.getCarVertices()

        collision = collisionClass.doPolygonIntersect(carVertices, inner) or collisionClass.doPolygonIntersect(carVertices, outer)
        circuitGates.checkGatePass(carVertices)


        car.move()

        #car.myRect.drawMyRect(collision)
        #car.sensors.drawSensors()
        circuitGates.drawGates(True)

        points, dist = car.sensors.calcInterseptionCircuit(inner, outer)
        car.sensors.drawInterceptionPoint(points)
        #car.sensors.drawInterceptionPoint(outer)

        car.showCar(screen)

        pygame.display.update()
        clock.tick(60)

        if collision:
            car.myRect.drawMyRect(collision)
            pygame.display.update()
            running = False

game_loop()
pygame.quit()
