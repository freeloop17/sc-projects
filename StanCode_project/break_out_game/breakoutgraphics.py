"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)
        self.paddle_offset = paddle_offset
        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height,
                            x=(self.window_width - paddle_width) / 2,
                            y=self.window_height - self.paddle_offset - paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window.
        self.size = ball_radius*2
        self.ball = GOval(self.size, self.size,
                          x=(self.window_width - self.size) / 2, y=(self.window_height - self.size) / 2)
        self.ball.filled = True
        self.window.add(self.ball)
        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED
        self.brick_count = brick_cols * brick_rows

        # Initialize our mouse listeners.
        # onmouseclicked(self.handle_click())
        onmousemoved(self.move_paddle)
        # Create bricks
        for i in range(brick_cols):
            brick_on_x = i * (brick_width + brick_spacing)
            for j in range(brick_rows):
                num_of_same_color_row = brick_rows // 5
                brick_on_y = brick_offset + j * (brick_height + brick_spacing)
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                if 0 <= j < num_of_same_color_row:
                    brick.fill_color = 'black'
                    brick.color = 'black'
                elif num_of_same_color_row <= j < 2 * num_of_same_color_row:
                    brick.fill_color = 'darkgray'
                    brick.color = 'darkgray'
                elif 2 * num_of_same_color_row <= j < 3 * num_of_same_color_row:
                    brick.fill_color = 'dimgray'
                    brick.color = 'dimgray'
                elif 3 * num_of_same_color_row <= j < 4 * num_of_same_color_row:
                    brick.fill_color = 'gray'
                    brick.color = 'gray'
                else:
                    brick.fill_color = 'lightgray'
                    brick.color = 'lightgray'
                self.window.add(brick, x=brick_on_x, y=brick_on_y)

    # collide with paddle
    def is_collide_paddle(self):
        ball_left_top = self.window.get_object_at(self.ball.x, self.ball.y)
        ball_right_top = self.window.get_object_at(self.ball.x + self.size, self.ball.y)
        ball_left_bottom = self.window.get_object_at(self.ball.x, self.ball.y + self.size)
        ball_right_bottom = self.window.get_object_at(self.ball.x + self.size, self.ball.y + self.size)
        if ball_left_bottom == self.paddle or ball_right_bottom == self.paddle:
            return True

    # collide with brick
    def is_collide_brick(self):
        ball_left_top = self.window.get_object_at(self.ball.x, self.ball.y)
        ball_right_top = self.window.get_object_at(self.ball.x + self.size, self.ball.y)
        ball_left_bottom = self.window.get_object_at(self.ball.x, self.ball.y + self.size)
        ball_right_bottom = self.window.get_object_at(self.ball.x + self.size, self.ball.y + self.size)
        if ball_left_top is not None and ball_left_top is not self.paddle:
            self.window.remove(ball_left_top)
            return True
        if ball_right_top is not None and ball_right_top is not self.paddle:
            self.window.remove(ball_right_top)
            return True

    # Getter
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    # def reset_ball(self):
    #     self.set_ball_velocity()

    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def reset_ball_position(self):
        self.ball.x = (self.window_width - self.size) / 2
        self.ball.y = (self.window_height - self.size) / 2

    def move_paddle(self, event):
        if event.x >= self.window.width-self.paddle.width:
            self.paddle.x = self.window.width-self.paddle.width
        elif event.x <= self.paddle.width / 2:
            self.paddle.x = 0
        else:
            self.paddle.x = event.x - self.paddle.width / 2





