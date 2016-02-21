import bottle
import os
import utils


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/yeezus.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#b36c42',
        'head': head_url
    }


@bottle.post('/start')
def start():
    data = bottle.request.json

    return {
        'taunt': 'Keitse taught me'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    for s in data["snakes"]:
        if s["id"] == "340c4aca-4a65-4bb1-9009-8dccd6602d14":
            snake = s
        food = data['food']
    if snake['health'] < 100:
        move = utils.move_to_food(food, snake)
    else:
        # all glory to loop snake
        turn = data['turn']
        if turn % 8 is 0 or turn % 8 is 1:
            move = 'north'
        elif turn % 8 is 2 or turn % 8 is 3:
            move = 'east'
        elif turn % 8 is 4 or turn % 8 is 5:
            move = 'south'
        elif turn % 8 is 6 or turn % 8 is 7:
            move = 'west'

    if utils.collision(move, snake, data):
        move = utils.calc_move(move, snake, data)

    return {
        'move': move,
        'taunt': 'move'
    }


@bottle.post('/end')
def end():
    data = bottle.request.json

    return {
        'taunt': 'end'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
