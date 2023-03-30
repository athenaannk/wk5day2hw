from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from app.models import Pokemon, User, pokesquadTable
from sqlalchemy import select

pokesquad = Blueprint('pokesquad', __name__, template_folder='pokesquad_templates')

@pokesquad.route('/capture/<int:pokename>')
def catchPokemon(pokename):
    pokemon = Pokemon.query.get(pokename)
    if pokemon:

        current_user.catch(pokemon)

    return redirect(url_for('pokesquad.viewCurrentSquad'))

@pokesquad.route('/release/<int:pokename>')
def releasePokemon(pokename):
    pokemon = Pokemon.query.get(pokename)
    if pokemon:
        current_user.release(pokemon)

    return redirect(url_for('pokesquad.viewCurrentSquad'))

@pokesquad.route('/current_squad')
def viewCurrentSquad():
    viewSquad = Pokemon.query.join(squadTable).join(User).filter(squadTable.c.user_id == current_user.user_id)
    return render_template('pokesquad.html', viewSquad=viewSquad)

@pokesquad.route('/battle/<current_user>/<user>')
def battleRoyale(user, current_user):
    user1 = User.query.filter(User.first_name == user).first()
    user2 = User.query.filter(User.first_name == current_user).first()
    print(user1.wins)

    pokesquad1 = user1.pokesquad.all()
    pokesquad2 = user2.pokesquad.all()

    health_defense_points1 = 0
    attack_points1 = 0
    health_defense_points2 = 0
    attack_points2 = 0

    for pokemon in pokesquad1:
        health_defense_points1 += pokemon.defense
        health_defense_points1 += pokemon.hp
        attack_points1 += pokemon.attack

    for pokemon in pokesquad2:
        health_defense_points2 += pokemon.defense
        health_defense_points2 += pokemon.hp
        attack_points2 += pokemon.attack

    overall_points_pokesquad1 = health_defense_points1 - attack_points2
    overall_points_pokesquad2 = health_defense_points2 - attack_points1

    if overall_points_pokesquad1 > overall_points_pokesquad2:
        user1.wins += 1
        user2.losses += 1
        user1.savePokemon()
        user2.savePokemon()


    elif overall_points_pokesquad1 < overall_points_pokesquad2:
        user1.losses += 1
        user2.wins += 1
        user1.savePokemon()
        user2.savePokemon()

        

    elif overall_points_pokesquad1 == overall_points_pokesquad2:
        user1.ties += 1
        user2.ties += 1
        user1.savePokemon()
        user2.savePokemon()


    return render_template('battleroyale.html', pokesquad1=pokesquad1, pokesquad2=pokesquad2, user1=user1, user2=user2, overall_points_pokesquad1=overall_points_pokesquad1, overall_points_pokesquad2=overall_points_pokesquad2)