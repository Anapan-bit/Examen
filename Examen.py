import random
import csv
import os

#Lista de trabajadores
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

sueldos = []

#Crear el archivo
def crear_archivo_csv():
    with open('sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Sueldo"])

#Asignar sueldos en archivo aparte
def asignar_sueldos_aleatorios():
    os.system('cls')
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in trabajadores]
    with open('sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Sueldo"])
        for i, sueldo in enumerate(sueldos):
            writer.writerow([trabajadores[i], sueldo])
    print("Sueldos asignados correctamente y guardados en sueldos.csv.")


def clasificar_sueldos():
    #Si no se han asignado los sueldos
    os.system('cls')
    if not sueldos:
        print("Debe asignar los sueldos primero.")
        input("Presione una tecla para continuar...")
        os.system('cls')
        return
    
    
    #Clasificacion
    menores_800k = [(trabajadores[i], sueldo) for i, sueldo in enumerate(sueldos) if sueldo < 800000]
    entre_800k_2000k = [(trabajadores[i], sueldo) for i, sueldo in enumerate(sueldos) if 800000 <= sueldo <= 2000000]
    mayores_2000k = [(trabajadores[i], sueldo) for i, sueldo in enumerate(sueldos) if sueldo > 2000000]

    os.system('cls')
    print("\nSueldos menores a $800.000")
    print(f"TOTAL: {len(menores_800k)}")
    print(f"{'Nombre empleado':<20}{'Sueldo':>15}")
    print('-' * 35)
    for trabajador, sueldo in menores_800k:
        print(f"{trabajador:<20} ${sueldo:>10,}")


    print("\nSueldos entre $800.000 y $2.000.000")
    print(f"TOTAL: {len(entre_800k_2000k)}")
    print(f"{'Nombre empleado':<20}{'Sueldo':>15}")
    print('-' * 35)
    for trabajador, sueldo in entre_800k_2000k:
        print(f"{trabajador:<20} ${sueldo:>10,}")


    print("\nSueldos superiores a $2.000.000")
    print(f"TOTAL: {len(mayores_2000k)}")
    print(f"{'Nombre empleado':<20}{'Sueldo':>15}")
    print('-' * 35)
    for trabajador, sueldo in mayores_2000k:
        print(f"{trabajador:<20} ${sueldo:>10,}")
    


def ver_estadisticas():
    #Si no se han asignado los sueldos
    if not sueldos:
        print("Debe asignar los sueldos primero.")
        return
    
    #Estadisticas
    max_sueldo = max(sueldos)
    min_sueldo = min(sueldos)
    promedio = sum(sueldos) / len(sueldos)
    
    os.system('cls')
    print(f"Sueldo más alto: ${max_sueldo}")
    print(f"Sueldo más bajo: ${min_sueldo}")
    print(f"Promedio de sueldos: ${promedio:.0f}")

def reporte_sueldos():
    #Si no se han asignado los sueldos
    if not sueldos:
        os.system('cls')
        print("Debe asignar los sueldos primero.")
        return
    
    #Reporte
    with open('sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        os.system('cls')
        print("Reporte de sueldos")
        print("\nNombre empleado | Sueldo Base | Descuento Salud | Descuento AFP | Sueldo Líquido")
        for i, sueldo in enumerate(sueldos):
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([trabajadores[i], sueldo, descuento_salud, descuento_afp, sueldo_liquido])
            print(f"{trabajadores[i]} | ${sueldo} | ${descuento_salud:.0f} | ${descuento_afp:.0f} | ${sueldo_liquido:.0f}")
    print("Datos de sueldos guardados")

#Salir!
def salir_programa():
    print("Finalizando programa... Desarrollado por Anais Palma RUT: 20.965.255-5")

#Mostrar el menú
def menu():
    while True:
        print("Menú de opciones:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            asignar_sueldos_aleatorios()
            input("Presione una tecla para continuar...")
            os.system('cls')
        elif opcion == '2':
            clasificar_sueldos()
            input("Presione una tecla para continuar...")
            os.system('cls')
        elif opcion == '3':
            ver_estadisticas()
            input("Presione una tecla para continuar...")
            os.system('cls')
        elif opcion == '4':
            reporte_sueldos()
            input("Presione una tecla para continuar...")
            os.system('cls')
        elif opcion == '5':
            salir_programa()
            break
        else:
            os.system('cls')
            print("Opción no válida, por favor intente de nuevo.")
            input("Presione una tecla para continuar...")
            os.system('cls')

# Iniciar el programa directamente
crear_archivo_csv()
menu()



