print("¿Quieres comprar paella?")
respuesta = input("Responde si/no: ")

if respuesta == "si":
    estilo = input("Elige estilo (chica/mediana/grande): ")
    
    if estilo == "chica":
        precio_base = 500
    elif estilo == "mediana":
        precio_base = 800
    else:
        precio_base = 1200

    ingredientes_extra = int(input("¿Cuántos ingredientes extra quieres? "))
    costo_extra = ingredientes_extra * 50
    
    cantidad = int(input("¿Cuántas paellas quieres pedir? "))

    subtotal_unidad = precio_base + costo_extra

    subtotal = subtotal_unidad * cantidad

    iva = subtotal * 0.16
    total = subtotal + iva

    print(f"El costo total de tu pedido es: ${total}")
    
    