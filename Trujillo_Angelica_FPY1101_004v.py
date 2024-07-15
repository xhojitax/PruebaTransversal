import random
import statistics
import csv

trabajadores = [
    {"nombre": "juan perez"}, 
    {"nombre": "María García"},
    {"nombre": "Carlos López"},
    {"nombre": "Ana Martinez"},
    {"nombre": "Pedro Rodríguez"},
    {"nombre": "Laura Hernández"},
    {"nombre": "Miguel Sánchez"},
    {"nombre": "Isabel Gómez"},
    {"nombre": "Francisco Díaz"},
    {"nombre": "Elena Fernández"}
]

def asignar_sueldo():

    for empleado in trabajadores:
        empleado ["sueldo"]=random.randint(300000, 2500000)
    

def clasificar():
    for empleado in trabajadores:
        nom= empleado["nombre"]
        sueldo= empleado["sueldo"]
        if sueldo < 800000:
            print(f"{nom}: ${sueldo} - Sueldo bajo")
        elif 800000 <= sueldo <= 2000000:
            print(f"{nom}: ${sueldo} - sueldo medio")
        else:
            print(f"{nom}: ${sueldo} - sueldo alto")


def estadisticas():
    sueldos= [empleado["sueldo"] for empleado in trabajadores]
    sueldo_max= max(sueldos)
    sueldo_min= min(sueldos)
    promedio_sueldo= statistics.mean(sueldos)
    medida_G= statistics.geometric_mean(sueldos)

    print("estadisticas: ")
    print(f"sueldo mas alto: ${sueldo_max}")
    print(f"suelgo mas bajo: ${sueldo_min}")
    print(f"promedio de sueldos: ${promedio_sueldo}")
    print(f"medida geometria de sueldos: ${medida_G}")

def reporte():
    nom_archivo= "reporte_sueldo.csv"
    with open(nom_archivo, mode='w', newline="") as file:
        writer= csv.writer(file)
        writer.writerow(['nombre', 'cargo', 'sueldo_base', 'descuento_salud', 'descuento_afp', 'sueldo_liquido'])

        for empleado in trabajadores:
            nom=empleado['nombre']
            sueldo_base= empleado['sueldo']
            descuento_salud= sueldo_base * 0.07
            descuento_AFP= sueldo_base * 0.12
            sueldo_liquido= sueldo_base - descuento_salud - descuento_AFP
           
            print(f"\nNombre empleado: {nom}, Sueldo Base: ${sueldo_base}, Descuento Salud: ${descuento_salud}, Descuento AFP: ${descuento_AFP}, Sueldo Líquido: ${sueldo_liquido}")

while True:
    print("\nMenu")
    print("1. asignar sueldos aleatorios")
    print("2. clasificar sueldos")
    print("3. ver estadisticas")
    print("4. generar reporte de sueldos")
    print("5. salir del programa")

    op=input("seleccione una opcion: \n")
    
    if op =="1":
        asignar_sueldo()
        print("sueldos asignados aleatoriamente")
    elif op =="2":
        clasificar()
    elif op=="3":
        estadisticas()
    elif op=="4":
        reporte()
    elif op =="5":
        print("finalizando programa...")
        print("\ndesarrollado por: Angelica Trujillo Serrano")
        print("Rut: 18.085.559-9\n")
        break
    else:
        print("opcion no valida, intente nuevamente.")
        