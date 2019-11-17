def draw_tanks():
    # Initial Spacing
    top_initial_spacing = ' ' * 3
    bottom_initial_spacing = ' ' * 2
    middle_initial_spacing = ' ' * 1

    # Middle Spacing
    top_middle_spacing = ' ' * 30
    middle_middle_spacing = ' ' * 16
    middle_bottom_spacing = ' ' * 28

    # Tank Components
    tank_top = '-' * 4
    tank_bottom = '****'
    tank_middle = '-' * 6
    line_break = '\n'
    cannon = '=' * 5
    print(top_initial_spacing, tank_top, top_middle_spacing, tank_top, line_break,
          middle_initial_spacing, tank_middle, cannon, middle_middle_spacing, cannon, tank_middle, line_break,
          middle_initial_spacing, tank_middle, middle_bottom_spacing, tank_middle, line_break,
          bottom_initial_spacing, tank_bottom, top_middle_spacing, tank_bottom, line_break,)

draw_tanks()
