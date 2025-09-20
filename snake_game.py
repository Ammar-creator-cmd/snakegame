from time import time
import pygame
import random
import math

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 300
window_size = (WIDTH, HEIGHT)
window_title = "Snake Game"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#create the game window
window = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)

#snake class to manage movement and growth
class Snake:
    def __init__(self, speed):
        # Start moving right, body laid out to the left
        self.direction = (1, 0)  # dx=1, dy=0 (right)
        head_x = WIDTH // 2
        head_y = HEIGHT // 2
        self.body = [(head_x - i * 20, head_y) for i in range(4)]
        self.speed = speed
    
    def move(self):
        dx, dy = self.direction
        new_head = ((self.body[0][0] + dx * 20) % WIDTH, (self.body[0][1] + dy * 20) % HEIGHT)
        self.body.pop()  # Remove tail
        self.body.insert(0, new_head)  # Add new head

    def grow(self):
        dx, dy = self.direction
        new_tail = ((self.body[-1][0] - dx * 20) % WIDTH, (self.body[-1][1] - dy * 20) % HEIGHT)
        self.body.append(new_tail)
        
    def change_direction(self, dx, dy):
        if (dx, dy) != (-self.direction[0], -self.direction[1]):  # Prevent reversing
            self.direction = (dx, dy)

    def get_head(self):
        return self.body[0]
    
    def get_body(self):
        return self.body[1:]
    
    def set_speed(self, speed):
        self.speed = speed

#food class to manage food position
class Food:
    def __init__(self):
        self.position = (random.randint(10, WIDTH - 10), random.randint(10, HEIGHT - 10))

    def respawn(self):
        self.position = (random.randint(10, WIDTH - 10), random.randint(10, HEIGHT - 10))

    def get_position(self):
        return self.position

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

#show intro screen
def show_intro_screen():
    font_large = pygame.font.Font(None, 50)
    font_small = pygame.font.Font(None, 30)
    
    # Colors for button states
    BUTTON_COLOR = (200, 200, 200)
    BUTTON_HOVER_COLOR = (180, 180, 180)
    
    game_name = font_large.render("Snake Game", True, BLACK)
    slow_button = font_small.render("SLOW", True, BLACK)
    normal_button = font_small.render("NORMAL", True, BLACK)
    fast_button = font_small.render("FAST", True, BLACK)
    
    # Button dimensions and positions
    button_width = 150
    button_height = 40
    button_margin = 20
    
    # Calculate button positions
    start_y = HEIGHT // 2 - 30
    slow_rect = pygame.Rect(WIDTH//2 - button_width//2, start_y, button_width, button_height)
    normal_rect = pygame.Rect(WIDTH//2 - button_width//2, start_y + button_height + button_margin, button_width, button_height)
    fast_rect = pygame.Rect(WIDTH//2 - button_width//2, start_y + 2 * (button_height + button_margin), button_width, button_height)
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if slow_rect.collidepoint(mouse_pos):
                    return "slow"
                elif normal_rect.collidepoint(mouse_pos):
                    return "normal"
                elif fast_rect.collidepoint(mouse_pos):
                    return "fast"
        
        window.fill(WHITE)
        
        # Draw game name
        window.blit(game_name, (WIDTH // 2 - game_name.get_width() // 2, HEIGHT // 4 - game_name.get_height() // 2))
        
        # Draw buttons with hover effect
        for button, text in [(slow_rect, slow_button), (normal_rect, normal_button), (fast_rect, fast_button)]:
            color = BUTTON_HOVER_COLOR if button.collidepoint(mouse_pos) else BUTTON_COLOR
            pygame.draw.rect(window, color, button)
            pygame.draw.rect(window, BLACK, button, 2)  # Button border
            window.blit(text, (button.centerx - text.get_width() // 2, button.centery - text.get_height() // 2))
        
        pygame.display.update()

def main():
    speed_level = show_intro_screen()


    if speed_level == "slow":
        snake_speed = 5
    elif speed_level == "normal":
        snake_speed = 10
    else:
        snake_speed = 15


    snake = Snake(snake_speed)
    food = Food()


    score = 0  # Initialize the score to zero
    clock = pygame.time.Clock()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(0, -1)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(0, 1)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(1, 0)
        snake.move()


        head = snake.get_head()
        if distance(head, food.get_position()) < 20:
            snake.grow()
            food.respawn()
            score += 1


        #cek kalo snake nyetuh diri sendiri
        if head in snake.get_body():
            #draw gameOver
            font = pygame.font.Font(None, 50)
            text = font.render("Game Over", True, BLACK)
            window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
            pygame.display.update()
            # Wait for 2 seconds while processing events
            game_over_time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - game_over_time < 2000:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
            pygame.quit()
            return


        window.fill(WHITE)


        #draw snake's body as black rectangles
        for segment in snake.body:
            pygame.draw.rect(window, BLACK, (segment[0], segment[1], 20, 20))


        RED = (255, 0, 0)
        #draw food as a red circle
        pygame.draw.circle(window, RED, food.get_position(), 10)


        #draw score
        font = pygame.font.Font(None, 30)
        text = font.render("Score: " + str(score), True, BLACK)
        window.blit(text, (10, 10))


        pygame.display.update()
        clock.tick(snake_speed)




if __name__ == "__main__":
    main()