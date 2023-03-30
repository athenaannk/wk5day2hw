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


