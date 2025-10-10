def mostrar_menu(paellas):
    print("\n--- Menú de Paellas ---")
    i = 1  
    for paella in paellas:
        nombre = paella[0]
        precio = paella[1]
        ingredientes = paella[2]

        print((i),(nombre),  (precio),"MXN")
        print("   Ingredientes:", ingredientes)
        print()
        i = i + 1


def calcular_subtotal(precio_paella, cantidad):
    if cantidad <= 0:
        print("La cantidad mínima es 1. Se pondrá 1.")
        cantidad = 1
    return precio_paella * cantidad


def calcular_total(subtotal):
    iva = subtotal * 0.16
    return subtotal + iva




paellas = [["Paella Mixta", 395, "costilla, pollo, butifarra, almejas, mejillones, calamar, camarón pacotilla, camarón jumbo"],
["Paella Marinera", 545, "lomo de merluza, pulpo, almejas, mejillones, calamar, camarón pacotilla, camarón jumbo"],
["Paella Negra", 495, "camarones jumbo, calamar, mejillones, alioli"],
["Paella Especial", 695, "lomo de merluza, pulpo, almejas, mejillones, calamar, camarón pacotilla, camarón jumbo, vieiras"]
]


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

  
    nombre_paella = paellas[opcion - 1][0]
    precio_paella = paellas[opcion - 1][1]
    ingredientes = paellas[opcion - 1][2]

    cantidad = int(input(f"¿Cuántas órdenes de '{nombre_paella}' quieres? "))

    subtotal = calcular_subtotal(precio_paella, cantidad)
    total = calcular_total(subtotal)

    print("\n--- Resumen del Pedido ---")
    print("Paella elegida:", nombre_paella)
    print("Cantidad de órdenes:", cantidad)
    print("Ingredientes:", ingredientes)
    print("Subtotal:", subtotal, "MXN")
    print("Total con IVA (16%):", total, "MXN")

else:
    print("Gracias por tu visita. ¡Vuelve pronto!")
