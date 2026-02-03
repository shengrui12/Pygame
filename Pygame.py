import pygame
import sys
pygame.init()

Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

size = (800, 500)

screen = pygame.display.set_mode(size)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  screen.file(Black)


  pygame.display.flip()
