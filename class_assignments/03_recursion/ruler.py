def draw_line(tick_lenght, tick_lable=""):
    line = "-" * tick_lenght

    if tick_lable:
        line += " " + tick_lable
    print(line)


def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_interval(center_length)
        draw_interval(center_length - 1)


def draw_ruler(num_inches, major_lenght):
    draw_line(major_lenght, "0")

    for i in range(1, 1 + num_inches):
        draw_interval(major_lenght - 1)
        draw_line(major_lenght, str(i))


draw_ruler(5, 3)