#Import library Pygame
import pygame

#Initiating Pygame
pygame.init()

#Creating display surface
window_x = 1280 
window_y = 720
display_surface = pygame.display.set_mode((window_x, window_y)) #Imports the window

#Rename the display surface name
pygame.display.set_caption("Space Shooter")

#Creating a FPS (Frames per second)
clock = pygame.time.Clock()

#Starts running the game. Change the value to true, if else, close the display
running = True

#This variables helps the object to move each time this variable increase or decrease
x = 100

#Creating a surface in the display
surf = pygame.Surface((100, 200))
#Changing the color of the surface
surf.fill("red")

#Import images
player_surf = pygame.image.load("../player.png")

#Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #If false then out of the loop

    #Changing the color of the display
    display_surface.fill("darkgrey")

    #Here the surface go to x and y position. 
    display_surface.blit(player_surf, (x, 150))

    #Here is how we can make surfaces move
    x += 0.1

    #Update the window
    pygame.display.update()

    #Value of the game FPS (More fps, more quickly)
    clock.tick(60)

#This let the game close
pygame.quit()
