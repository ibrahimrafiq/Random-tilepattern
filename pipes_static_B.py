from graphics import *
import random


def draw_left_up_ninety(win, x, y, fill_color):
    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)

    center_x = x + width / 2
    center_y = y + height / 2

    win.line(center_x, y, center_x, center_y, width=10)

    win.line(x, center_y, center_x, center_y, width=10)


def draw_right_down_ninety(win, x, y, fill_color):
    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)

    center_x = x + width / 2
    center_y = y + height / 2
    pt_y = x + (width / 2 + height / 2)
    pt_x = y + (height / 2 + width / 2)

    win.line(center_x, pt_x, center_x, center_y, width=10)

    win.line(pt_y, center_y, center_x, center_y, width=10)


def draw_dead_end_left(win, x, y, fill_color):
    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)

    center_x = x + width / 2
    center_y = y + height / 2

    pt_y = x + (width / 2 + height / 2)
    pt_x = y + (height / 2 + width / 2)

    width_small = 30
    height_small = 30

    center_xs = center_x - width_small / 2
    center_ys = center_y - height_small / 2

    win.rectangle(center_xs, center_ys, width_small, height_small, fill="black")

    win.line(pt_y, center_y, center_x, center_y, width=10)


def draw_dead_end_right(win, x, y, fill_color):
    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)

    center_x = x + width / 2
    center_y = y + height / 2

    win.line(x, center_y, center_x, center_y, width=10)

    width_small = 30
    height_small = 30

    center_xs = center_x - width_small / 2
    center_ys = center_y - height_small / 2

    win.rectangle(center_xs, center_ys, width_small, height_small, fill="black")


def draw_dead_end_up(win, x, y, fill_color):
    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)

    center_x = x + width / 2
    center_y = y + height / 2
    pt_y = x + (width / 2 + height / 2)
    pt_x = y + (height / 2 + width / 2)

    # vertical line
    win.line(center_x, pt_x, center_x, center_y, width=10)

    width_small = 30
    height_small = 30
    center_xs = center_x - width_small / 2
    center_ys = center_y - height_small / 2

    win.rectangle(center_xs, center_ys, width_small, height_small, fill="black")


def horiontal_line(win, x, y, fill_color):
    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)

    center_x = x + width / 2
    center_y = y + height / 2
    pt_y = x + (width / 2 + height / 2)

    win.line(x, center_y, pt_y, center_y, width=10)


def vertical_line(win, x, y, fill_color):
    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)

    center_x = x + width / 2
    center_y = y + height / 2
    pt_x = y + (height / 2 + width / 2)

    win.line(center_x, y, center_x, pt_x, width=10)


def horizontal_down(win, x, y, fill_color):
    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)

    center_x = x + width / 2
    center_y = y + height / 2
    pt_y = x + (width / 2 + height / 2)
    pt_x = y + (height / 2 + width / 2)

    win.line(x, center_y, pt_y, center_y, width=10)

    # vertical line
    win.line(center_x, pt_x, center_x, center_y, width=10)


def horizontal_up(win, x, y, fill_color):
    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)

    center_x = x + width / 2
    center_y = y + height / 2
    pt_y = x + (width / 2 + height / 2)

    win.line(x, center_y, pt_y, center_y, width=10)

    win.line(center_x, y, center_x, center_y, width=10)


def vertical_right(win, x, y, fill_color):
    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)

    center_x = x + width / 2
    center_y = y + height / 2
    pt_x = y + (height / 2 + width / 2)
    pt_y = x + (width / 2 + height / 2)
    win.line(center_x, y, center_x, pt_x, width=10)

    win.line(pt_y, center_y, center_x, center_y, width=10)


def line_blue_cross(win, x, y, fill_color):

    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)

    center_x = x + width / 2
    center_y = y + height / 2
    pt_x = y + (height / 2 + width / 2)
    pt_y = x + (width / 2 + height / 2)
    win.line(center_x, y, center_x, pt_x, width=10)
    win.line(x, center_y, center_x, center_y, width=10)

    width_small = 30
    height_small = 30
    center_xs = center_x - width_small / 2
    center_ys = center_y - height_small / 2

    win.rectangle(center_xs, center_ys, width_small, height_small, fill="black")

    center_x = x + width / 2
    center_y = y + height / 2
    pt_x = y + (height / 2 + width / 2)
    pt_y = x + (width / 2 + height / 2)
    win.line(center_x, y, center_x, pt_x, width=5, fill="blue")
    win.line(x, center_y, center_x, center_y, width=5, fill="blue")

    width_small = 20
    height_small = 20
    center_xs = center_x - width_small / 2
    center_ys = center_y - height_small / 2

    win.rectangle(center_xs, center_ys, width_small, height_small, fill="blue")


