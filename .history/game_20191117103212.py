def draw_tanks():
    top_initial_spacing = ' ' * 3
    bottom_initial_spacing = ' ' * 2
    middle_initial_spacing = ' ' * 1
    top_middle_spacing = ' ' * 20
    middle_middle_spacing = ' ' * 6
    tank_top = '-' * 4
    tank_bottom = '*' * 4
    tank_middle = '-' * 6
    line_break = '\n'
    cannon = '=' * 5
    print(top_initial_spacing, tank_top, top_middle_spacing, tank_top, line_break,
          middle_initial_spacing, tank_middle, cannon, middle_middle_spacing, cannon, tank_middle, line_break,
          bottom_initial_spacing, tank_top, top_middle_spacing, tank_top, line_break,
          bottom_initial_spacing, tank_bottom, top_middle_spacing, tank_bottom, line_break,)

draw_tanks()
