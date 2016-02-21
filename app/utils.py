def move_to_food(board, snake):
    location = closest_food(board, snake)
    return direct_move_to(snake, location)


def closest_food(food, snake):
    """
    Takes a board and snake, calculates which food is the closest and provides
    the distance.
    """
    dist_to_food = 100000
    closest_food = [0, 0]
    for item in food:
        x = snake['coords'][0][0] - item[0]
        y = snake['coords'][0][1] - item[1]

        sum_squared = x**2 + y**2
        if sum_squared < dist_to_food:
            dist_to_food = sum_squared
            closest_food = [x, y]

    x_dist = closest_food[0] - snake['coords'][0][0]
    y_dist = closest_food[1] - snake['coords'][0][1]

    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print x_dist, y_dist
    return [x_dist, y_dist]


def direct_move_to(snake, location):
    """
    Queues the moves to move to a location.
    """
    food_x = location[0]
    food_y = location[1]

    snake_x = snake['coords'][0][0]
    snake_y = snake['coords'][0][1]

    x = food_x - snake_x
    y = food_y - snake_y

    print '\n\n\n\n\n'
    print x, y

    if x is not 0:
        if x > 0:
            return 'west'
        else:
            return 'east'

    if y is not 0:
        if x > 0:
            return 'north'
        else:
            return 'south'
