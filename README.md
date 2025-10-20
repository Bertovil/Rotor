# Rotor
Helicopter Calculations

Purpose: Little Tool to perform calculations on model helicopters for performance analysis and comparisions of different types and brands.
Structure: 
  - main: start main.py for interaction with the console
  - classes: contains information for building instances from data, new data is stored in data-files
  - data_model: contains information on available helicopter models
  - data_rotor: contains information on available rotors
  - data_battery: contains information on available batteries
  - data_physics: contains information on available physics models
  - functions2: contains definitions of available calculations with data
  - rotor_help: calls helper-functions
  - utils: contains names of functions2 for calculations and explanation text

Usage:
  1. start main.py
  2. enter data string to populate each category with a data set. Categories to set are [model, rotor, battery, physics]    
  3. possible actions with data are:


    Perform a single calculation with data sets:
     ```shell
       --calc [name of function]
     ```
     
     List all available calculation functions:
     ```shell
       --calc list
     ```

      Show parameters of chosen data sets:
      ```shell
       --show param 
      ```

      Show object names of chosen data sets:
      ```shell
       --show all
       ```
       
4. example usage:

```shell
--model LOGO600SX --rotor NACA0009 --battery TURNIGY5000 --physics ERDE --calc induzierter_Durchflussgrad_lambda_i
```

5. result: ✅ Ergebnis von induzierter_Durchflussgrad_lambda_i(): 0.03710445257197212

6. argument ```shell --help ``` or ```shell --h ``` is used for general help
7. argument ```shell --help [name of functions] ``` is used for specific information on calculation function, which is edited in the utils.py 

     
  
