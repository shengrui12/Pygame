import pygame
import sys
pygame.init()

#Def RGB 
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

  screen.fill(Black)

  #SALA DE DIBUJO

  pygame.draw.rect(screen, Red, (400, 200, 80, 80))
  #pygame.draw.rect(surface, color, rect)
  #pygame.draw.rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)
  

  #TERMINAR SALA DE DIBUJO

  pygame.display.flip()
