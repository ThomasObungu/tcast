import pygame
import math

from map2D import *

PLAYER_FOV = math.pi/3
RAYS_CASTED = 240
RAY_DEPTH = MAP_SIZE * TILE_SIZE_X
MAP_SCALE = SCREEN_WIDTH / RAYS_CASTED

class player():
    def __init__(self, plr_x : float, plr_y : float, plr_angle : float):
        # Initiate player coords 
        self.plr_x = plr_x
        self.plr_y = plr_y
        self.plr_angle = plr_angle
        self.plr_movment = 1
    
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
            self.plr_movment = 1
            self.plr_x += math.cos(self.plr_angle)
            self.plr_y += math.sin(self.plr_angle)
        if keys[pygame.K_DOWN]:
            self.plr_movment = 0
            self.plr_x -= math.cos(self.plr_angle)
            self.plr_y -= math.sin(self.plr_angle)
        
    def cast_rays(self, surface, array):
        # Start at left most angle
        start_angle = self.plr_angle -  (PLAYER_FOV / 2)
        # Loop over amount of rays to be cast
        for ray in range(int(RAYS_CASTED)):
            # Loop over each step, very ineffcient
            for step in range(int(RAY_DEPTH/2)):
                ray_x = self.plr_x + math.cos(start_angle) * step
                ray_y = self.plr_y + math.sin(start_angle) * step

                # Enumerate player coordintes
                col = int(ray_x / TILE_SIZE_X)
                row = int(ray_y / TILE_SIZE_Y)

                player_col = int(self.plr_x / TILE_SIZE_X)
                player_row = int(self.plr_y / TILE_SIZE_Y)

                # Player wall collision
                if array[player_row][player_col]==1:
                    if self.plr_movment:
                        self.plr_x -= math.cos(self.plr_angle) 
                        self.plr_y -= math.sin(self.plr_angle)
                    elif self.plr_movment == 0:
                        self.plr_x += math.cos(self.plr_angle)
                        self.plr_y += math.sin(self.plr_angle)
                    break
                
                # If step coordinate is enumerated to a wall index, then stop incrementing steps
                if array[row][col] == 1:
                    break
                
                # pygame.draw.line(surface, (255,0,255), (self.plr_x, self.plr_y), 
                #                  (ray_x, ray_y))

            # Implementing shading
            colour = 220 / (1 + step* step * 0.0001)
            # Remove fish effect by mutliplying the x offset by cosine player angle
            step *= math.cos(self.plr_angle - start_angle)
            # Height is calculated by a large constant by the distance from the wall
            wall_height = 21000 / (step + 0.0001)
            

            # Comment this code below
            
            #Print the actual walls, rectangle by rectangle.
            pygame.draw.rect(surface, (colour,colour,colour), (0 + ray * MAP_SCALE, 
                            (SCREEN_HEIGHT / 2) - wall_height / 2, 
                            MAP_SCALE, wall_height )) 
            
            # Comment this code above to enable 2D map 
            
            start_angle += PLAYER_FOV / RAYS_CASTED