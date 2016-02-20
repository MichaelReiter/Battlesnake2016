import bottle
import os
from board import Board
from snake import Snake
from queue import Queue
import utils


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.get('/')
def index():
    head_url = '%s://%s/static/yeezus.jpg' % (
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

    board = Board().initialize(data)
    for s in data["snakes"]:
        if s.id == "340c4aca-4a65-4bb1-9009-8dccd6602d14":
            snake = Snake.start(s)

    move = utils.move_to_food(board, snake)

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
