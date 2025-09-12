def obtener_precio_base(estilo):
    if estilo == "chica":
        return 500
    elif estilo == "mediana":
        return 800
    elif estilo == "grande":
        return 1200
    else:
        print("Estilo no válido, se asignará precio de mediana.")
        return 800

def calcular_subtotal(precio_base, ingredientes_extra, cantidad):
    costo_extra = ingredientes_extra * 50
    subtotal_unidad = precio_base + costo_extra
    return subtotal_unidad * cantidad

def calcular_total(subtotal):
    iva = subtotal * 0.16
    return subtotal + iva

print("¿Quieres comprar paella?")
respuesta = input("Responde si/no: ")

if respuesta == "si":
    estilo = input("Elige estilo (chica/mediana/grande")
    precio_base = obtener_precio_base(estilo)

    ingredientes_extra = int(input("¿Cuántos ingredientes extra quieres? "))
    cantidad = int(input("¿Cuántas paellas quieres pedir? "))

    subtotal = calcular_subtotal(precio_base, ingredientes_extra, cantidad)
    total = calcular_total(subtotal)

    print(f"El costo total de tu pedido es: ${total:.2f}")
else:
    print("Gracias por tu visita. ¡Vuelve pronto!")


"en mi python si me corrio el programa"

    



