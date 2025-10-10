from classes import Physics

List_Physics = { 
    "ERDE": Physics(
        g= 9.80665,
        dynViskos= 17.20,
        kinViskos= 0.00001331,
        T= 288.15,
        Luftdichte_rho= 1.225,
        altitude= 0,
        kappa_Korrektur= 1.15
    ),
    "MOND": Physics(    
        g= 1.625,
        dynViskos= 0.0,
        kinViskos= 0.0,
        T= 220,
        Luftdichte_rho= 0.0,
        altitude= 0,
        kappa_Korrektur= 1.0
    ),
    "MARS": Physics(
        g= 3.72076,
        dynViskos= 13.0,
        kinViskos= 0.0000064,
        T= 210,
        Luftdichte_rho= 0.02,
        altitude= 0,
        kappa_Korrektur= 1.15
    ),
    "JUPITER": Physics(
        g= 24.79,
        dynViskos= 0.0,
        kinViskos= 0.0,
        T= 165,
        Luftdichte_rho= 0.16,
        altitude= 0,
        kappa_Korrektur= 1.0
    ),
    "SATURN": Physics(
        g= 10.44,
        dynViskos= 0.0,
        kinViskos= 0.0,
        T= 134,
        Luftdichte_rho= 0.19,
        altitude= 0,
        kappa_Korrektur= 1.0
    )
}
