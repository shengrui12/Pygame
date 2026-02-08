#Import Pygame
import pygame
import sys
pygame.init()

#Def pantalla
size = (800, 500)
screen = pygame.display.set_mode(size)

#Def FPS(Frames per second)
clock = pygame.time.Clock()

#Def RGB 
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

#Loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
  
  #Background color
  screen.fill(Black)

  #Drawing part -------------------------------------------------------------------------------

  
  #End drawing part ---------------------------------------------------------------------------

  #Refresh screen and add FPS
  pygame.display.flip()
  clock.tick(60) #<---60 is the FPS
