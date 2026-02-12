import pygame
pygame.init()
window_x = 1280
window_y = 720
display_surface = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Space Shooter")

running = True

surface = ((100, 200))
surface.fill("red")
x = 100

player = pygame.image.load("player.png")

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  display.surface.fill("darkgrey")
  display_surface.blit
  x += 0.1
  pygame.display.update(surface, (x, 150))

pygame.quit()
