# def find_food(snake, board):


def closest_food(board, snake):
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
