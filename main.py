import pygame
import sys
import math

from map2D import *
from player import *

PLAYER_FOV = math.pi/3
RAYS_CASTED = 144
RAY_DEPTH = MAP_SIZE * TILE_SIZE_X
MAP_SCALE = SCREEN_WIDTH / RAYS_CASTED
CHANGE = True
        
def main():
    # Initiate 2D_Array width and Height
    game_map_2D = map2D(MAP_SIZE,MAP_SIZE)
    map_array_2D = game_map_2D.generate_array()
    
    # Neatly print out array
    for i in map_array_2D:
        print(i)
    
    #Intialize screen and size
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((720,480))

    # Show map on screen
    show_map_2D = True

    # Initiate starting player coordinates
    plr_x = game_map_2D.find_empty_space(map_array_2D)[1] * TILE_SIZE_X + TILE_SIZE_X / 2
    plr_y = game_map_2D.find_empty_space(map_array_2D)[0] * TILE_SIZE_Y + TILE_SIZE_Y / 2

    # Initiate player angle 
    plr_angle = math.pi/2

    # Initiate player on 2D map
    game_player = player(plr_x,plr_y,plr_angle)

    # Main game loop
    while True:
        if show_map_2D:
            # Draw 2D map
            game_map_2D.draw_map(map_array_2D,screen)  
            # Draw Player
            game_player.draw_player(screen)
        # Handle user input
        game_player.user_input()
        # Draw 3D background
        pygame.draw.rect(screen, (50,50,50), (0,SCREEN_HEIGHT/2, 
                                SCREEN_WIDTH, SCREEN_HEIGHT/2))
        pygame.draw.rect(screen, (255,255,255), (0,0, 
                                SCREEN_WIDTH, SCREEN_HEIGHT/2))
        # Cast rays
        game_player.cast_rays(screen,map_array_2D)

        # Apply application exit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()

        # Update screen display
        pygame.display.update() 
        # Set fps to 60
        clock.tick(60)
        # Set windows name to fps
        pygame.display.set_caption(str(clock)[7:15])
        
if __name__ == "__main__":
    main()



