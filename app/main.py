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

    if health <= 100:
        for s in data["snakes"]:
            if s["id"] == "340c4aca-4a65-4bb1-9009-8dccd6602d14":
                snake = s
        food = data['food']
        move = utils.move_to_food(food, snake)
    else:
        turn = data['turn']
        if turn % 4 is 0:
            move = 'north'
        elif turn % 4 is 1:
            move = 'east'
        elif turn % 4 is 2:
            move = 'south'
        elif turn % 4 is 3:
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
