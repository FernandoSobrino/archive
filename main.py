import csv

from support_functions import *


with open('datos_prueba_tecnica.csv') as file:
    reader = csv.reader(file, delimiter=";")
    
    resultado_h = 0
    resultado_m = 0
    sumatorio_bruto_anual = 0
    listado_trabajadores = []


    for row in reader:
        if row[4] == "H":
          resultado_h += (row.count("H"))
        if row[4] == "M":
          resultado_m += (row.count("M"))
        if row[10] == "Alovera":
          sumatorio_bruto_anual += int(row[6])
        if row[7] == "2" and int(row[6]) > 28000:
           listado_trabajadores.append(row)

    

    print("Bienvenido al programa de gestión de Equilibra")
    print("1- Nº Mujeres y hombres \n 2- Suma bruta anual de trabajadores de Alovera \n 3-Empleados de Equilibra RRHH con más de 28000 € brutos")
    
    opcion = choose_option('Introduzca una de las tres opciones disponibles: ',correct_number)

    if opcion == '1':
      print("Número de hombres: {0}, Número de mujeres: {1}".format(
          resultado_h, resultado_m))

    if opcion == '2':
      print("El salario bruto anual total de los trabajadores de Alovera es {0}".format(
          sumatorio_bruto_anual))
    
    if opcion == '3':
      print("Los empleados que perciben un salario de más de 28000 € y pertenecen a Equilibra RRHH son:")

      for trabajador in listado_trabajadores:
          
          print("Nombre: {0} | Apellidos: {1} {2}".format(trabajador[1], trabajador[2], trabajador[3]))
          
        
        
        
      

