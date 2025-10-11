import math
#from init_rotor_data import this_bat, this_model, this_rotor, this_physics
from main import this_battery, this_model, this_rotor, this_physics  

# Funktionen zu this.model
def takeoff_mass_kg():
    takeoff_mass_kg = this_model.net_mass_kg + this_battery.mass_kg
    print("Take-Off Mass:", takeoff_mass_kg, "kg")
    return takeoff_mass_kg

def getriebeübersetzung_motor_HZR():
    Gear_Ratio = this_model.zähne_HZR/this_model.zähne_motorritzel
    #print(Gear_Ratio)
    return Gear_Ratio

def tailrotor_rpm():
    tailrotor_rpm = getriebeübersetzung_motor_HZR()/this_model.getriebe_TR*this_rotor.drehzahl_rpm
    #print("Heckrotordrehzahl: " + str(round(tailrotor_rpm(), 1)), "RPM")
    return tailrotor_rpm

def tailrotor_frequenz():
    tailrotor_frequ = tailrotor_rpm()/60
    #print("Heckrotorfrequenz: " + str(round(tailrotor_frequenz(), 1)), "Hz")   
    return tailrotor_frequ

def Gewichtskraft():
    G = takeoff_mass_kg()*this_physics.g
    #print("Gewichtskraft: ", "\t", G, "N")
    return G





# Funktionen zu this.rotor
def rotor_radius_m():
    rotor_radius_m = this_rotor.durchmesser_m/2
    #print("Rotorradius = " ,rotor_radius_m, "m")
    return rotor_radius_m
    
def rotor_kreisumfang_m():
    rotor_kreisumfang_m = 2*math.pi*this_rotor.blattlänge_m
    #print("Rotorkreis Umfang ", rotor_kreisumfang_m, "m")
    return rotor_kreisumfang_m

def rotor_kreisfläche_m():
    rotor_kreisfläche = rotor_radius_m()**2*math.pi
    #print("Rotorkreisfläche: " ,rotor_kreisfläche, "m²")
    return rotor_kreisfläche

def rotor_speed_ms (): #Blattspitzengeschwindigkeit
    rotor_speed_ms = rotor_kreisumfang_m()*this_rotor.drehzahl_rpm/60
    #print(rotor_speed_ms)
    return rotor_speed_ms

def rotor_flächendichte_sigma(): #S.115
    Flächendichte = this_rotor.anzahl*this_rotor.blatttiefe_m/(math.pi*rotor_radius_m())
    #print(Flächendichte)
    return Flächendichte

def rotor_streckung():
    Streckung = this_rotor.blattlänge_m**2/(this_rotor.blatttiefe_m*this_rotor.blattlänge_m)
    #print(Streckung)
    return Streckung

def rotor_frequenz_hauptrotor_hz():
    Frequenz_Hauptrotor = this_rotor.drehzahl_rpm/60
    #print(Frequenz_Hauptrotor)
    return Frequenz_Hauptrotor


def rotor_omega_hauptrotor_rad():
    omega_Hauptrotor_rad = 2*math.pi*this_rotor.drehzahl_rpm/60
    #print(omega_Hauptrotor_rad)
    return omega_Hauptrotor_rad

def rotor_blattspitzengeschwindigkeit_omega_R_ms(): #S.370
    Blattspitzengeschwindigkeit_ms = rotor_omega_hauptrotor_rad()*rotor_radius_m()
    #print("Blattspitzengeschwindigkeit: " + str(round(Blattspitzengeschwindigkeit_ms,2)), "m/s" + "\t" + str(round ((Blattspitzengeschwindigkeit_ms*3.6), 2)) + "km/h")
    return Blattspitzengeschwindigkeit_ms

def rotor_blattlänge_r05():
    Blattlänge_r05 = 0.5*this_rotor.blattlänge_m
    return Blattlänge_r05

def rotor_speed_r05():
    speed_r05 = rotor_blattlänge_r05()*2*math.pi*rotor_frequenz_hauptrotor_hz()
    return speed_r05

