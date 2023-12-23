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
        
class player():
    def __init__(self, plr_x : float, plr_y : float, plr_angle : float):
        # Initiate player coords 
        self.plr_x = plr_x
        self.plr_y = plr_y
        self.plr_angle = plr_angle
    
    def draw_player(self, surface):
        # Draw player on 2D Map
        pygame.draw.circle(surface, (0,150,250), (self.plr_x,self.plr_y), 8)
        # Draw player direction line based on angle. sin(0) is y coords, cos(0) is x coords
        pygame.draw.line(surface, (255,0,0),(self.plr_x, self.plr_y),
                         (self.plr_x + math.cos(self.plr_angle) * 20, 
                          self.plr_y + math.sin(self.plr_angle) * 20), 3)
        # Draw left most player direction line
        pygame.draw.line(surface, (255,0,0),(self.plr_x, self.plr_y),
                         (self.plr_x + math.cos(self.plr_angle - PLAYER_FOV / 2) * 20, 
                          self.plr_y + math.sin(self.plr_angle - PLAYER_FOV / 2) * 20), 3)
        # Draw right most player direction line
        pygame.draw.line(surface, (255,0,0),(self.plr_x, self.plr_y),
                         (self.plr_x + math.cos(self.plr_angle + PLAYER_FOV / 2) * 20, 
                          self.plr_y + math.sin(self.plr_angle + PLAYER_FOV / 2) * 20), 3)
    
    def user_input(self):
        # Change player angle based on key press
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: self.plr_angle += 0.05
        if keys[pygame.K_LEFT]: self.plr_angle -= 0.05
        # Move forward or backwards based on player direction
        if keys[pygame.K_UP]: 
            self.plr_x += math.cos(self.plr_angle)
            self.plr_y += math.sin(self.plr_angle)
        if keys[pygame.K_DOWN]:
            self.plr_x -= math.cos(self.plr_angle)
            self.plr_y -= math.sin(self.plr_angle)
        
    def cast_rays(self, surface, array):
        # Start at left most angle
        start_angle = self.plr_angle -  (PLAYER_FOV / 2)
        # Loop over amount of rays to be cast
        for ray in range(int(RAYS_CASTED)):
            # Loop over each step, very ineffcient
            for step in range(int(RAY_DEPTH)):
                ray_x = self.plr_x + math.cos(start_angle) * step
                ray_y = self.plr_y + math.sin(start_angle) * step

                col = int(ray_x / TILE_SIZE_X)
                row = int(ray_y / TILE_SIZE_Y)

                if array[row][col] == 1:
                    break
                
                #pygame.draw.line(surface, (255,0,255), (self.plr_x, self.plr_y), 
                                 #(ray_x, ray_y))

            wall_height = 21000 / (step + 0.0001)

            pygame.draw.rect(surface, (220,220,220), (0 + ray * MAP_SCALE, 
                            (SCREEN_HEIGHT / 2) - wall_height / 2, 
                            MAP_SCALE, wall_height )) 
            
            start_angle += PLAYER_FOV / RAYS_CASTED

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



