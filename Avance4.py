def obtener_precio_base(personas):
    if personas == 15:
        return 600
    elif personas == 25:
        return 900
    elif personas == 40:
        return 1400
    elif personas == 50:
        return 1700
    else:
        print("Cantidad no válida. Se asignará paella para 25 personas.")
        return 900

def calcular_subtotal(precio_base, ingredientes_extra, cantidad):
    if ingredientes_extra < 0:
        print(" No puedes poner ingredientes negativos, se pondrá 0.")
        ingredientes_extra = 0
    if cantidad <= 0:
        print(" La cantidad mínima es 1, se pondrá 1.")
        cantidad = 1

    costo_extra = ingredientes_extra * 50
    subtotal_unidad = precio_base + costo_extra
    return subtotal_unidad * cantidad

def calcular_total(subtotal):
    if subtotal > 0:
        iva = subtotal * 0.16
        return subtotal + iva
    else:
        return 0

print(" Bienvenido a Paellas Online ")

respuesta = input("¿Quieres comprar paella? (si/no): ").lower()

while respuesta != "si" and respuesta != "no":
    print(" Respuesta no válida. Escribe 'si' o 'no'.")
    respuesta = input("¿Quieres comprar paella? (si/no): ").lower()

if respuesta == "si":
    personas = int(input("¿Para cuántas personas será la paella? (15 / 25 / 40 / 50): "))
    while personas != 15 and personas != 25 and personas != 40 and personas != 50:
        print(" Opción no válida. Elige 15, 25, 40 o 50.")
        personas = int(input("¿Para cuántas personas será la paella? (15 / 25 / 40 / 50): "))

    precio_base = obtener_precio_base(personas)

    ingredientes_extra = int(input("¿Cuántos ingredientes extra quieres? (cada uno $50): "))
    while ingredientes_extra < 0:
        print(" No puedes poner un número negativo.")
        ingredientes_extra = int(input("¿Cuántos ingredientes extra quieres? (cada uno $50): "))

    cantidad = int(input("¿Cuántas paellas quieres pedir? "))
    while cantidad <= 0:
        print(" La cantidad mínima es 1.")
        cantidad = int(input("¿Cuántas paellas quieres pedir? "))

    subtotal = calcular_subtotal(precio_base, ingredientes_extra, cantidad)
    total = calcular_total(subtotal)

    if total > 0:
        print(f" El costo total de tu pedido es: ${total:.2f}. ¡Gracias por comprar con nosotros!")
    else:
        print(" No se pudo calcular tu pedido correctamente.")
else:
    print("Gracias por tu visita. ¡Vuelve pronto!")


