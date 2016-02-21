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

    turn = data['turn']
    if turn % 8 is 0:
        move = 'north'
    elif turn % 8 is 1:
        move = 'east'
    elif turn % 8 is 2:
        move = 'south'
    elif turn % 8 is 3:
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
