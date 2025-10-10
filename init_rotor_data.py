# Initialisierung der Klassen mit Werten der Dictionaries - bei Änderungen einmal ausühren

import math
from classes import Model, Battery, Rotor, Physics
from data_batteries import *
from data_models import *
from data_rotors import *
from data_physics import *

# set model, battery, rotor, physics
use_model_dict = LOGO600SX 
use_battery_dict = Battery_Turnigy
use_rotor_dict = Rotorblatt_E182
use_physics_dict = Erde   

# Creating an instance of the class

this_model = Model(use_model_dict["brand"], 
                   use_model_dict["model"],
                   use_model_dict["net_mass"],
                   use_model_dict["Typical_TOM"],
                   use_model_dict["Länge"],
                   use_model_dict["Breite"],
                   use_model_dict["Höhe"],
                   use_model_dict["Zähne_HZR"],
                   use_model_dict["Zähne_Motorritzel"],
                   use_model_dict["Getriebe_TR"],
                   use_model_dict["Motor_name"],
                   use_model_dict["Motor_kV"],
                   use_model_dict["Tailrotor_Hebelarm_m"])

this_bat = Battery(use_battery_dict["bat_brand"], 
                   use_battery_dict["bat_type"],
                   use_battery_dict["bat_volt_per_cell_nominal"],
                   use_battery_dict["bat_volt_per_cell_load"],
                   use_battery_dict["bat_volt"],
                   use_battery_dict["bat_länge_mm"],
                   use_battery_dict["bat_breite_mm"],
                   use_battery_dict["bat_höhe_mm"],
                   use_battery_dict["bat_cells"],
                   use_battery_dict["bat_capacity_Wh"],
                   use_battery_dict["bat_capacity_usable_Wh"],
                   use_battery_dict["bat_mass_kg"])

this_rotor = Rotor(use_rotor_dict["Rotor_Profilart"], 
                   use_rotor_dict["Rotor_Profilname"], 
                   use_rotor_dict["Rotor_Anzahl"], 
                   use_rotor_dict["Rotor_Masse"], 
                   use_rotor_dict["Rotor_Blatttiefe_c"], 
                   use_rotor_dict["Rotor_Blattlänge_l"], 
                   use_rotor_dict["Rotor_Durchmesser"], 
                   use_rotor_dict["Rotor_Max_Drehzahl"],
                   use_rotor_dict["Rotor_cd0"])

this_physics = Physics(use_physics_dict["g"],
                       use_physics_dict["dynamische Viskosität"], 
                       use_physics_dict["kinematische Viskosität"], 
                       use_physics_dict["T"], 
                       use_physics_dict["Dichte"], 
                       use_physics_dict["Altitude"],
                       use_physics_dict["kappa_Korrektur"])
