'''#Dictionaries mit Startwerten - bei Änderung einmal ausführen

Rotorblatt_E182 ={
    "Rotor_Profilart": "S-Schlag",
    "Rotor_Profilname": "E182_Test",
    "Rotor_Anzahl": 2,
    "Rotor_Masse": 0.2, #kg
    "Rotor_Blatttiefe_c" : 0.048 ,#m
    "Rotor_Blattlänge_l": 0.55, #m
    "Rotor_Durchmesser": 1.24, #m
    "Rotor_Max_Drehzahl": 1100, #RPM
    "Rotor_cd0": 0.0125 #Profilwiderstandsbeiwert
   
}


Rotorblatt_NACA0009 ={
    "Rotor_Profilart": "vollsymmetrisch",
    "Rotor_Profilname": "NACA0009",
    "Rotor_Anzahl": 2,
    "Rotor_Masse": 0.2, #kg
    "Rotor_Blatttiefe_c" : 0.048 ,#m
    "Rotor_Blattlänge_l": 0.55, #m
    "Rotor_Durchmesser": 1.24, #m
    "Rotor_Max_Drehzahl": 1500, #RPM
    "Rotor_cd0": 0.0125 #Profilwiderstandsbeiwert
   
}'''


List_Rotors = {
    "Rotorblatt_E182": {
        "Rotor_Profilart": "S-Schlag",
        "Rotor_Profilname": "E182_Test",
        "Rotor_Anzahl": 2,
        "Rotor_Masse": 0.2,
        "Rotor_Blatttiefe_c": 0.048,
        "Rotor_Blattlänge_l": 0.55,
        "Rotor_Durchmesser": 1.24,
        "Rotor_Max_Drehzahl": 1100,
        "Rotor_cd0": 0.0125
    },
    "Rotorblatt_NACA0009": {
        "Rotor_Profilart": "vollsymmetrisch",
        "Rotor_Profilname": "NACA0009",
        "Rotor_Anzahl": 2,
        "Rotor_Masse": 0.2,
        "Rotor_Blatttiefe_c": 0.048,
        "Rotor_Blattlänge_l": 0.55,
        "Rotor_Durchmesser": 1.24,
        "Rotor_Max_Drehzahl": 1500,
        "Rotor_cd0": 0.0125
    }
}
