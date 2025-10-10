import math
from init_rotor_data import this_bat, this_model, this_rotor, this_physics
from functions import *

# Calling the functions

#Header()

#Rotorkopfdrehzahl2(3.3, 0.85, 0.6, 6, 850, 11, 106)
#print(Heckrotorschub_T_TR())

print(this_model.info())
print(this_bat.info())
print(this_rotor.info())
print(this_physics.info())  

Rotorkopfdrehzahl2(3.3, 0.85, 0.6, 6, 850, 11, 106)

'''

vi_induzierte_geschw_ST(True)

P0_Profilwiderstandsleistung(True)

Gewichtskraft(True)

Rotorkopfdrehzahl(3.7, 0.93, 0.6)
Rotorkopfdrehzahl2(3.7, 0.93, 0.6, 6, 850, 11, 106)

print(rotor_flächendichte_sigma())

Schubbeiwert_CT(True)

Drehmomentbeiwert_CQ(True)

Schwebeflugleistung_P(True)

print(induzierter_Durchflussgrad_lambda_i())

print(induzierter_Durchflussgrad_lambda_hover())

print(CP_i_induzierter_Leistungsbeiwert())
print(CP_i_korrigiert_Leistungsbeiwert())

print(Leistungsgütegrad_FM())

print(einfacher_Blattspitzenverlust())

#Rotorkopfdrehzahl2(3.7, 0.93, 0.8, 6, 830, 11, 106)



'''