from flask import Flask;
from modules.pokemons.pokemons_controller import init_pokemon_routes;
from modules.forms.forms_controller import init_forms_routes;

app = Flask(__name__)

init_pokemon_routes(app)
init_forms_routes(app)

if __name__ == '__main__':
    app.run(debug=True)