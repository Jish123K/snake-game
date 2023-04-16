import pygame

import random

# Set up the game board

WIDTH = 600

HEIGHT = 400

ROWS = 20

COLS = 20

# Create the snake

class Snake:

    def __init__(self, x, y):

        self.body = [(x, y)]

        self.direction = "up"

    def move(self):

        if self.direction == "up":

            self.body.append((self.body[-1][0], self.body[-1][1] - 1))

        elif self.direction == "down":

            self.body.append((self.body[-1][0], self.body[-1][1] + 1))

        elif self.direction == "left":

            self.body.append((self.body[-1][0] - 1, self.body[-1][1]))

        elif self.direction == "right":

            self.body.append((self.body[-1][0] + 1, self.body[-1][1]))

        self.body.pop(0)

    def grow(self):

        self.body.append(self.body[-1])

# Add food

class Food:

    def __init__(self, x, y):

        self.x = x

        self.y = y

# Initialize the game

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

# Create the snake and food

snake = Snake(0, 0)

food = Food(random.randint(0, ROWS - 1), random.randint(0, COLS - 1))
# Main game loop

while True:

    # Check for events

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            break

        # Move the snake

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:

                if snake.direction != "down":

                    snake.direction = "up"

            elif event.key == pygame.K_DOWN:

                if snake.direction != "up":

                    snake.direction = "down"

            elif event.key == pygame.K_LEFT:

                if snake.direction != "right":

                    snake.direction = "left"

            elif event.key == pygame.K_RIGHT:

                if snake.direction != "left":

                    snake.direction = "right"

    # Check for collisions

    if snake.body[0][0] == 0 or snake.body[0][0] == COLS - 1 or snake.body[0][1] == 0 or snake.body[0][1] == ROWS - 1:

        game_over()

    for i in range(1, len(snake.body)):

        if snake.body[0] == snake.body[i]:

            game_over()

    # Check if the snake ate the food

    if snake.body[0] == (food.x, food.y):

        snake.grow()

        food.x = random.randint(0, ROWS - 1)

        food.y = random.randint(0, COLS - 1)

    # Move the snake

    snake.move()

    # Draw the game board

    screen.fill((0, 0, 0))

    for i in range(ROWS):

        for j in range(COLS):

            if (i, j) in snake.body:

                pygame.draw.rect(screen, (255, 0, 0), (j * 30, i * 30, 30, 30))

            else:
              pygame.draw.rect(screen, (0, 0, 255), (j * 30, i * 30, 30, 30))

    pygame.draw.rect(screen, (255, 0, 0), (food
                                           # Update the display

    pygame.display.update()

    clock.tick(30)

# Game over function

def game_over():

    pygame.quit()

    exit()
           # Add levels

def add_level():

    # Increase the speed of the snake

    clock.tick(clock.get_ticks() + 10)

    # Add more food to the game board

    for i in range(3):

        food = Food(random.randint(0, ROWS - 1), random.randint(0, COLS - 1))

        while food in snake.body:

            food = Food(random.randint(0, ROWS - 1), random.randint(0, COLS - 1))
                                        # Main function

def main():

    # Initialize the game

    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()

    # Create the snake and food

    snake = Snake(0, 0)

    food = Food(random.randint(0, ROWS - 1), random.randint(0, COLS - 1))

    # Main game loop

    level = 1

    while True:

        # Check for events

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                break

            # Move the snake

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:

                    if snake.direction != "down":

                        snake.direction = "up"

                elif event.key == pygame.K_DOWN:

                    if snake.direction != "up":

                        snake.direction = "down"

                elif event.key == pygame.K_LEFT:

                    if snake.direction != "right":

                        snake.direction = "left"

                elif event.key == pygame.K_RIGHT:

                    if snake.direction != "left":

                        snake.direction = "right"

        # Check for collisions

        if snake.body[0][0] == 0 or snake.body[0][0] == COLS - 1 or snake.body[0][1] == 0 or snake.body[0][1] == ROWS - 1:

            game_over()

        for i in range(1, len(snake.body)):

            if snake.body[0] == snake.body[i]:

                game_over()

        # Check if the snake ate the food

        if snake.body[0] == (food.x, food.y):

            snake.grow()   
                                          food.x = random.randint(0, ROWS - 1)
            food.y = random.randint(0, COLS - 1)
            add_level()

        # Move the snake
        snake.move()

        # Draw the game board
        screen.fill((0, 0, 0))
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in snake.body:
                    pygame.draw.rect(screen, (255, 0, 0), (j * 30, i * 30, 30, 30))
                else:
                    pygame.draw.rect(screen, (0, 0, 255), (j * 30, i * 30, 30, 30))

        pygame.draw.rect(screen, (255, 0, 0), (food.x * 30, food.y * 30, 30, 30))

        # Update the display
        pygame.display.update()
        clock.tick(clock.get_ticks() + 10)

# Run the main function
if __name__ == "__main__":
    main()

                                
                                           
