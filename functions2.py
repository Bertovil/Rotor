import math

def takeoff_mass_kg(model, rotor, battery, physics):
    return model.net_mass_kg + battery.mass_kg

def getriebeübersetzung_motor_HZR(model, rotor, battery, physics):
    return model.zähne_HZR / model.zähne_motorritzel

def tailrotor_rpm(model, rotor, battery, physics):
    return getriebeübersetzung_motor_HZR(model, rotor, battery, physics) / model.getriebe_TR * rotor.drehzahl_rpm

def tailrotor_frequenz(model, rotor, battery, physics):
    return tailrotor_rpm(model, rotor, battery, physics) / 60

def Gewichtskraft(model, rotor, battery, physics):
    return takeoff_mass_kg(model, rotor, battery, physics) * physics.g

def rotor_radius_m(model, rotor, battery, physics):
    return rotor.durchmesser_m / 2

def rotor_kreisumfang_m(model, rotor, battery, physics):
    return 2 * math.pi * rotor.blattlänge_m

def rotor_kreisfläche_m(model, rotor, battery, physics):
    return rotor_radius_m(model, rotor, battery, physics) ** 2 * math.pi

def rotor_speed_ms(model, rotor, battery, physics):
    return rotor_kreisumfang_m(model, rotor, battery, physics) * rotor.drehzahl_rpm / 60

def rotor_flächendichte_sigma(model, rotor, battery, physics):
    return rotor.anzahl * rotor.blatttiefe_m / (math.pi * rotor_radius_m(model, rotor, battery, physics))

def rotor_streckung(model, rotor, battery, physics):
    return rotor.blattlänge_m / rotor.blatttiefe_m

def rotor_frequenz_hauptrotor_hz(model, rotor, battery, physics):
    return rotor.drehzahl_rpm / 60

def rotor_omega_hauptrotor_rad(model, rotor, battery, physics):
    return 2 * math.pi * rotor.drehzahl_rpm / 60

def rotor_blattspitzengeschwindigkeit_omega_R_ms(model, rotor, battery, physics):
    return rotor_omega_hauptrotor_rad(model, rotor, battery, physics) * rotor_radius_m(model, rotor, battery, physics)

def rotor_blattlänge_r(model, rotor, battery, physics, faktor):
    return faktor * rotor.blattlänge_m

def rotor_speed_r(model, rotor, battery, physics, faktor):
    return rotor_blattlänge_r(model, rotor, battery, physics, faktor) * 2 * math.pi * rotor_frequenz_hauptrotor_hz(model, rotor, battery, physics)

def rotor_flächenbelastung(model, rotor, battery, physics):
    return takeoff_mass_kg(model, rotor, battery, physics) / rotor_kreisfläche_m(model, rotor, battery, physics)

def rotor_reynoldszahl(model, rotor, battery, physics):
    return rotor_speed_r(model, rotor, battery, physics, 0.75) * rotor.blatttiefe_m / physics.kinViskos

def Rotorkopfdrehzahl(model, rotor, battery, physics, Zellspannung_Last, Wirkungsgrad, Regleröffnung):
    return battery.cells * Zellspannung_Last * model.motor_kV * model.zähne_motorritzel / model.zähne_HZR * Wirkungsgrad * Regleröffnung

def thrust_req_hover(model, rotor, battery, physics):
    return Gewichtskraft(model, rotor, battery, physics)

def vi_induzierte_geschw_ST(model, rotor, battery, physics):
    return math.sqrt(thrust_req_hover(model, rotor, battery, physics) / (2 * physics.Luftdichte_rho * rotor_kreisfläche_m(model, rotor, battery, physics)))

def induzierter_Durchflussgrad_lambda_i(model, rotor, battery, physics):
    return vi_induzierte_geschw_ST(model, rotor, battery, physics) / rotor_blattspitzengeschwindigkeit_omega_R_ms(model, rotor, battery, physics)

