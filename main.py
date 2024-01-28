from constants import *
import pygame
import car
import car2
import line
import line2

pygame.init()
states = 0

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

car_group = pygame.sprite.Group()
car2_group = pygame.sprite.Group()
line_group = pygame.sprite.Group()
line2_group = pygame.sprite.Group()





car = car.Car(32, 100)
car2 = car2.Car2(32, 100)




line = line.Line(10, 32, 150, 0)


line2 = line2.Line2(10, 32, 400, 0)



car_group.add(car)
car2_group.add(car2)

line_group.add(line)
line2_group.add(line2)


def main():
    global states
    running = True


    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    pygame.quit()

                if event.key == pygame.K_p:

                    if states == 1:
                        states = 2

                    elif states == 2:
                        states = 1


                if event.key == pygame.K_SPACE:
                    if states == 0:
                        states = 1


                if event.key == pygame.K_e:

                    if states == 1:
                        states = 4
                    elif states == 4:
                        states = 1











        draw()
        update()

    pygame.quit()




def draw():
    # global states


    if states == 0:
        menu()
        pass
    if states == 1:


        surface.fill((0, 0, 0))

        car_group.draw(surface)
        car2_group.draw(surface)
        line_group.draw(surface)
        line2_group.draw(surface)


    draw_scores()


    # pause
    if states == 2:
        pause()



    pygame.display.flip()


def update():
    global states
    # main menu
    if states == 0:
        menu()
    if states == 1:
        if car.hit:
            states = 3

        car_group.update(car2_group)
        car2_group.update()
        line_group.update()
        line2_group.update()


# death
if states == 3:
    surface.fill((255, 0, 0))
    
if states == 4:
    print(f"player's X: {car.x}")
    print(f"player's Y: {car.y}")
    print(f"car 2's X {car2.x}")
    print(f"car 2's Y {car2.y}")
    print(f"score:  {car2.points}")




def menu():
    surface.fill((0, 200, 0))



def pause():
    surface.fill((255, 255, 255))




def draw_scores():
    message_display(str(car2.points), GAME_WIDTH / 2 - FONT_SIZE, FONT_SIZE)



def text_objects(text, font):
    textSurface = font.render(text, True, (255, 0, 0))
    return textSurface, textSurface.get_rect()



def message_display(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf',FONT_SIZE)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    surface.blit(TextSurf, TextRect)





if __name__ == "__main__":
    main()
