from app import app

from flask import render_template, request, url_for, redirect

from .services import get_pokemon

import requests, json


from app import app



from .auth.forms import SignUpForm, LoginForm, Poke_Name
from .models import User, Pokemon

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemonPage():
    form = Poke_Name()
    if request.method == 'POST':
        if form.validate():
            pokename = form.poke_name.data
            poke_info = Pokemon.query.filter_by(name = pokename).first()
            if poke_info:
                print('from db')
                return render_template('pokepage.html', poke_info=poke_info, form=form)
            else:
                poke_info = get_pokemon(pokename)
                if poke_info:
                    name = poke_info["name"]
                    base_xp= poke_info["base_xp"]
                    front_shiny = poke_info["front_shiny"]
                    base_atk = poke_info["base_atk"]
                    base_hp = poke_info["base_hp"]
                    base_def = poke_info["base_def"]
                    new_poke = Pokemon(name, base_xp, front_shiny, base_atk, base_hp, base_def)
                    new_poke.savePokemon()
                    print('saved to db')
                    return render_template('pokepage.html', poke_info=poke_info, form=form)

    return render_template('pokepage.html',form=form)

# @app.route('/catchpokemon')
def catch():
    catchpokemon
    for p in catchpokemon:
        name = pokemon_dict["name"]
        base_xp= pokemon_dict["base_xp"]
        front_shiny = pokemon_dict["front_shiny"]
        base_atk = pokemon_dict["base_atk"]
        base_hp = pokemon_dict["base_hp"]
        base_def = pokemon_dict["base_def"]

    new = catch()
#     u = User.query.get(pokename)
#     if u:
#         user.catch(u)
#         flash(f"You caught {pokename}", category='success')
#     else:
#         flash(f"{pokename} doesn't exist!", category='danger')

#     return redirect(url_for('homePage'))