def Schubbeiwert_CT(model, rotor, battery, physics):
    return Gewichtskraft(model, rotor, battery, physics) / (physics.Luftdichte_rho * rotor_kreisfläche_m(model, rotor, battery, physics) * rotor_blattspitzengeschwindigkeit_omega_R_ms(model, rotor, battery, physics) ** 2)

def P0_Profilwiderstandsleistung(model, rotor, battery, physics):
    return physics.Luftdichte_rho * rotor_kreisfläche_m(model, rotor, battery, physics) * rotor_blattspitzengeschwindigkeit_omega_R_ms(model, rotor, battery, physics) ** 3 * rotor_flächendichte_sigma(model, rotor, battery, physics) * rotor.cd0 / 8

def CP0_Leistungsbeiwert(model, rotor, battery, physics):
    return rotor_flächendichte_sigma(model, rotor, battery, physics) / 8 * rotor.cd0

def Pi_induzierte_Leistung(model, rotor, battery, physics):
    return thrust_req_hover(model, rotor, battery, physics) * vi_induzierte_geschw_ST(model, rotor, battery, physics)

def CP_i_korrigiert_Leistungsbeiwert(model, rotor, battery, physics):
    CT = Schubbeiwert_CT(model, rotor, battery, physics)
    return physics.kappa_Korrektur * math.sqrt((CT ** 3) / 2)

def P_Gesamtleistung(model, rotor, battery, physics):
    return P0_Profilwiderstandsleistung(model, rotor, battery, physics) + Pi_induzierte_Leistung(model, rotor, battery, physics)

def CP_Leistungsbeiwert(model, rotor, battery, physics):
    return CP0_Leistungsbeiwert(model, rotor, battery, physics) + CP_i_korrigiert_Leistungsbeiwert(model, rotor, battery, physics)

def Leistungsgütegrad_FM(model, rotor, battery, physics):
    vi = vi_induzierte_geschw_ST(model, rotor, battery, physics)
    return thrust_req_hover(model, rotor, battery, physics) * vi / (physics.kappa_Korrektur * thrust_req_hover(model, rotor, battery, physics) * vi + P0_Profilwiderstandsleistung(model, rotor, battery, physics))

def Drehmomentbeiwert_CQ(model, rotor, battery, physics):
    CT = Schubbeiwert_CT(model, rotor, battery, physics)
    return rotor_flächendichte_sigma(model, rotor, battery, physics) * rotor.cd0 / 8 + math.sqrt((CT ** 3) / 2)

def Schwebeflugleistung_P(model, rotor, battery, physics):
    return Drehmomentbeiwert_CQ(model, rotor, battery, physics) * physics.Luftdichte_rho * rotor_kreisfläche_m(model, rotor, battery, physics) * rotor_speed_ms(model, rotor, battery, physics) ** 3

def Gegendrehmoment_Q(model, rotor, battery, physics):
    return P_Gesamtleistung(model, rotor, battery, physics) / rotor_omega_hauptrotor_rad(model, rotor, battery, physics)

def Heckrotorschub_T_TR(model, rotor, battery, physics):
    return Gegendrehmoment_Q(model, rotor, battery, physics) / model.tailrotor_hebelarm_m

def einfacher_Blattspitzenverlust(model, rotor, battery, physics):
    return 1 - math.sqrt(Schubbeiwert_CT(model, rotor, battery, physics)) / rotor.anzahl

def Wheatley_Blattspitzenverlust(model, rotor, battery, physics):
    return 1 - rotor.blatttiefe_m / (2 * rotor_radius_m(model, rotor, battery, physics))

def Header(model, rotor, battery, physics):
    print("Modell:", model.brand, model.model)
    print("Profil:", rotor.profilname)
    print("Rotordrehzahl:", rotor.drehzahl_rpm, "RPM")
    print("Blattspitzengeschwindigkeit:", round(rotor_blattspitzengeschwindigkeit_omega_R_ms(model, rotor, battery, physics), 2), "m/s")
    print("Heckrotordrehzahl:", round(tailrotor_rpm(model, rotor, battery, physics), 1), "RPM")
