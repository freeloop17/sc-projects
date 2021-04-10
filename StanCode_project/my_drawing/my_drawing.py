"""
File: my_drawing.py
Name: Ching-Ching Chuang
----------------------
This file shows how to use campy module to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause

# This controls the pause time (in millisecond) for the animation
DELAY = 50

window = GWindow(width='800', height='600')


def main():
    """
    Draw a Mac window with loading bar animation
    """
    mac_window()
    loading_bar()
    create_label()
    move()


def move():
    rect = GRect(20, 35, x=252 + 205, y=303)
    window.add(rect)
    vx = 3
    while True:
        rect.move(vx, 0)
        rect.filled = True
        rect.color = 'darkgrey'
        rect.fill_color = 'darkgrey'

        if rect.x + rect.width >= 550:
            rect.x = 457
            rect.y = 303
        pause(DELAY)


def create_label():
    label = GLabel("Loading.....", x=280, y=380)
    label.color = 'darkgrey'
    label.font = 'SansSerif-28'
    window.add(label)


def loading_bar():
    rect = GRect(300, 40, x=255, y=300)
    rect.color = 'lightgrey'
    window.add(rect)

    for i in range(0, 200, 25):
        rect_loading = GRect(20, 35, x=258 + i, y=303)
        rect_loading.filled = True
        rect_loading.color = 'darkgrey'
        rect_loading.fill_color = 'darkgrey'
        window.add(rect_loading)


def mac_window():
    # create Mac window
    big_rect = GRect(750, 500, x=5, y=5)
    big_rect.color = 'lightgrey'
    # create tool bar
    small_rect = GRect(750, 18, x=5, y=5)
    small_rect.filled = True
    small_rect.color = 'lightgrey'
    small_rect.fill_color = 'gainsboro'
    # create close window button
    oval_1 = GOval(12, 12, x=7, y=7)
    oval_1.filled = True
    oval_1.color = 'tomato'
    oval_1.fill_color = 'tomato'
    # create minimize window button
    oval_2 = GOval(12, 12, x=27, y=7)
    oval_2.filled = True
    oval_2.color = 'gold'
    oval_2.fill_color = 'gold'
    # create maximize window button
    oval_3 = GOval(12, 12, x=47, y=7)
    oval_3.filled = True
    oval_3.color = 'limegreen'
    oval_3.fill_color = 'limegreen'

    window.add(big_rect)
    window.add(small_rect)
    window.add(oval_1)
    window.add(oval_2)
    window.add(oval_3)


if __name__ == '__main__':
    main()
