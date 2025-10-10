from classes import Battery

List_Batteries = {
    "TURNIGY5000": Battery(
        name = "Turnigy 5000mAh 6S",
        brand= "Turnigy",
        type= "Lipo",
        volt_per_cell_nominal= 3.7, #V
        volt_per_cell_load= 3.1,
        volt= 22.2,
        länge_mm= 320,
        breite_mm= 46,
        höhe_mm= 51,
        cells= 6,
        capacity_Wh= 230.88,
        capacity_usable_Wh= 184.7,
        mass_kg= 1.5
    ),
    "TATTU6000": Battery(
        name= "Tattu 6000mAh 6S",
        brand= "Tattu",
        type= "Lipo",
        volt_per_cell_nominal= 3.7,
        volt_per_cell_load= 3.2,
        volt= 22.2,
        länge_mm= 138,
        breite_mm= 42,
        höhe_mm= 70,
        cells= 6,
        capacity_Wh= 222.0,
        capacity_usable_Wh= 177.6,
        mass_kg= 1.3
    )
}
