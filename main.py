#!/usr/bin/env python2
import pygame
from pygame.locals import *
from sshConnectionToVechicle import SshConnection as Vehicle


class Keys:
        UP          = 0b00000001
        DOWN        = 0b00000010
        LEFT        = 0b00000100
        RIGHT       = 0b00001000
        BRAKE       = 0b00010000
        QUIT        = 0b00100000
        SPEED_UP    = 0b01000000
        SPEED_DOWN  = 0b10000000





def texts(text, screen):
   font = pygame.font.Font(None,30)
   scoretext = font.render(str(text), 0,(255,255,255))
   screen.blit(scoretext, (10, 10))



def run():

    # 2 - Initialize the "game"
    pygame.init()
    width, height = 300, 200
    screen = pygame.display.set_mode((width, height))

    keysStatus = 0 # tells us which keys are being pressed. It is a number resulting from adding the values from Keys class
    newStatus = 0

    # connect the vehicle
    vehicle = Vehicle("192.168.0.104") # this is the address of the beaglebone robot

    # 4 - keep looping through
    while 1:
        # # 5 - clear the screen before drawing it again
        screen.fill(0)


        # Send new commands to vehicle
        if newStatus != keysStatus:
            keysStatus = newStatus
            vehicle.sendKeysStatus(str(keysStatus)+"\n")
            print"event"

        texts("{0:b}".format(keysStatus), screen)

        # # 7 - update the screen
        pygame.display.flip()

        # # 8 - loop through the events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==K_UP:
                    newStatus = newStatus | Keys.UP
                elif event.key==K_DOWN:
                    newStatus = newStatus | Keys.DOWN
                elif event.key==K_LEFT:
                    newStatus = newStatus | Keys.LEFT
                elif event.key==K_RIGHT:
                    newStatus = newStatus | Keys.RIGHT
                elif event.key==K_SPACE:
                    newStatus = newStatus | Keys.BRAKE
                elif event.key== K_ESCAPE:
                    newStatus = newStatus | Keys.QUIT
                elif event.key== K_a:
                    newStatus = newStatus | Keys.SPEED_UP
                elif event.key== K_z:
                    newStatus = newStatus | Keys.SPEED_DOWN

            elif event.type == pygame.KEYUP:
                if event.key==K_UP:
                    newStatus = newStatus & ~Keys.UP
                elif event.key==K_DOWN:
                    newStatus = newStatus & ~Keys.DOWN
                elif event.key==K_LEFT:
                    newStatus = newStatus & ~Keys.LEFT
                elif event.key==K_RIGHT:
                    newStatus = newStatus & ~Keys.RIGHT
                elif event.key==K_SPACE:
                    newStatus = newStatus & ~ Keys.BRAKE
                elif event.key== K_ESCAPE:
                    newStatus = newStatus & ~Keys.QUIT
                elif event.key== K_a:
                    newStatus = newStatus & ~Keys.SPEED_UP
                elif event.key== K_z:
                    newStatus = newStatus & ~Keys.SPEED_DOWN
                if event.key == K_ESCAPE:
                    vehicle.sendKeysStatus(str(keysStatus)+"\n")
                    return




if __name__ == "__main__":
    run()




