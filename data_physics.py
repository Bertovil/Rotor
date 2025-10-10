'''#Dictionaries mit Startwerten - bei Änderung einmal ausführen

Erde ={
    "g": 9.80665, #m/s²
    "dynamische Viskosität": 17.20, # *10^-6*kg/m*s
    "kinematische Viskosität": 0.00001331, # m²/s
    "T": 288.15, #K
    "Dichte": 1.225, #kg/m³
    "Altitude": 0, #m
    "kappa_Korrektur": 1.15 # Korrekturfaktor S. 116
}

Mond ={
    "g": 1.625, #m/s²
    "dynamische Viskosität": 0.0, # *10^-6*kg/m*s
    "kinematische Viskosität": 0.0, # m²/s
    "T": 220, #K
    "Dichte": 0.0, #kg/m³
    "Altitude": 0, #m
    "kappa_Korrektur": 1.0 # Korrekturfaktor S
}

Mars ={
    "g": 3.72076, #m/s²
    "dynamische Viskosität": 13.0, # *10^-6*kg/m*s
    "kinematische Viskosität": 0.0000064, # m²/s
    "T": 210, #K
    "Dichte": 0.02, #kg/m³
    "Altitude": 0, #m
    "kappa_Korrektur": 1.15 # Korrekturfaktor S. 116
}

Jupiter ={
    "g": 24.79, #m/s²
    "dynamische Viskosität": 0.0, # *10^-6*kg/m*s
    "kinematische Viskosität": 0.0, # m²/s
    "T": 165, #K
    "Dichte": 0.16, #kg/m³
    "Altitude": 0, #m
    "kappa_Korrektur": 1.0 # Korrekturfaktor S
}

Saturn ={
    "g": 10.44, #m/s²
    "dynamische Viskosität": 0.0, # *10^-6*kg/m*s
    "kinematische Viskosität": 0.0, # m²/s
    "T": 134, #K
    "Dichte": 0.19, #kg/m³
    "Altitude": 0, #m
    "kappa_Korrektur": 1.0 # Korrekturfaktor S
}'''

List_Physics = {
    "Erde": {
        "g": 9.80665,
        "dynamische Viskosität": 17.20,
        "kinematische Viskosität": 0.00001331,
        "T": 288.15,
        "Dichte": 1.225,
        "Altitude": 0,
        "kappa_Korrektur": 1.15
    },
    "Mond": {
        "g": 1.625,
        "dynamische Viskosität": 0.0,
        "kinematische Viskosität": 0.0,
        "T": 220,
        "Dichte": 0.0,
        "Altitude": 0,
        "kappa_Korrektur": 1.0
    },
    "Mars": {
        "g": 3.72076,
        "dynamische Viskosität": 13.0,
        "kinematische Viskosität": 0.0000064,
        "T": 210,
        "Dichte": 0.02,
        "Altitude": 0,
        "kappa_Korrektur": 1.15
    },
    "Jupiter": {
        "g": 24.79,
        "dynamische Viskosität": 0.0,
        "kinematische Viskosität": 0.0,
        "T": 165,
        "Dichte": 0.16,
        "Altitude": 0,
        "kappa_Korrektur": 1.0
    },
    "Saturn": {
        "g": 10.44,
        "dynamische Viskosität": 0.0,
        "kinematische Viskosität": 0.0,
        "T": 134,
        "Dichte": 0.19,
        "Altitude": 0,
        "kappa_Korrektur": 1.0
    }
}
