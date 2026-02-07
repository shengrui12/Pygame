#IMPORTANT NOTES:

#In the screen the minimum x and y position is 0 and the maximum is the size variable for x is -large and for y is -width. *
#For example my size is (800, 500) and our square dimensions are 80, 80 
#The minimum x position is 0 and the maximum is 720 (800 - 80)
#The minimum y position is 0 and the maximum is 420 (500 - 80)
# *We need to know that this isn't neccessary if you want the object to dissapear in the limits.

#Import Pygame
import pygame
import sys
pygame.init()

#Def pantalla
size = (800, 500)
screen = pygame.display.set_mode(size)

#Object Position
cord_x = 400
cord_y = 200

#Movement x and y velocity
speed_x = 3
speed_y = 3

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

  #SCRIPT___Bounce___
  
  if (cord_x > 720 or cord_x < 0):
    speed_x *= -1
    #Inverts the x speed

  if (cord_y > 420 or cord_y < 0):
    speed_y *= -1
    #Inverts the y speed
  
  #Movement
  cord_x += speed_x 
  cord_y += speed_y
  
  #Background color
  screen.fill(Black)

  #Drawing part -------------------------------------------------------------------------------
  pygame.draw.rect(screen, Red, (cord_x, cord_y, 80, 80)) #<---Here is the 2 variables: Cord_x and Cord_y
  #Create rectangle: pygame.draw.rect(superficie, color, (x position, y position, large, width)
  
  #End drawing part ---------------------------------------------------------------------------

  #Refresh screen and add FPS
  pygame.display.flip()
  clock.tick(60) #<---Lo que va dentro del paréntesis son los FPS