def line_blue_left(win, x, y, fill_color):
    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)

    center_x = x + width / 2
    center_y = y + height / 2
    pt_x = y + (height / 2 + width / 2)
    pt_y = x + (width / 2 + height / 2)
    win.line(center_x, y, center_x, pt_x, width=10)
    win.line(pt_y, center_y, center_x, center_y, width=10)

    win.line(center_x, y, center_x, pt_x, width=5, fill="blue")
    win.line(pt_y, center_y, center_x, center_y, width=5, fill="blue")


def line_blue_up(win, x, y, fill_color):
    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)
    center_x = x + width / 2
    center_y = y + height / 2
    pt_y = x + (width / 2 + height / 2)

    win.line(x, center_y, pt_y, center_y, width=10)
    win.line(center_x, y, center_x, center_y, width=10)

    win.line(x, center_y, pt_y, center_y, width="5", fill="blue")
    win.line(center_x, y, center_x, center_y, width="5", fill="blue")


def blue_90_right(win, x, y, fill_color):

    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)

    center_x = x + width / 2
    center_y = y + height / 2
    pt_y = x + (width / 2 + height / 2)
    pt_x = y + (height / 2 + width / 2)

    # vertical line
    win.line(center_x, center_y, center_x, pt_x, width=10)
    # horizontal line
    win.line(center_x, center_y, pt_y, center_y, width=10)

    win.line(center_x, center_y, center_x, pt_x, width=5, fill="blue")
    win.line(center_x, center_y, pt_y, center_y, width=5, fill="blue")


def blue_90_left(win, x, y, fill_color):
    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)

    center_x = x + width / 2
    center_y = y + height / 2

    # vertical line
    win.line(center_x, y, center_x, center_y, width=10)

    # horizontal line
    win.line(x, center_y, center_x, center_y, width=10)

    # repeat for diff color
    win.line(center_x, y, center_x, center_y, width=5, fill="blue")

    win.line(x, center_y, center_x, center_y, width=5, fill="blue")


def blue_end_up(win, x, y, fill_color):
    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)

    center_x = x + width / 2
    center_y = y + height / 2
    pt_y = x + (width / 2 + height / 2)
    pt_x = y + (height / 2 + width / 2)

    # vertical line
    win.line(center_x, pt_x, center_x, center_y, width=10)

    width_small = 30
    height_small = 30
    center_xs = center_x - width_small / 2
    center_ys = center_y - height_small / 2
    win.rectangle(center_xs, center_ys, width_small, height_small, fill="black")

    width_small = 20
    height_small = 20
    center_xs = center_x - width_small / 2
    center_ys = center_y - height_small / 2

    win.rectangle(center_xs, center_ys, width_small, height_small, fill="blue")
    win.line(center_x, pt_x, center_x, center_y, width=5, fill="blue")


def blue_90_up_right(win, x, y, fill_color):

    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)

    center_x = x + width / 2
    center_y = y + height / 2
    pt_y = x + (width / 2 + height / 2)
    pt_x = y + (height / 2 + width / 2)

    # vertical line
    win.line(center_x, y, center_x, center_y, width=10)

    win.line(pt_y, center_y, center_x, center_y, width=10)

    win.line(center_x, y, center_x, center_y, width=5, fill="blue")

    win.line(pt_y, center_y, center_x, center_y, width=5, fill="blue")


def left_down_90(win, x, y, fill_color):

    width = 95
    height = 95

    win.rectangle(x, y, width, height, fill_color)

    center_x = x + width / 2
    center_y = y + height / 2
    pt_y = x + (width / 2 + height / 2)
    pt_x = y + (height / 2 + width / 2)

    win.line(center_x, pt_x, center_x, center_y, width=10)

    win.line(x, center_y, center_x, center_y, width=10)


random_funcs = [
    draw_left_up_ninety,
    draw_right_down_ninety,
    draw_dead_end_left,
    draw_dead_end_right,
    draw_dead_end_up,
    horiontal_line,
    vertical_line,
    horizontal_down,
    horizontal_up,
    vertical_right,
    line_blue_cross,
    line_blue_left,
    line_blue_up,
    blue_90_right,
    blue_90_left,
    blue_end_up,
    blue_90_up_right,
    left_down_90,
]


def random_fucntion(win, x, y, fill_color):
    random_name = random.choice(random_funcs)
    random_name(win, x, y, fill_color="grey")


def main():
    win = graphics(w=500, h=500, title="Pipe Grid")

    for row in range(5):
        for col in range(5):
            x = row * 100
            y = col * 100
            random_fucntion(win, x, y, fill_color="grey")


main()
