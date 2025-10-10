from data_models import List_Models
from functions import *

def start_cli():
    print("🚁 Willkommen zum Rotor-Simulator CLI")
    global aktuelles_modell
    aktuelles_modell = List_Models[0]  # Standardmodell

    while True:
        print("\nBefehle:")
        print("1 - Modell anzeigen")
        print("2 - Modell wechseln")
        print("3 - Leistung berechnen")
        print("4 - Hilfe")
        print("q - Beenden")

        cmd = input("Eingabe: ").strip().lower()

        if cmd == "1":
            print("Aktuelles Modell:", aktuelles_modell)
        elif cmd == "2":
            print("Verfügbare Modelle:", list(List_Models.keys()))
            wahl = input("Modellname: ")
            if wahl in List_Models:
                
                aktuelles_modell = List_Models[wahl]
                print(f"{wahl} ausgewählt.")
            else:
                print("Modell nicht gefunden.")
        elif cmd == "3":
            print("Führe Berechnung für", aktuelles_modell.model, "durch...")
        elif cmd == "4":
            print("Hilfe")
        elif cmd == "q":
            print("Programm beendet.")
            break
        else:
            print("Ungültiger Befehl.")
