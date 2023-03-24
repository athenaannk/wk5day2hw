from app import app

from flask import render_template, request, url_for, redirect
from .forms import Poke_Name
from .services import get_pokemon

import requests, json


@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemonPage():
    form = Poke_Name()
    if request.method == 'POST':
        if form.validate():
            pokename = form.poke_name.data
            poke_info = get_pokemon(pokename)
            print(poke_info)        
            return render_template('pokepage.html', poke_info=poke_info, form=form)
    return render_template('pokepage.html',form=form)