import pygame
import random
import math

pygame.init()

# Screen dimensions
width, height = 400, 300
window_size = (width, height)
window_title = "Snake Game"
white = (255, 255, 255)
black = (0, 0, 0)
#create the game window
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)

#snake class to manage movement and growth
class Snake:
    def __init__(self,speed):
        self.body = [(width // 2-i * 20, height // 2) for i in range(4)]
        #[(200, 150), (180, 150), (160, 150), (140, 150)]
        self.direction = (20, 0)  # Moving right initially
        self.speed = speed
        

