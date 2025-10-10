'''#Dictionaries mit Startwerten - bei Änderung einmal ausführen


LOGO600SX ={

    "brand": "Mikado",
    "model": "LOGO 600 SX",
    "net_mass": 2.7, #kg
    "Typical_TOM": 4.0, #kg
    "Länge": 1.60, #m
    "Breite": 1.24, #m
    "Höhe": 0.4, #m

    "Zähne_HZR": 106,
    "Zähne_Motorritzel":11,
    "Getriebe_TR": 4.56,

    "Motor_name": "Hacker Turnado A50-8S",
    "Motor_kV": 850,

    "Tailrotor_Hebelarm_m": 0.5
    
}

ALIGN_TREX600 ={
    "brand": "Align",
    "model": "T-REX 600",
    "net_mass": 2.9, #kg
    "Typical_TOM": 4.2, #kg
    "Länge": 1.65, #m
    "Breite": 1.24, #m
    "Höhe": 0.4, #m

    "Zähne_HZR": 106,
    "Zähne_Motorritzel":15,
    "Getriebe_TR": 4.9,

    "Motor_name": "Scorpion HKIII-4025-520",
    "Motor_kV": 520,

    "Tailrotor_Hebelarm_m": 0.5
    
}

List_Models =[LOGO600SX, ALIGN_TREX600]
'''

List_Models = {
    "LOGO600SX": {
        "brand": "Mikado",
        "model": "LOGO 600 SX",
        "net_mass": 2.7,
        "Typical_TOM": 4.0,
        "Länge": 1.60,
        "Breite": 1.24,
        "Höhe": 0.4,
        "Zähne_HZR": 106,
        "Zähne_Motorritzel": 11,
        "Getriebe_TR": 4.56,
        "Motor_name": "Hacker Turnado A50-8S",
        "Motor_kV": 850,
        "Tailrotor_Hebelarm_m": 0.5
    },
    "ALIGN_TREX600": {
        "brand": "Align",
        "model": "T-REX 600",
        "net_mass": 2.9,
        "Typical_TOM": 4.2,
        "Länge": 1.65,
        "Breite": 1.24,
        "Höhe": 0.4,
        "Zähne_HZR": 106,
        "Zähne_Motorritzel": 15,
        "Getriebe_TR": 4.9,
        "Motor_name": "Scorpion HKIII-4025-520",
        "Motor_kV": 520,
        "Tailrotor_Hebelarm_m": 0.5
    }
}
