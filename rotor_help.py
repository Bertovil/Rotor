
import inspect
import functions  # dein Modul importieren
print("Verfügbare Funktionen:")
print("---------------------")  

# Alle Funktionen im Modul auflisten
funktionen = inspect.getmembers(functions, inspect.isfunction)

for name, func in funktionen:
    print(f"- {name}")



'''import functions
help(functions)'''
