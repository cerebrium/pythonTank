import math

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
    print( line_break, bottom_initial_spacing, 'WELCOME TO TANKS IN THE TERMINAL', line_break, line_break,
        bottom_initial_spacing, tank_top, top_middle_spacing, tank_top, line_break,
        middle_initial_spacing, tank_middle, cannon, middle_middle_spacing, cannon, tank_middle, line_break,
        middle_initial_spacing, tank_middle, middle_bottom_spacing, tank_middle, line_break,
        bottom_initial_spacing, tank_bottom, top_middle_spacing, tank_bottom, line_break,
        )

def draw_tank_one():
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

    print(
        top_initial_spacing, tank_top, line_break,
        middle_initial_spacing, tank_middle, cannon, '  *', line_break,
        middle_initial_spacing, tank_middle, line_break,
        bottom_initial_spacing, tank_bottom,
        )   

def draw_tank_two():
        # Initial Spacing
    top_initial_spacing = ' ' * 3
    bottom_initial_spacing = ' ' * 2
    middle_initial_spacing = ' ' * 1

    # Middle Spacing
    top_middle_spacing = ' ' * 19
    one_tank_special_spacing = ' ' * 18
    middle_middle_spacing = ' ' * 7
    middle_bottom_spacing = ' ' * 17

    # Tank Components
    tank_top = '-' * 4
    tank_bottom = '****'
    tank_middle = '-' * 6
    line_break = '\n'
    cannon = '=' * 5

    print(
        top_middle_spacing, tank_top, line_break,
        middle_middle_spacing, '*  ', cannon, tank_middle, line_break,
        middle_bottom_spacing, tank_middle, line_break,
        one_tank_special_spacing, tank_bottom, line_break,
        )        

def get_velocity_and_angle():
    velocity, angel = input('Please enter a velocity (x-component) and an angle (in degrees)!').split()
    print(int(velocity)**2)
    print(math.degrees(math.sin(2*math.radians(int(angel)))))
    endpoint = ((int(velocity)**2)*math.degrees(math.sin(2*math.radians(int(angel)))))/9.8
    return endpoint 

def draw_line(tank1_coord, tank2_coord, shot):
    if int(tank1_coord) and int(tank2_coord) and int(shot) < 200 and int(tank1_coord) and int(tank2_coord) and int(shot) > 0:
        myLine = list('-'*200)
        myLine[int(tank1_coord)] = 'Tank1'
        myLine[int(tank2_coord)] = 'Tank2'
        myLine[int(shot)] = 'shot'   
    else:
        myLine = 'your shot is so far off it is not within the range of the display array!'     
    print(myLine)

def winner(tank):
    print(f'GAME OVER YOU HAVE WON: {tank}')

def player_one_goes(tank2, tank1):
    line_break = '\n'
    print(line_break)
    print('Player One Turn!')
    print(line_break)
    draw_tank_one()
    print(line_break)
    endpoint_for_tank1_shot = get_velocity_and_angle()
    print(line_break)
    if (int(tank2) == int(endpoint_for_tank1_shot)):
        winner('PLAYER 1')
        return False
    else:
        print(f'You shot and hit {int(endpoint_for_tank1_shot)}, you were {int(tank2)-int(endpoint_for_tank1_shot)} off of tank2!')
        print(line_break)
        draw_line(tank1, tank2, endpoint_for_tank1_shot)
        return True    

def player_two_goes(tank1, tank2):
    line_break = '\n'
    print(line_break)
    print('Player Two Turn!')
    print(line_break)
    draw_tank_two()
    print(line_break)
    endpoint_for_tank2_shot = get_velocity_and_angle()
    print(line_break)
    if (int(tank1) == int(endpoint_for_tank2_shot)):
        winner('PLAYER 2')
        return False
    else:
        print(f'You shot and hit {int(endpoint_for_tank2_shot)}, you were {int(tank1)-int(endpoint_for_tank2_shot)} off of tank1!')
        print(line_break)
        draw_line(tank1, tank2, endpoint_for_tank2_shot)
        return True    


def play_game():
    draw_tanks()
    tank1, tank2 = input('Please give the coordinates of the two tanks (one number along x-axis)').split()
    while True:
        myVar = player_one_goes(tank2, tank1)
        if myVar == False:
            break
        myVar = player_two_goes(tank1, tank2)
        if myVar == False:
            break

play_game()        