class Model:
    def __init__(self, brand, model, net_mass_kg, typical_TOM_kg, länge_m, breite_m, höhe_m, zähne_HZR, zähne_motorritzel, getriebe_TR, motor_name, motor_kV, tailrotor_hebelarm_m):
        self.brand = brand
        self.model = model
        self.net_mass_kg = net_mass_kg
        self.typical_TOM_kg = typical_TOM_kg
        self.länge_m = länge_m
        self.breite_m = breite_m
        self.höhe_m = höhe_m
        self.zähne_HZR = zähne_HZR
        self.zähne_motorritzel = zähne_motorritzel
        self.getriebe_TR = getriebe_TR
        self.motor_name = motor_name
        self.motor_kV = motor_kV
        self.tailrotor_hebelarm_m = tailrotor_hebelarm_m
  
    #Spezialfunktionen und Berechnungen
    def getriebeübersetzung_motor_HZR(self):
        Gear_Ratio = self.zähne_HZR/self.zähne_motorritzel
        #print(Gear_Ratio)
        return Gear_Ratio
    
    def info(self):
        print("Modell: ", self.brand, self.model)
        print("Netto Masse: ", self.net_mass_kg, "kg")
        print("Typische Abflugmasse: ", self.typical_TOM_kg, "kg")
        print("Länge: ", self.länge_m, "m")
        print("Breite: ", self.breite_m, "m")
        print("Höhe: ", self.höhe_m, "m")
        print("Zähne Hauptzahnrad: ", self.zähne_HZR)
        print("Zähne Motorritzel: ", self.zähne_motorritzel)
        print("Getriebeübersetzung: ", self.getriebeübersetzung_motor_HZR())
        print("Motor: ", self.motor_name)
        print("Motor kV: ", self.motor_kV, "kV")
        print("Hebelarm Heckrotor: ", self.tailrotor_hebelarm_m, "m")

class Mainrotor:
    def __init__(self, profilart, profilname, anzahl, masse_kg, blatttiefe_m, blattlänge_m, durchmesser_m, drehzahl_rpm, cd0):
        self.profilart = profilart
        self.profilname = profilname
        self.anzahl = anzahl
        self.masse_kg = masse_kg
        self.blatttiefe_m = blatttiefe_m
        self.blattlänge_m = blattlänge_m
        self.durchmesser_m = durchmesser_m
        self.drehzahl_rpm = drehzahl_rpm
        self.cd0 = cd0

    def info(self):
        print("Rotor: ", self.profilart, self.profilname)
        print("Anzahl Blätter: ", self.anzahl)
        print("Masse: ", self.masse_kg, "kg")
        print("Blatttiefe: ", self.blatttiefe_m, "m")
        print("Blattlänge: ", self.blattlänge_m, "m")
        print("Durchmesser: ", self.durchmesser_m, "m")
        print("MDrehzahl: ", self.drehzahl_rpm, "RPM")
        print("CD0: ", self.cd0)


class Battery:
    def __init__(self, name, brand, type, volt_per_cell_nominal, volt_per_cell_load, volt, länge_mm, breite_mm, höhe_mm, cells, capacity_Wh, capacity_usable_Wh, mass_kg):
        self.name = name
        self.brand = brand
        self.type = type
        self.volt_per_cell_nominal = volt_per_cell_nominal
        self.volt_per_cell_load = volt_per_cell_load
        self.volt = volt
        self.länge_mm = länge_mm
        self.breite_mm = breite_mm
        self.höhe_mm = höhe_mm
        self.cells = cells
        self.capacity_Wh = capacity_Wh
        self.capacity_usable_Wh = capacity_usable_Wh
        self.mass_kg = mass_kg

    def info(self):
        print("Batterie: ", self.name)
        print("Batterie: ", self.brand, self.type)
        print("Zellenspannung unbelastet: ", self.volt_per_cell_nominal, "V")
        print("Zellenspannung unter Last: ", self.volt_per_cell_load, "V")
        print("Spannung: ", self.volt, "V")
        print("Länge: ", self.länge_mm, "mm")
        print("Breite: ", self.breite_mm, "mm")
        print("Höhe: ", self.höhe_mm, "mm")
        print("Anzahl Zellen: ", self.cells)
        print("Kapazität: ", self.capacity_Wh, "Wh")
        print("Nutzbare Kapazität: ", self.capacity_usable_Wh, "Wh")
        print("Masse: ", self.mass_kg, "kg")

class Physics:
    def __init__(self, g, dynViskos, kinViskos, T, Luftdichte_rho, altitude, kappa_Korrektur):
        self.g = g
        self.dynViskos = dynViskos
        self.kinViskos = kinViskos
        self.T = T
        self.Luftdichte_rho = Luftdichte_rho
        self.altitude = altitude
        self.kappa_Korrektur = kappa_Korrektur

    def info(self):
        print("Erdbeschleunigung g: ", self.g, "m/s²")
        print("Dynamische Viskosität: ", self.dynViskos, "Ns/m²")
        print("Kinematische Viskosität: ", self.kinViskos, "m²/s")
        print("Temperatur: ", self.T, "K")
        print("Luftdichte: ", self.Luftdichte_rho, "kg/m³")
        print("Höhe über NN: ", self.altitude, "m")
        print("Korrekturfaktor kappa: ", self.kappa_Korrektur)
