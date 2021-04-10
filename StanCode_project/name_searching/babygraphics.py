"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    interval = (width-(GRAPH_MARGIN_SIZE*2))/len(YEARS)
    return GRAPH_MARGIN_SIZE + year_index * interval


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    height = CANVAS_HEIGHT

    for i in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_coordinate, 0, x_coordinate, height, width=LINE_WIDTH)
        canvas.create_text(x_coordinate+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    height_interval = (CANVAS_HEIGHT-(GRAPH_MARGIN_SIZE*2))/1000
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        color_index = i % len(COLORS)
        for j in range(len(YEARS)-1):
            year = str(YEARS[j])
            x_coordinate = get_x_coordinate(CANVAS_WIDTH, j)
            next_year = str(YEARS[j+1])
            next_x_coordinate = get_x_coordinate(CANVAS_WIDTH, j+1)
            if year in name_data[name]:
                rank = name_data[name][year]
                y_coordinate = GRAPH_MARGIN_SIZE + int(rank) * height_interval
            else:
                rank = '*'
                y_coordinate = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
            if next_year in name_data[name]:
                next_rank = name_data[name][next_year]
                next_y_coordinate = GRAPH_MARGIN_SIZE + int(next_rank) * height_interval
            else:
                next_rank = '*'
                next_y_coordinate = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
            canvas.create_line(x_coordinate, y_coordinate,
                               next_x_coordinate, next_y_coordinate,
                               width=LINE_WIDTH, fill=COLORS[color_index])
            if j == 0:
                canvas.create_text(x_coordinate + TEXT_DX, y_coordinate,
                                   text=name+" "+rank, anchor=tkinter.SW, fill=COLORS[color_index])
            canvas.create_text(next_x_coordinate+TEXT_DX, next_y_coordinate,
                               text=name+" "+next_rank, anchor=tkinter.SW, fill=COLORS[color_index])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
