from flask import render_template, request;
import requests;

def init_pokemon_routes(app):
    @app.route('/')
    def listPokemons():
        response = requests.get('https://pokeapi.co/api/v2/pokemon')
        if response.ok:
            data = response.json()
            detailed_pokemons = []  # List to hold detailed data
            for pokemon in data['results']:
                # Fetch detailed data for each pokemon
                local_response = requests.get(pokemon['url'])
                if local_response.ok:
                    detailed_data = local_response.json()
                    detailed_pokemons.append(detailed_data)
                else:
                    print(f"Failed to fetch data for {pokemon['name']}")
            # Pass the list of detailed data to the template
            return render_template('list-pokemon.html', title='Home', pokemons=detailed_pokemons)
        else:   
            return 'Failed to fetch data'
        
    @app.route('/<name>')
    def editPokemon(name):
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
        if response.ok:
            data = response.json()
            return render_template('edit-pokemon.html', title='Pokemon', pokemon=data)
        else:
            return 'Failed to fetch data'
        