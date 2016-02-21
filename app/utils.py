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
    x = location[0]
    y = location[1]

    if abs(x) <= abs(y):
        if y >= 0:
            return 'north'

        elif y < 0:
            return 'south'

    if abs(x) > abs(y):
        if x >= 0:
            return 'west'

        elif x < 0:
            return 'east'
