import arcade

# Creating MainGame class       
class MainGame(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, title="Player Movement")
  
        # Initializing the initial x and y coordinated
        self.x = 250 
        self.y = 250

        # Initializing a variable to store
        # the velocity of the player
        self.vel_x = 100
        self.vel_y = 70

        self.mouse_x = 0
        self.mouse_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.mouse_x = x
        self.mouse_y = y
    
    # Creating on_draw() function to draw on the screen
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("x = {}\n y = {} \n X = {}\n Y = {}".format(
            round(self.x), round(self.y), round(self.mouse_x), round(self.mouse_y)),
                        120.0,300.0, arcade.color.WHITE)

        arcade.draw_rectangle_filled(self.x, self.y,50, 50,
                                     arcade.color.GREEN )

    def on_update(self,delta_time):
        self.x += self.vel_x * delta_time
        self.y += self.vel_y * delta_time
        # Changing the direction of
        # movement if player crosses the screen
        if self.x>=550 or self.x<=50:
            self.vel_x *= -1
        if self.y>=550 or self.y<=50:
            self.vel_y *= -1

        dx = abs(self.x - self.mouse_x)
        dy = abs(self.y - self.mouse_y)
        if dx<=25 and dy<=25:
            if dx > dy:
                self.vel_x *= -1
                self.x += self.vel_x* delta_time*1.3
            elif dx < dy:
                self.vel_y *= -1
                self.y += self.vel_y * delta_time*1.3

          
# Calling MainGame class       
MainGame()
arcade.run()