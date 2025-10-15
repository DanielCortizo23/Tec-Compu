def mostrar_menu(paellas):
    """
    Esta funcion sirve para mostrar el menu de las paellas,
    junto con el precio y los ingredientes
    """
    print("\n--- Menú de Paellas ---")
    i = 1  
    for paella in paellas:
        nombre = paella[0]
        precio = paella[1]
        ingredientes = paella[2]

        print(i, nombre,  precio,"MXN")
        print("   Ingredientes:", ingredientes)
        print()
        i = i + 1


def calcular_subtotal(precio_paella, cantidad):
    """
    Esta funcion me ayuda a calcular el total
    dependiendo de la cantidad de paella que quiera
    con el precio de cada una
    """
    if cantidad <= 0:
        print("La cantidad mínima es 1. Se pondrá 1.")
        cantidad = 1
    return precio_paella * cantidad


def calcular_total(subtotal):
    """
    Esta funcion calcula el total con iva
    """
    iva = subtotal * 0.16
    return subtotal + iva


"""
======================================    Esta es la matriz de las paellas     ==================================================== 
"""

paellas = [["Paella Mixta", 395,
            "costilla, pollo, butifarra, almejas, mejillones,"
            "calamar, camarón pacotilla, camarón jumbo"],
            ["Paella Marinera", 545,
             "lomo de merluza, pulpo, almejas, mejillones,"
             "calamar, camarón pacotilla, camarón jumbo"],
            ["Paella Negra", 495,
             "camarones jumbo, calamar, mejillones, alioli"],
            ["Paella Especial", 695,
             "lomo de merluza, pulpo, almejas, mejillones, calamar,"
             "camarón pacotilla, camarón jumbo, vieiras"]
]

"""
======================================    Codigo principal del programa     ==================================================== 
"""


print("Bienvenido a Delantal Iberico")

respuesta = input("¿Quieres comprar paella? (si/no): ")

while respuesta not in ["si", "no"]:
    print("Respuesta no válida. Escribe 'si' o 'no'.")
    respuesta = input("¿Quieres comprar paella? (si/no): ")

if respuesta == "si":
    mostrar_menu(paellas)

    opcion = int(input("Elige el número de la paella que deseas: "))
    while opcion < 1 or opcion > len(paellas):
        print("Opción no válida.")
        opcion = int(input("Elige el número de la paella que deseas: "))

    nombre_paella, precio_paella, ingredientes = paellas[opcion - 1]

    confirmar = input(f"Elegiste '{nombre_paella}'. ¿Es correcto? (si/no): ")
    while confirmar not in ["si", "no"]:
        confirmar = input("Respuesta no válida. Escribe 'si' o 'no': ")

    if confirmar == "no":
        print("Operación cancelada.")
        exit()

    cantidad = int(input(f"¿Cuántas órdenes de '{nombre_paella}' quieres? "))
    confirmar = input(f"Elegiste {cantidad} orden(es). ¿Es correcto? (si/no): ")
    while confirmar not in ["si", "no"]:
        confirmar = input("Respuesta no válida. Escribe 'si' o 'no': ")

    if confirmar == "no":
        print("Operación cancelada.")
        exit()

    subtotal = calcular_subtotal(precio_paella, cantidad)
    total = calcular_total(subtotal)

    print("\n--- Resumen del Pedido ---")
    print("Paella elegida:", nombre_paella)
    print("Cantidad de órdenes:", cantidad)
    print("Ingredientes:", ingredientes)
    print("Subtotal:", subtotal, "MXN")
    print("Total con IVA (16%):", total, "MXN")

    confirmar = input("\n¿Deseas realizar el pedido? (si/no): ")
    while confirmar not in ["si", "no"]:
        confirmar = input("Respuesta no válida. Escribe 'si' o 'no': ")

    if confirmar == "si":
        print("Gracias por tu compra, vuelva pronto!!")
    else:
        print("Pedido cancelado. ¡Gracias por tu visita!")

else:
    print("Muchas gracias por su visita")

"""
======================================    Fin del programa    ==================================================== 
"""  

