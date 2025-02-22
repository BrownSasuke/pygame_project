import pygame
import random
from constants import *  # Import everything from constants.py

# Create an asteroid class to store its properties
class Asteroid:
    def __init__(self, x, y, radius, dx, dy):
        self.x = x
        self.y = y
        self.radius = radius
        self.dx = dx  # Movement in the x-direction
        self.dy = dy  # Movement in the y-direction
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))  # Random color

    def move(self):
        self.x += self.dx
        self.y += self.dy
        
        # Wrap around the screen if the asteroid goes off-screen
        if self.x > SCREEN_WIDTH:
            self.x = 0
        elif self.x < 0:
            self.x = SCREEN_WIDTH
        
        if self.y > SCREEN_HEIGHT:
            self.y = 0
        elif self.y < 0:
            self.y = SCREEN_HEIGHT

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize pygame
    pygame.init()

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the title of the window
    pygame.display.set_caption("Asteroids Game")

    # Create a list to store the asteroids
    asteroids = []

    # Create random asteroids
    for _ in range(5):  # Generate 5 asteroids
        asteroid_radius = random.randint(ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS)
        asteroid_x = random.randint(0, SCREEN_WIDTH)
        asteroid_y = random.randint(0, SCREEN_HEIGHT)
        asteroid_dx = random.uniform(-1, 1)  # Random movement speed in the x-direction
        asteroid_dy = random.uniform(-1, 1)  # Random movement speed in the y-direction
        asteroids.append(Asteroid(asteroid_x, asteroid_y, asteroid_radius, asteroid_dx, asteroid_dy))

    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update and draw each asteroid
        screen.fill((0, 0, 0))  # Clear the screen (black background)
        for asteroid in asteroids:
            asteroid.move()  # Move the asteroid
            asteroid.draw(screen)  # Draw the asteroid
        
        # Update the game display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()
