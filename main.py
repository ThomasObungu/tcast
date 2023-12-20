import pygame
import sys
from map2D import *
                
class player:
    def __init__(self, plr_x, plr_y):
        pass
                 
def main():
    # Initiate 2D_Array width and Height
    game_map = map2D(16,16)
    map_array_2D = game_map.generate_array()
    
    # Neatly print out array
    for i in map_array_2D:
        print(i)
    
    #Intialize screen and size
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((720,480))

    # Show map on screen
    show_map = True

    # Main game loop
    while True:
        if show_map:
            game_map.draw_map(map_array_2D,screen)
    
        # Apply application exit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
        
        #Draw 2D map
        # Update screen display
        pygame.display.update() 
        # Set fps to 60
        clock.tick(60)
        # Set windows name to fps
        pygame.display.set_caption(str(clock)[7:15])
        
if __name__ == "__main__":
    main()