def rotor_blattlänge_r075():
    Blattlänge_r075 = 0.75*this_rotor.blattlänge_m
    return Blattlänge_r075

def rotor_speed_r075():
    speed_r075 = rotor_blattlänge_r075()*2*math.pi*rotor_frequenz_hauptrotor_hz()
    return speed_r075

def rotor_flächenbelastung():
    Flächenbelastung = takeoff_mass_kg()/rotor_kreisfläche_m()
    #print("Flächenbelastung: " + str(round(Flächenbelastung,2)), "kg/m²")
    return Flächenbelastung

def rotor_reynoldszahl():
    reynoldszahl = rotor_speed_r075()*this_rotor.blatttiefe_m/this_physics.kinViskos
    #print("Reynoldszahl: " + str(round(reynoldszahl,0)))
    return reynoldszahl






# Rotorkopf-Drehzahlrechner
def Rotorkopfdrehzahl(Zellspannung_Last, Wirkungsgrad, Regleröffnung):
    calc_rotordrehzahl = this_battery.cells*Zellspannung_Last*this_model.motor_kV*this_model.zähne_motorritzel/this_model.zähne_HZR*Wirkungsgrad*Regleröffnung
    print("berechnete Rotorkopfdrehzahl: " , "\t", calc_rotordrehzahl, "RPM")
    return calc_rotordrehzahl

def Rotorkopfdrehzahl2(Zellspannung_Last, Wirkungsgrad, Regleröffnung, Bat_Zellen, Motor_kV, Zähne_Motorritzel, Zähne_Hauptzahnrad):
    calc_rotordrehzahl2 = Bat_Zellen*Zellspannung_Last*Motor_kV*Zähne_Motorritzel/Zähne_Hauptzahnrad*Wirkungsgrad*Regleröffnung
    print("berechnete Rotorkopfdrehzahl: " , "\t", calc_rotordrehzahl2, "RPM")
    return calc_rotordrehzahl2




# Funktionen zu Schwebeflugleistung:
def thrust_req_hover():
    thrust = takeoff_mass_kg()*this_physics.g
    #print("Benötigter Schub im Hover: ", "\t", thrust, "N")
    return thrust

def vi_induzierte_geschw_ST():
    vi= (thrust_req_hover()/(2*this_physics.Luftdichte_rho*rotor_kreisfläche_m()))**0.5
    #print("v_i: " + "\t",  vi, "m/s")
    return vi

def induzierter_Durchflussgrad_lambda_i(): #S.113
    lambda_i = vi_induzierte_geschw_ST()/(rotor_blattspitzengeschwindigkeit_omega_R_ms())
    #print("Induzierter Durchflussgrad lambda_i: " + "\t", lambda_i)
    return lambda_i

def induzierter_Durchflussgrad_lambda_hover():
    lambda_hover = (Schubbeiwert_CT()/2)**0.5
    #print("Induzierter Durchflussgrad im Hover: " + "\t", lambda_hover)
    return lambda_hover

def P0_Profilwiderstandsleistung():
    P0 = this_physics.Luftdichte_rho*rotor_kreisfläche_m()*rotor_blattspitzengeschwindigkeit_omega_R_ms()**3*rotor_flächendichte_sigma()*this_rotor.cd0/8
    #print("P0: " + "\t" , P0, "W")
    return P0

def CP0_Leistungsbeiwert():
    CP0 = rotor_flächendichte_sigma()/8*this_rotor.cd0
    #print("Leistungsbeiwert CP0: " + "\t" , CP0)
    return CP0

def Pi_induzierte_Leistung():
    P_i = thrust_req_hover()*vi_induzierte_geschw_ST()
    #print("Pi: ", "\t", P_i, "W")
    return P_i

def CP_i_korrigiert_Leistungsbeiwert(): #S.116
    #kappa = 1.15 empirischer Korrekturfaktor aufgr. Drallverluste etc.
    CP_i = this_physics.kappa_Korrektur*((Schubbeiwert_CT())**3/2)**0.5
    #print("Korrigierter induzierter Leistungsbeiwert CP_i :", "\t" , CP_i)
    return CP_i

