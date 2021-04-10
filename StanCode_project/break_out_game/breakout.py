"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3

graphics = BreakoutGraphics()
game_status = 0  # 0:the game does not start yet, 1:the game is ongoing
brick_cnt = graphics.brick_count
lives = NUM_LIVES


def main():
    onmouseclicked(handle_click)


def handle_click(mouse):
    graphics.set_ball_velocity()
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    global game_status
    global brick_cnt
    global lives
    if game_status == 0 and lives > 0 and brick_cnt > 0:
        # Add animation loop here
        while True:
            pause(FRAME_RATE)
            if brick_cnt == 0:
                graphics.reset_ball_position()
                break
            graphics.ball.move(dx, dy)
            game_status = 1
            if graphics.is_collide_paddle():
                if dy > 0:
                    dy = -dy
            if graphics.is_collide_brick():
                dy = -dy
                brick_cnt -= 1
            if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
                dx = -dx
            if graphics.ball.y <= 0:
                dy = -dy
            if graphics.ball.y >= graphics.window.height - graphics.ball.height:
                game_status = 0
                lives -= 1
                graphics.reset_ball_position()
                break
            # print(f'lives:{lives}')
            # print(f'brick count:{brick_cnt}')


if __name__ == '__main__':
    main()
