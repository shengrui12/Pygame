import pygame
pygame.init()
window_x = 1280
window_y = 720
display_surface = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Space Shooter")

running = True

surface = ((100, 200))
surface.fill("red")

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  display.surface.fill("darkgrey")
  display_surface.blit
  pygame.display.update(surface, (100, 150))

pygame.quit()