def P_Gesamtleistung():
    P_Gesamt = P0_Profilwiderstandsleistung()+Pi_induzierte_Leistung()
    #print("P_Gesamt: ", "\t", P_Gesamt, "W")
    return P_Gesamt

def CP_Leistungsbeiwert():
    CP = CP0_Leistungsbeiwert()+CP_i_korrigiert_Leistungsbeiwert()
    #print("Leistungsbeiwert CP: ", "\t", CP)
    return CP

def Schubbeiwert_CT(): #S.113
    CT = Gewichtskraft()/(this_physics.Luftdichte_rho*rotor_kreisfläche_m()*rotor_blattspitzengeschwindigkeit_omega_R_ms()**2)
    #print("Schubbeiwert CT :", "\t" , CT)
    return CT

def CP_i_induzierter_Leistungsbeiwert(): #S.113
    CP_i = Schubbeiwert_CT()*induzierter_Durchflussgrad_lambda_i()
    #print("Induzierter Leistungsbeiwert CP_i :", "\t" , CP_i)
    return CP_i

#def Leistungsbeiwert_CP(): #S.113


def Leistungsgütegrad_FM():
    FM = thrust_req_hover()*vi_induzierte_geschw_ST()/(this_physics.kappa_Korrektur*thrust_req_hover()*vi_induzierte_geschw_ST()+P0_Profilwiderstandsleistung())
    #print("Leistungsgütegrad FM: ", "\t", FM)
    return FM


def Drehmomentbeiwert_CQ():
    CQ = rotor_flächendichte_sigma()*this_rotor.cd0/8+((Schubbeiwert_CT()**3)/2)**0.5
    #print("Drehmomentenbeiwert CQ: " , "\t", CQ)
    return CQ

def Schwebeflugleistung_P():
    P_Hover = Drehmomentbeiwert_CQ()*this_physics.Luftdichte_rho*rotor_kreisfläche_m()*(rotor_speed_ms())**3
    #print("Schwebeflugleistung_P_Hover: ", "\t", P_Hover , "W")
    return P_Hover

def Gegendrehmoment_Q():
    Q = P_Gesamtleistung()/rotor_omega_hauptrotor_rad()
    #print("Gegendrehmoment Q: ", "\t", Q, "Nm")
    return Q

def Heckrotorschub_T_TR():
    T_TR = Gegendrehmoment_Q()/this_model.tailrotor_hebelarm_m
    #print("Heckrotorschub T_TR: ", "\t", T_TR, "N")
    return T_TR





# Blattelementetheorie

# Blattspitzenverluste

def einfacher_Blattspitzenverlust():
    B = 1-((Schubbeiwert_CT())**0.5)/this_rotor.anzahl
    #print("Einfacher Blattspitzenverlust: ", "\t", B)
    return B

def Wheatley_Blattspitzenverslust():
    B_Wheatley = 1-this_rotor.blatttiefe_m/(2*rotor_radius_m())
    #print("Wheatley Blattspitzenverlust: ", "\t", B_Wheatley)
    return B_Wheatley




# Funktionen Auswertung
def Header():
    print("Gewähltes Modell:" + "\t" + this_model.brand, this_model.model)
    print("Gewähltes Profil:" + "\t" + this_rotor.profilname)
    print("Rotordrehzahl:" + "\t" + "\t" + str(this_rotor.drehzahl_rpm), "RPM" + "\t" + str(rotor_frequenz_hauptrotor_hz()), "Hz" + "\t" + "Blattspitzengeschwindigkeit:" + "\t" + str(round(rotor_blattspitzengeschwindigkeit_omega_R_ms(),2)), "m/s" + "\t" + str(round ((rotor_blattspitzengeschwindigkeit_omega_R_ms()*3.6), 2)) + "km/h")
    print("Heckrotordrehzahl:" +"\t" +  str(round(tailrotor_rpm(), 1)), "RPM" + "\t" + str(round(tailrotor_frequenz(), 1)), "Hz")
    print("------------------------------------------------------------------------------------------------------------------------------------------")
