from fighters import fighter1, fighter2
from random import choice

while (fighter1['hp'] > 0 and fighter2['hp'] > 0):

    attack = choice(['punch', 'kick', 'bit'])
    attack_value = fighter1[attack] - fighter2['def']
    attack_value = max(attack_value, 0)
    print(fighter1['name'] + " : " + attack + " inflige " + str(attack_value) + " dégâts !")
    fighter2['hp'] = fighter2['hp'] - attack_value

    attack = choice(['punch', 'kick', 'bit'])
    attack_value = fighter2[attack] - fighter1['def']
    attack_value = max(attack_value, 0)
    print(fighter2['name'] + " : " + attack + " inflige " + str(attack_value) + " dégâts !")
    fighter1['hp'] = fighter1['hp'] - attack_value

if fighter1['hp'] > 0:
    print(fighter1['name'] + " gagne ! Il lui reste " + str(fighter1['hp']) + " points de vies.")
elif fighter2['hp'] > 0:
    print(fighter2['name'] + " gagne ! Il lui reste " + str(fighter2['hp']) + " points de vies.")
else:
    print("Les deux combattants sont K.O. Match nul !")