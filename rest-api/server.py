from flask import Flask;
from modules.pokemons.pokemons_controller import init_pokemon_routes

app = Flask(__name__)

init_pokemon_routes(app)

if __name__ == '__main__':
    app.run(debug=True)