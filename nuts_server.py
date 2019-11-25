import re, json
import dispenser
from bottle import get, response, route, run
PORT = 8080
TOKEN = 'TOKEN'
HOST = 'localhost'

@get('/dispense/nuts/{TOKEN}')
def dispense():
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    nuts_dispenser = dispenser.Dispenser()
    nuts_dispenser.enable_engine()
    nuts_dispenser.dispense_food()
    nuts_dispenser.disable_engine()
    return json.dumps({'status': 'OK'})

run(host=HOST, port=PORT)