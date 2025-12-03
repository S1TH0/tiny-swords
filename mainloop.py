import pygame

# init pygame
pygame.init

# Set the display up
pygame.display.set_mode((196,196))
pygame.display.set_caption("Tiny Swords")

# Main game loop (menu?)
run = True
while run:
  for event in pygame.event.get():
    if event.type = pygame.QUIT:
      run = False



# when while loop ends, quits pygame
pygame.quit()
