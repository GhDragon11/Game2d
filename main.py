import pygame
# ctrl+alt+l = corrigi os espaços que estão sobrando, no padrão profissional
print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('loop Start')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitting...')
            pygame.quit()  # Close Window
            quit()  # end pygame
