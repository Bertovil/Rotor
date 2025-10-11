import argparse
import shlex
import readline
import os
import atexit
from difflib import get_close_matches
import inspect

import classes
import functions2
from utils import function_groups

from data_models import List_Models
from data_batteries import List_Batteries
from data_rotors import List_Rotors
from data_physics import List_Physics

# Alle verfügbaren Funktionen aus functions2
available_functions = [
    name for name, func in inspect.getmembers(functions2, inspect.isfunction)
    if not name.startswith("_")
]

def completer(text, state):
    buffer = readline.get_line_buffer()
    line = buffer.strip()

    # Nur das letzte Wort betrachten
    words = line.split()
    if not words:
        return None

    last = words[-1]
    options = []

    if "--calc" in words:
        prefix = last if line.endswith(last) else ""
        options = [name for name in available_functions if name.startswith(prefix)]
    elif "--help" in words:
        prefix = last if line.endswith(last) else ""
        options = [name for name in available_functions if name.startswith(prefix)]

    if state < len(options):
        return options[state]
    return None


def verarbeite_befehl(eingabe):
    this_model = None
    this_battery = None
    this_rotor = None
    this_physics = None

    parser = argparse.ArgumentParser(prog="RotorShell", add_help=False)
    parser.add_argument("--model", type=str)
    parser.add_argument("--show", choices=["param", "all"])
    parser.add_argument("--battery", type=str)
    parser.add_argument("--rotor", type=str)
    parser.add_argument("--physics", type=str)
    parser.add_argument("--calc", type=str, help="Name der Berechnungsfunktion oder 'list'")
    parser.add_argument("--simulate", action="store_true")
    parser.add_argument("--export", action="store_true")
    parser.add_argument("--compare", nargs="+")
    parser.add_argument("--help", nargs="?", const="__general__", type=str)

    try:
        args = parser.parse_args(shlex.split(eingabe))
    except SystemExit:
        print("❌ Ungültige Eingabe. Gib '--help' ein für Optionen.")
        return

    # Hilfe anzeigen
    if args.help:
        if args.help == "__general__":
            print("\n📘 Verfügbare Optionen:")
            print("--model <NAME>         – Wähle ein Modell")
            print("--show param|all       – Zeige Modellparameter oder vollständigen Datensatz")
            print("--battery <NAME>       – Wähle eine Batterie")
            print("--rotor <NAME>         – Wähle ein Rotorblatt")
            print("--physics <NAME>       – Wähle physikalische Umgebung")
            print("--calc <FUNKTION|list> – Berechnung ausführen oder Liste anzeigen")
            print("--simulate             – Starte Dummy-Simulation")
            print("--export               – Exportiere Daten (Dummy)")
            print("--compare <A> <B> ...  – Vergleiche Modelle (Dummy)")
            print("--help [FUNKTION]      – Zeigt diese Hilfe oder Beschreibung zu einer Berechnungsfunktion")
            return
        else:
            func_name = args.help.strip()
            found = False
            for group, funcs in function_groups.items():
                if func_name in funcs:
                    print(f"\nℹ️ Funktion: {func_name}")
                    print(f"Beschreibung: {funcs[func_name]}")
                    print(f"Gruppe: {group}")
                    found = True
                    break
            if not found:
                print(f"❌ Keine Beschreibung für '{func_name}' gefunden.")
            return

    # Sonderfall: --calc list
    if args.calc and args.calc.lower() == "list":
        print("\n📘 Verfügbare Berechnungsfunktionen:")
        for group, funcs in function_groups.items():
            print(f"\n{group}")
            for name, desc in funcs.items():
                if hasattr(functions2, name):
                    print(f"- {name}: {desc}")
        return

    # Modell auswählen
    if args.model:
        modellname = args.model.upper()
        modell = List_Models.get(modellname)
        if modell:
            this_model = modell
        else:
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

    # Anzeigeoptionen
    if args.show == "param":
        print(f"\n📘 Parameter von {modell}:")
        modell.info()
    elif args.show == "all":
        print(f"\n📦 Vollständiger Datensatz für {modell}:")
        print(modell)

    # Batterie auswählen
    if args.battery:
        battery = List_Batteries.get(args.battery.upper())
        if battery:
            this_battery = battery
            print(f"\n🔋 Batterie '{battery.brand} {battery.type}' ausgewählt:")
            battery.info()
        else:
            print(f"❌ Batterie '{args.battery}' nicht gefunden.")
            print("Verfügbare Batterien:")
            for name in List_Batteries:
                print(f"- {name}")

    # Rotor auswählen
    if args.rotor:
        rotor = List_Rotors.get(args.rotor.upper())
        if rotor:
            this_rotor = rotor
            print(f"\n🌀 Rotor '{rotor.profilname}' ausgewählt:")
            rotor.info()
        else:
            print(f"❌ Rotor '{args.rotor}' nicht gefunden.")
            print("Verfügbare Rotoren:")
            for name in List_Rotors:
                print(f"- {name}")

    # Physik auswählen
    if args.physics:
        physics = List_Physics.get(args.physics.upper())
        if physics:
            this_physics = physics
            print(f"\n⚙️ Physikprofil '{args.physics.upper()}' ausgewählt:")
            physics.info()
        else:
            print(f"❌ Physikprofil '{args.physics}' nicht gefunden.")
            print("Verfügbare Physikprofile:")
            for name in List_Physics:
                print(f"- {name}")

    # Berechnung ausführen
    if args.calc and args.calc.lower() != "list":
        func_name = args.calc
        if not this_model or not this_rotor or not this_battery or not this_physics:
            print("❌ Bitte wähle Modell, Rotor, Batterie und Physikprofil aus.")
            return

        if hasattr(functions2, func_name):
            func = getattr(functions2, func_name)
            try:
                result = func(this_model, this_rotor, this_battery, this_physics)
                print(f"✅ Ergebnis von {func_name}(): {result}")
            except TypeError as e:
                print(f"⚠️ Fehler beim Aufruf von {func_name}(): {e}")
                print("Stelle sicher, dass die Funktion genau 4 Parameter erwartet: model, rotor, battery, physics.")
        else:
            print(f"❌ Funktion '{func_name}' nicht gefunden in functions2.py.")

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

    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")

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
