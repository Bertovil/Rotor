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
        drehzahl_rpm= 1100,
        cd0= 0.0125
    ),
    "NACA0009": Mainrotor(
        profilart= "vollsymmetrisch",
        profilname= "NACA0009",
        anzahl= 4,
        masse_kg= 0.2,
        blatttiefe_m= 0.049,
        blattlänge_m= 0.58,
        durchmesser_m= 1.26,
        drehzahl_rpm= 1500,
        cd0= 0.012
    )
}
