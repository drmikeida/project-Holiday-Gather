import pyxel
import random
class App:
    def __init__(self):
        # Initialize the Pyxel window (width, height)
        pyxel.init(160, 120)
        # Set the initial position of the square
        self.x = 75
        self.y = 85
        self.score = 0
        # Create a list to hold enemy data
        self.enemies = []
        # Spawn the first enemy
        self.enemies.append({
            'x': random.randint(0, 160),  # Random x-coordinate
            'y': random.randint(0, 120),  # Random y-coordinate
            'dx': random.choice([-2, 2]),  # Random horizontal movement
            'dy': random.choice([-2, 2])  # Random vertical movement
        })
        # Create a list to hold item data
        self.items = []
        self.spawn_item()  # Spawn the first item
        self.game_over = False  # Flag to track game over
        self.play_again_button_pressed = False  # New button state
        # Start the game loop
        pyxel.run(self.update, self.draw)
    def update(self):
        # Only update positions if the game is not over
        if not self.game_over:
            # Update the square's position based on arrow keys
            if pyxel.btn(pyxel.KEY_UP):
                self.y -= 4
            if pyxel.btn(pyxel.KEY_DOWN):
                self.y += 4
            if pyxel.btn(pyxel.KEY_LEFT):
                self.x -= 4
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.x += 4
            # Update the square's position based on WASD keys
            if pyxel.btn(pyxel.KEY_W):
                self.y -= 4
            if pyxel.btn(pyxel.KEY_S):
                self.y += 4
            if pyxel.btn(pyxel.KEY_A):
                self.x -= 4
            if pyxel.btn(pyxel.KEY_D):
                self.x += 4
            # Wrap around
            self.x %= 160
            self.y %= 120
            # Update each enemy's position
            for enemy in self.enemies:
                enemy['x'] += enemy['dx']
                enemy['y'] += enemy['dy']
                # Bounce the enemy off the edges of the screen
                if enemy['x'] <= 0 or enemy['x'] >= 160:
                    enemy['dx'] *= -1
                if enemy['y'] <= 0 or enemy['y'] >= 120:
                    enemy['dy'] *= -1
                # Check for collision with player
                if (self.x < enemy['x'] + 10 and self.x + 10 > enemy['x'] and
                        self.y < enemy['y'] + 10 and self.y + 10 > enemy['y']):
                    self.game_over = True
            # Check for collision with items
            for item in self.items:
                if (self.x < item['x'] + 5 and self.x + 10 > item['x'] and
                        self.y < item['y'] + 5 and self.y + 10 > item['y']):
                    self.score += 1
                    self.items.remove(item)
                    self.spawn_item()
                    # Spawn a new enemy every 5 points
                    if self.score % 5 == 0:
                        self.enemies.append({
                            'x': random.randint(0, 160),  # Random x-coordinate
                            'y': random.randint(0, 120),  # Random y-coordinate
                            'dx': random.choice([-2, 2]),  # Random horizontal movement
                            'dy': random.choice([-2, 2])  # Random vertical movement
                        })
        # Check if play again button is clicked
        if self.game_over:
            if pyxel.btnp(pyxel.KEY_SPACE):  # Check for space key press
                self.game_over = False
                self.score = 0
                self.enemies = []
                self.enemies.append({
                    'x': random.randint(0, 160),  # Random x-coordinate
                    'y': random.randint(0, 120),  # Random y-coordinate
                    'dx': random.choice([-2, 2]),  # Random horizontal movement
                    'dy': random.choice([-2, 2])  # Random vertical movement
                })
                self.items = []
                self.spawn_item()
    def draw(self):
        # Clear the screen with black (color 0)
        pyxel.cls(0)
        # Draw a square (color 9)
        pyxel.rect(self.x, self.y, 10, 10, 1)
        # Draw each enemy (color 4)
        for enemy in self.enemies:
            pyxel.rect(enemy['x'], enemy['y'], 5, 5, 4) # Draw a blue square
        # Draw each item (color 10)
        for item in self.items:
            pyxel.rect(item['x'], item['y'], 5, 5, 7)
        # Display the score
        pyxel.text(5, 5, f"Score: {self.score}", 7)
        # Display a message when score is high
        if self.score >= 5:
            pyxel.text(50, 50, "You’re doing great!", 8)
        # Display "Game Over" message if game_over is True
        if self.game_over:
            pyxel.text(50, 60, "Game Over!", 11)
            pyxel.text(50,70, "Press 'space' to try again!", 7)
    def spawn_item(self):
        self.items.append({
            'x': random.randint(0, 160),
            'y': random.randint(0, 120)
        })
# Run the game
App()