import requests

url = 'http://localhost:8080/'

print requests.get(url)

data = {
    "game": "hairy-cheese",
    "mode": "advanced",
    "turn": 4,
    "height": 20,
    "width": 30,
    "snakes": [],
    "food": [
             [1, 2], [9, 3]
        ],
    "walls": [[2, 2]],
    "gold": [[5, 5]]
}

print requests.post(url + 'move', data=data)
