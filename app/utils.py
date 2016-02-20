# def find_food(snake, board):


def move_to_food(board, snake, queue):
    location = closest_food(board, snake)
    direct_move_to(snake, location, queue)


def closest_food(board, snake):
    """
    Takes a board and snake, calculates which food is the closest and provides
    the distance.
    """
    if len(board.food) == 0:
        return None

    dist_to_food = 100000
    closest_food = [0, 0]
    for item in board.food:
        x = snake.x - item[0]
        y = snake.y - item[1]

        sum_squared = x**2 + y**2
        if sum_squared < dist_to_food:
            dist_to_food = sum_squared
            closest_food = [x, y]

    x_dist = closest_food[0] - snake.x
    y_dist = closest_food[1] - snake.y

    return [x_dist, y_dist]


def direct_move_to(snake, location, queue):
    """
    Queues the moves to move to a location.
    """
    if snake.x >= 0:
        for m in range(snake.x):
            queue.enqueue('west')

    elif snake.x < 0:
        for m in range(abs(snake.x)):
            queue.enqueue('east')

    if snake.y >= 0:
        for m in range(snake.y):
            queue.enqueue('north')

    elif snake.y < 0:
        for m in range(abs(snake.y)):
            queue.enqueue('south')
