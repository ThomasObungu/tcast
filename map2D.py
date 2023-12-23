import random
import pygame

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
MAP_SIZE = 16
TILE_SIZE_X = SCREEN_WIDTH / MAP_SIZE
TILE_SIZE_Y = SCREEN_HEIGHT / MAP_SIZE

class map2D:
    def __init__(self, map_width : int, map_height : int):
        # Initalize 2D array width and array height
        self.map_height = map_height
        self.map_width = map_width
    
    def generate_array(self):
        # Fill map with empty arrays
        array = [[] for i in range(self.map_height)]
        for i in range(self.map_width):
            # Fills arrays in array with 0's
            array[i] = [0 for i in range(self.map_width)]          
        # Itrate through the rows
        for i in range(1,len(array)-1):
        # Loop through each array and randomly fill tiles with 1's or 0's
            array[i]=[random.randint(0,1)
                                    for j in range(0,len(array[i]))]
        # Set first and last arrays to be filled with 1's only to create map boundaries
        array[0] = [1 for i in range(self.map_width)]
        array[-1] = [1 for i in range(self.map_width)]
        # Set first and last element of arrays in array to 1 to make side walls
        for i in range(self.map_width):
            array[i][0] = 1
            array[i][-1] = 1 
        # Return array
        return array
    
    def draw_map(self,array,game_surface):
        # Draw background to overule any printing
        pygame.draw.rect(game_surface,(0,0,0),(0,0,SCREEN_WIDTH,SCREEN_HEIGHT))
        # Iterate through rows
        for row in range(len(array)):
            # Iterate through columns
            for column in range(len(array[row])):
                # Draw each square with coords based on array position/ Col is x coords, row is y coords
                pygame.draw.rect(game_surface, (220,220,220) if array[row][column] == 1 else (50,50,50), 
                                 (column * TILE_SIZE_X, row * TILE_SIZE_Y,
                                  TILE_SIZE_X-1,TILE_SIZE_Y-1))
    
    def find_empty_space(self, array):
        # Iterate through the rows
        for row in range(len(array)):
            # Iterate through the rows
            for col in range(len(array[row])):
                # Once found a 0 which is an empty space, loop breaks and returns indexes
                if array[row][col] == 0:
                    return[row,col]
                