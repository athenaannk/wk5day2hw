import requests 
import time
#import numpy as np
#import sys

def get_pokemon(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response = requests.get(url)
    if response.ok:
        my_dict = response.json()
        pokemon_dict = {}
        pokemon_dict["name"] = my_dict["name"]
        pokemon_dict["ability"] = my_dict["abilities"][0]["ability"]["name"]
        pokemon_dict["base_xp"] = my_dict["base_experience"]
        pokemon_dict["front_shiny"] = my_dict["sprites"]["front_shiny"]
        pokemon_dict["base_atk"] = my_dict["stats"][1]["base_stat"]
        pokemon_dict["base_hp"] = my_dict["stats"][0]["base_stat"]
        pokemon_dict["base_def"] = my_dict["stats"][2]["base_stat"]
        return pokemon_dict

# def delay_print(s):
#     #stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
#     for c in s:
#         sys.stdout.write(c)
#         sys.stdout.flush()
#         time.sleep(0.05)

# class Pokemon:
#     def __init__(self, name, types, moves, EVs, heath='=============='):
#         self.name = name
#         self.type = types
#         self.moves = moves
#         self.attack = EVs ['ATTACK']
#         self.defense = EVs ['DEFENSE']
#         self.health=health
#         self.bars = 20 #amount of health bars left for each pokemon

#     def fight(self, Pokemon2):
#         print("\nPOKEMON BATTLE")
#         print(f"\n(self.name)")
#         print("\nTYPE/", self.types)
#         print("\nATTACK/", self.attack)
#         print("\nDEFENSE/",self.defense)
#         print("\nLVL/", 3*(1+np.mean([self.attack, self.defense])))

#         print("\nVS")
           
       
#         print(f"\n(Pokemon2.name)")
#         print("\nTYPE/", Pokemon2.types)
#         print("\nATTACK/", Pokemon2.attack)
#         print("\nDEFENSE/",Pokemon2.defense)
#         print("\nLVL/", 3*(1+np.mean([Pokemon2.attack, Pokemon2.defense])))

#         time.sleep(2)

#         version = ['Fire', 'Water', 'Grass']
#         for i,k in enumerate(version):
#             if self.types == k:
#                 #both types are the same
#                 if Pokemon2.types == k:
#                     attack_1 = 'It is not very effective.'
#                     attack_2= 'It is not very effective.'  

#                 #pokemon2 is strong
#                 if Pokemon2.types == version[(i+1)%3]:
#                     Pokemon2.attack *= 2
#                     Pokemon2.defense *= 2
#                     self.attack /= 2
#                     self.defense /= 2
#                     attack_1 = 'It is not very effective.'
#                     attack_2= 'It is super effective!'

#                 #pokemon2 is weak
#                 if Pokemon2.types == version[(i+2)%3]:
#                     self.attack *= 2
#                     self.defense *= 2
#                     Pokemon2.attack /= 2
#                     Pokemon2.defense /= 2
#                     attack_1 = 'It is super effective!'
#                     attack_2 = 'It is not very effective.'
#                 #while pokemon still have health
#                 while (self.bars >0) and (Pokemon2.bars >0):
#                     print(f"\n{self.name}\t\tHEALTH\t{self.health}")
#                     print(f"\n{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}")
                
#                     print(f"\nLET'S GO {self.name}!")
#                     for i, x in enumerate(self.moves):
#                         print(f"\n{i+1.}", x)
#                     move = int(input(\n'Pick a Move: '))
#                     delay_print(f"\n{self.name} used {self.moves[move-1]}!")
#                     time.sleep(1)
#                     delay_print(attack_1)

#                 #assess damage
#                 Pokemon2.bars -= self.attack
#                 Pokemon2.health=""

#                 #add bars back plus defense boost
#                 for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
#                     Pokemon2.health += "="

#                 time.sleep(1)
#                 print(f"\n{self.name}\t\tHEALTH\t{self.health}")
#                 print(f"\n{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}")

#                 time.sleep(.5)

#                 #check to see if pokemon2 is ok
#                 if Pokemon2.bars <0:
#                     delay_print("\n..." + Pokemon2.name + 'is unwell.')
#                     break
#                 #pokemon 2's turn
#                 print(f"\nLET'S GO {Pokemon2.name}!")
#                 for i, x in enumerate(Pokemon2.moves):
#                     print(f"\n{i+1.}", x)
#                 move = int(input('Pick a Move: '))
#                 delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[move-1]}!")
#                 time.sleep(1)
#                 delay_print(attack_2)

#                 #assess damage
#                 self.bars -= self.attack
#                 self.health=""

#                 #add bars back plus defense boost
#                 for j in range(int(self.bars+.1*self.defense)):
#                     self.health += "="

#                 time.sleep(1)
#                 print(f"\n{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}")
#                 print(f"\n{self.name}\t\tHEALTH\t{self.health}")

#                 time.sleep(.5)

#                 if self.bars <0:
#                     delay_print("\n..." + self.name + 'is unwell.')
#                     break

#if __name__== '__main__':
    #create pokemon objects in the api and their sign??