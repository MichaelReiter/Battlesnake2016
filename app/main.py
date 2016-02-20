import bottle
import os
from board import Board
# from snake import Snake
from queue import Queue
# import utils

moves = Queue()
board = Board()
# snake = Snake()


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

    move = 'west'

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
