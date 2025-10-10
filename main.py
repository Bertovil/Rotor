import argparse
import shlex
import readline
import os
import atexit
from difflib import get_close_matches

# Datenquellen importieren
from data_models import List_Models
from data_batteries import List_Batteries
from data_rotors import List_Rotors
from data_physics import List_Physics

def verarbeite_befehl(eingabe):
    parser = argparse.ArgumentParser(prog="RotorShell", add_help=False)

    # Optionen definieren
    parser.add_argument("--model", type=str)
    parser.add_argument("--show", choices=["param", "all"])
    parser.add_argument("--battery", type=str)
    parser.add_argument("--rotor", type=str)
    parser.add_argument("--physik", type=str)
    parser.add_argument("--calc", action="store_true")
    parser.add_argument("--simulate", action="store_true")
    parser.add_argument("--export", action="store_true")
    parser.add_argument("--compare", nargs="+")
    parser.add_argument("--help", action="store_true")

    try:
        args = parser.parse_args(shlex.split(eingabe))
    except SystemExit:
        print("❌ Ungültige Eingabe. Gib '--help' ein für Optionen.")
        return

    # Hilfe anzeigen
    if args.help:
        print("\n📘 Verfügbare Optionen:")
        print("--model <NAME>         – Wähle ein Modell")
        print("--show param|all       – Zeige Modellparameter oder vollständigen Datensatz")
        print("--battery <NAME>       – Wähle eine Batterie")
        print("--rotor <NAME>         – Wähle ein Rotorblatt")
        print("--physik <NAME>        – Wähle physikalische Umgebung")
        print("--calc                 – Starte Dummy-Berechnung")
        print("--simulate             – Starte Dummy-Simulation")
        print("--export               – Exportiere Daten (Dummy)")
        print("--compare <A> <B> ...  – Vergleiche Modelle (Dummy)")
        print("--help                 – Zeigt diese Hilfe")
        return

    # Modell auswählen
    modell = None
    if args.model:
        modellname = args.model.upper()
        modell = List_Models.get(modellname)
        if not modell:
            print(f"❌ Modell '{args.model}' nicht gefunden.")
            vorschläge = get_close_matches(modellname, List_Models.keys())
            if vorschläge:
                print("🔍 Meintest du vielleicht:")
                for v in vorschläge:
                    print(f"- {v}")
            else:
                print("📦 Verfügbare Modelle:")
                for name in List_Models:
                    print(f"- {name}")
            return
    else:
        print("❌ Kein Modell angegeben. 📦 Verfügbare Modelle:")
        for name in List_Models:
            print(f"- {name}")
        return

    # Anzeigeoptionen
    if args.show == "param":
        print(f"\n📘 Parameter von {modell['model']}:")
        for key, value in modell.items():
            print(f"{key}: {value}")
    elif args.show == "all":
        print(f"\n📦 Vollständiger Datensatz für {modell['model']}:")
        print(modell)

    # Batterie auswählen
    if args.battery:
        battery = List_Batteries.get(args.battery.upper())
        if battery:
            print(f"\n🔋 Batterie '{battery['name']}' ausgewählt:")
            for k, v in battery.items():
                print(f"{k}: {v}")
        else:
            print(f"❌ Batterie '{args.battery}' nicht gefunden.")
            print("Verfügbare Batterien:")
            for name in List_Batteries:
                print(f"- {name}")

    # Rotor auswählen
    if args.rotor:
        rotor = List_Rotors.get(args.rotor.upper())
        if rotor:
            print(f"\n🌀 Rotor '{rotor['profil']}' ausgewählt:")
            for k, v in rotor.items():
                print(f"{k}: {v}")
        else:
            print(f"❌ Rotor '{args.rotor}' nicht gefunden.")
            print("Verfügbare Rotoren:")
            for name in List_Rotors:
                print(f"- {name}")

    # Physik auswählen
    if args.physik:
        physik = List_Physics.get(args.physik.upper())
        if physik:
            print(f"\n⚙️ Physikprofil '{args.physik.upper()}' ausgewählt:")
            for k, v in physik.items():
                print(f"{k}: {v}")
        else:
            print(f"❌ Physikprofil '{args.physik}' nicht gefunden.")
            print("Verfügbare Physikprofile:")
            for name in List_Physics:
                print(f"- {name}")

    # Dummy-Funktionen
    if args.calc:
        print("⚙️ Dummy-Berechnung gestartet… (noch nicht implementiert)")
    if args.simulate:
        print("🎮 Dummy-Simulation gestartet… (noch nicht implementiert)")
    if args.export:
        print("📤 Dummy-Export durchgeführt… (noch nicht implementiert)")
    if args.compare:
        print(f"📊 Dummy-Vergleich gestartet für: {', '.join(args.compare)}")

def start_shell():
    print("🚁 Willkommen im RotorShell-Modus mit Eingabeverlauf")
    print("Gib '--help' ein für verfügbare Optionen.")
    print("Gib 'exit' ein zum Beenden.")

    while True:
        try:
            eingabe = input("\n📝 Befehl: ").strip()
            if eingabe.lower() == "exit":
                print("👋 Bis bald!")
                break
            verarbeite_befehl(eingabe)
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Bis bald!")
            break

if __name__ == "__main__":
    start_shell()
