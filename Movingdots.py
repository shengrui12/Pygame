#Import Pygame
import pygame
import sys
import random
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

#List
coordinate_list = []
for value in range(60):
  x = random.randint(0, 800)
  y = random.randint(0, 500)
  coordinate_list.append([x, y])

#Loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
  
  #Background color
  screen.fill(Black)

  #Drawing part -------------------------------------------------------------------------------
  for coordinate in coordinate_list:
    x = coordinate[0]
    y = coordinate[1]
    pygame.draw.circle(screen, Red, (x, y), 2)
    #pygame.draw.circle(surface, color, (x, y), radius)
    coordinate[1] += 1
    if coordinate[1] > 500:
      coordinate[1] = 0

  #End drawing part ---------------------------------------------------------------------------

  #Refresh screen and add FPS
  pygame.display.flip()
  clock.tick(60) #<---60 is the FPS
