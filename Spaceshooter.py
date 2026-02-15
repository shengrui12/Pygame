import pygame

pygame.init()
window_x = 1280
window_y = 720
display_surface = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Space Shooter")

running = True

x = 100
surf = pygame.Surface((100, 200))
surf.fill("red")

player_surf = pygame.image.load("../player.png")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill("darkgrey")
    
    display_surface.blit(player_surf, (x, 150))
    
    x += 0.1
    pygame.display.update()

pygame.quit()
