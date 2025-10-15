"""
Algoritmo

Inicio
Quieres comprar paella
Respuesta si entonces ofrecer estilo de paella, tamaño y ingredientes
Pedir al usuario que llene los datos de como quiere la paella
Quieres hacer el pedido
Respuesta si etonces pedir datos del usario = crear cuenta, 
pedir metodo de pago
Respuesta no entonces regresar a pedir los datos de la paella
Respuesta no entonces ofrecer servicio a eventos
Respuesta si entoces dar horarios y ubicacion
Pedir crear cuenta y dar datos de ubicacion
Respuesta no regresar a la pagina de inico 
"""

def menu(paellas):
    """
    Esta funcion sirve para mostrar el menu de las paellas,
    junto con el precio y los ingredientes.

    Aqui usea enumerate que es algo que vi yo,
    sirve para recorrer una secuencia y al mismo tiempo
    obtener el indice y el valor de cada elemento
    """
    print("\n------------- Menu de Paellas -------------")
   
    for i, paella in enumerate(paellas, start=1):
        nombre = paella[0]
        precio = paella[1]
        ingredientes = paella[2]

        print(i, nombre,precio, "MXN")
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

paellas = [["Paella Mixta", 395,
            "costilla, pollo, butifarra, almejas, mejillones,"
            "calamar, camaron pacotilla, camaron jumbo"],
            ["Paella Marinera", 545,
             "lomo de merluza, pulpo, almejas, mejillones,"
             "calamar, camaron pacotilla, camaron jumbo"],
             ["Paella Negra", 495,
              "camarones jumbo, calamar, mejillones, alioli"],
              ["Paella Especial", 695,
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
    while c not in ["si","no"]:
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

    print("\n-- Resumen del Pedido ---")
    print("Paella elegida:", nombre_paella)
    print("Numero de ordenes solicitadas:", cantidad)
    print("Ingredientes de la paella:", ingredientes)
    print("Subtotal:", subtotal, "MXN")
    print("Total final con IVA (16%):", total, "MXN")

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

