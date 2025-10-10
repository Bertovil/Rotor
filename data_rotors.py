from classes import Mainrotor

List_Rotors = {
    "E182": Mainrotor(
        profilart= "S-Schlag",
        profilname= "E182_Test",
        anzahl= 2,
        masse_kg= 0.2,
        blatttiefe_m= 0.048,
        blattlänge_m= 0.55,
        durchmesser_m= 1.24,
        max_drehzahl_rpm= 1100,
        cd0= 0.0125
    ),
    "NACA0009": Mainrotor(
        profilart= "vollsymmetrisch",
        profilname= "NACA0009",
        anzahl= 2,
        masse_kg= 0.2,
        blatttiefe_m= 0.048,
        blattlänge_m= 0.55,
        durchmesser_m= 1.24,
        max_drehzahl_rpm= 1500,
        cd0= 0.0125
    )
}
