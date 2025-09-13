from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reset_position(self):
        """Send ball to top right"""
        self.goto(0, 0)
        self.move_speed = 0.05
        self.bounce_x()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 1 # optional, makes ball speed up

        

    # In the snake game, the ball food disappeared and reappeared at random locations,
    # Here, the ball detects collision and then simply changes direction randomly towards the other end of the screen
    # so refresh will probably be used after ball detects collision with paddle or wall

