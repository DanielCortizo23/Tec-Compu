import math
import random

def menu(paellas):
    """
    Esta funcion sirve para mostrar el menu de las paellas,
    junto con el precio y los ingredientes.

    Aqui use enumerate que es algo que vi yo,
    sirve para recorrer una secuencia y al mismo tiempo
    obtener el indice y el valor de cada elemento
    """
    print("\n------------- Menu de Paellas -------------")
    i = 1
    for paella in paellas:
        nombre = paella[0]
        precio = paella[1]
        ingredientes = paella[2]

        print(i, nombre, precio, "MXN")
        print("Ingredientes: ", ingredientes)
        i += 1
        


def c_subtotal(precio_paella, cantidad):
    """
    Esta funcion me ayuda a calcular el total
    dependiendo de la cantidad de paella que quiera
    con el precio de cada una.
    """
    if cantidad <= 0:
        print("La cantidad minima es 1. Se pondra 1.")
        cantidad = 1
    return precio_paella * cantidad


def c_total(subtotal):
    """Esta funcion calcula el total con iva."""
    iva = subtotal * 0.16
    return subtotal + iva


"""
=============    Esta es la matriz de las paellas     ===============
"""

paellas = [["Paella Mixta", 465,
            "costilla, pollo, butifarra, almejas, mejillones,"
            "calamar, camaron pacotilla, camaron jumbo"],
           ["Paella Marinera", 635,
            "lomo de merluza, pulpo, almejas, mejillones,"
            "calamar, camaron pacotilla, camaron jumbo"],
           ["Paella Negra", 585,
            "camarones jumbo, calamar, mejillones, alioli"],
           ["Paella Especial", 785,
               "lomo de merluza, pulpo, almejas, mejillones, calamar,"
               "camaron pacotilla, camaron jumbo, vieiras"]

           ]

"""
================   Codigo principal del programa     =============
"""

print("Bienvenido a delantal Iberico")

r = input("Te gustaria comprar una paella? (si/no): ")

while r not in ["si", "no"]:
    print("Respuesta no aceptada. Porfavor escriba 'si' o 'no'.")
    r = input("Te gustaria comprar una paella? (si/no): ")

if r == "si":
    menu(paellas)

    o = int(input("\nElige el numero de paella que desea pedir: "))
    while o < 1 or o > len(paellas):
        print("Porfavor eliga entre las 4 paellas que tenemos.")
        o = int(input("Elige el numero de paella que desea pedir: "))

    nombre_paella, precio_paella, ingredientes = paellas[o-1]

    c = input(f"Elegiste: {nombre_paella}. Es correcto? (si/no): ")
    while c not in ["si", "no"]:
        c = input("Respuesta erronea. Porfa escriba 'si' o 'no'. ")

    if c == "no":
        print("Pedido cancelado.")
        exit()

    cantidad = int(input(f"\nOrdenes de, {nombre_paella} quieres? "))
    c = input(f"Elegiste {cantidad} orden/es. Es correcto?(si/no): ")
    while c not in ["si", "no"]:
        c = input("Respuesta erronea. Porfa escriba 'si' o 'no'. ")

    if c == "no":
        print("Pedido cancelado.")
        exit()

    subtotal = c_subtotal(precio_paella, cantidad)
    total = c_total(subtotal)
    total_redondeado = math.ceil(total)
    descuento = random.randint(5, 20)
    monto_descuento = subtotal * (descuento/100)
    total_desc = subtotal - monto_descuento

    print("\n-- Resumen del Pedido ---")
    print("Paella elegida:", nombre_paella)
    print("Numero de ordenes solicitadas:", cantidad)
    print("Ingredientes de la paella:", ingredientes)
    print("Subtotal:", subtotal, "MXN")
    print("Total final (redondeado):", total_redondeado, "MXN")
    print("Total final con IVA (16%):", total, "MXN")
    print(f"¡Felicidades! Obtienes un {descuento}% de descuento.")
    print("Subtotal:", subtotal, "MXN")
    print("Total con descuento:", round(total_desc, 2), "MXN")

    c = input("\n Confirmacion del pedido (si/no): ")
    while c not in ["si", "no"]:
        c = input("Respuesta erronea. Porfavor escriba 'si' o 'no'. ")

    if c == "si":
        print("\nMuchas gracias por comprar, vuelva pronto!!")
    else:
        print("Pedido cancelado. Gracias por su visita!")

else:
    print("Para que se mete si no va a comprar")

"""
=============================   Fin del programa    =================
"""


