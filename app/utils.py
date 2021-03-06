def move_to_food(board, snake):
    location = closest_food(board, snake)
    return direct_move_to(snake, location)


def closest_food(food, snake):
    """
    Takes a board and snake, calculates which food is the closest and provides
    the distance.
    """
    dist_to_food = 100000
    nearest_food = [0, 0]
    for item in food:
        x = snake['coords'][0][0] - item[0]
        y = snake['coords'][0][1] - item[1]

        sum_squared = x**2 + y**2
        if sum_squared < dist_to_food:
            dist_to_food = sum_squared
            nearest_food = item

    print '\n\n\n\n nearest_food', nearest_food

    return nearest_food


def direct_move_to(snake, location):
    """
    Queues the moves to move to a location.
    """
    print '\n\n\n\n\n'
    food_x = location[0]
    food_y = location[1]
    print 'food_x', food_x, 'food_y', food_y

    snake_x = snake['coords'][0][0]
    snake_y = snake['coords'][0][1]
    print 'snake x', snake_x, 'snake_y', snake_y

    x = food_x - snake_x
    y = food_y - snake_y

    
    print 'x', 'y', x, y

    if y != 0:
        if y < 0:
            return 'north'
        else:
            return 'south'

    if x != 0:
        if x < 0:
            return 'west'
        else:
            return 'east'


def collision(move, snake, data):
    direction = {"north": -1,
                 "south": 1,
                 "east": 1,
                 "west": -1}
    amount = direction[move]

    current_pos = snake['coords'][0]

    occupied_positions = snake['coords'][1:]
    for s in data['snakes']:
        for c in s['coords']:
            occupied_positions.append(c)
    for w in data['walls']:
        occupied_positions.append(w)

    for w in data['width']:
        occupied_positions.append(w, 0)
        occupied_positions.append(w, data['height']) 

    for h in data['height']:
        occupied_positions.append(0, h)
        occupied_positions.append(data['width'], h)

    if move in ['north', 'south']:
        for pos in occupied_positions:
            if (current_pos[1] + amount) == pos:
                return True

    if move in ['east', 'west']:
        for pos in occupied_positions:
            if (current_pos[0] + amount) == pos:
                return True

    else:
        return False

def calc_move(move, snake, data):
    posibilites = ['north', 'east', 'south', 'west']
    for p in posibilites:
        if not collision:
            return p