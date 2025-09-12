def obtener_precio_base(estilo):
    if estilo == "chica":
        return 500
    elif estilo == "mediana":
        return 800
    elif estilo == "grande":
        return 1200
    else:
        print(" Estilo no válido, se asignará precio de MEDIANA.")
        return 800

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

if respuesta == "si":
    estilo = input("Elige estilo (chica/mediana/grande): ").lower()
    precio_base = obtener_precio_base(estilo)

    ingredientes_extra = int(input("¿Cuántos ingredientes extra quieres? (cada uno $50): "))
    cantidad = int(input("¿Cuántas paellas quieres pedir? "))

    subtotal = calcular_subtotal(precio_base, ingredientes_extra, cantidad)
    total = calcular_total(subtotal)

    if total > 0:
        print(f" El costo total de tu pedido es: ${total:.2f}, gracias por comprar!")
    else:
        print(" No se pudo calcular tu pedido correctamente.")
else:
    print("Gracias por tu visita. ¡Vuelve pronto! ")

