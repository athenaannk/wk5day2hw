from app import app

from flask import render_template, request, url_for, redirect

from .services import get_pokemon

import requests, json


from app import app



from .auth.forms import SignUpForm, LoginForm, Poke_Name
from .models import User

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

# @app.route()
# @catch_pokemon
# def catch():
#     u = User.query.get(pokename)
#     if u:
#         user.catch(u)
#         flash(f"You caught {pokename}", category='success')
#     else:
#         flash(f"{pokename} doesn't exist!", category='danger')

#     return redirect(url_for('homePage'))

