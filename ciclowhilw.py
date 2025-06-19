"""
i = 1
while i <= 10:
    
    print(i*8)
    i = i + 1
"""
"""
tabla = int(input("Que tabla quiere?: "))
i = 1
while i <= 10:
    
    print(tabla,"x","=",i*tabla)
    i = i + 1
"""
"""
i = 1 
while i <= 100:
    if i%7 == 0:
        print(i)
    i += 1
"""

def encontrar_multiplos(limite_superior=100):
    """
    Encuentra los múltiplos de un número especificado por el usuario
    dentro de un rango de 1 hasta el límite_superior.
    """
    """
    while True:
        try:
            # Solicitar al usuario el número del cual quiere los múltiplos
            numero_multiplo = int(input("Ingresa el número del cual quieres encontrar los múltiplos: "))

            # Validar que el número no sea cero para evitar divisiones por cero o bucles infinitos
            if numero_multiplo == 0:
                print("No puedes encontrar múltiplos de cero (o el resultado serían todos los números). Por favor, ingresa un número diferente de cero.")
                continue # Pide el número de nuevo
            break # Sale del bucle si el número es válido

        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    multiplos_encontrados = []
    # Iterar desde 1 hasta el límite superior (incluyéndolo)
    for numero in range(1, limite_superior + 1):
        # Si el residuo de la división es 0, es un múltiplo
        if numero % numero_multiplo == 0:
            multiplos_encontrados.append(numero)

    # Mostrar los resultados
    if multiplos_encontrados:
        print(f"\nLos múltiplos de {numero_multiplo} del 1 al {limite_superior} son:")
        print(multiplos_encontrados)
    else:
        print(f"\nNo se encontraron múltiplos de {numero_multiplo} del 1 al {limite_superior}.")

# Llamar a la función para ejecutar el programa
encontrar_multiplos(100)      
"""

def simular_restaurante():
    """
    Simula un restaurante: muestra un menú, permite al cliente pedir
    y calcula el total de la factura.
    """
    menu = {
        "1": {"nombre": "Hamburguesa Clásica", "precio": 12.50},
        "2": {"nombre": "Pizza Pepperoni", "precio": 15.00},
        "3": {"nombre": "Ensalada César", "precio": 9.75},
        "4": {"nombre": "Pasta Carbonara", "precio": 13.25},
        "5": {"nombre": "Tacos al Pastor (3)", "precio": 11.00},
        "6": {"nombre": "Refresco", "precio": 2.50},
        "7": {"nombre": "Agua Mineral", "precio": 2.00},
        "8": {"nombre": "Postre de Chocolate", "precio": 6.00}
    }

    orden_cliente = {} # Aquí guardaremos lo que el cliente pida
    total_cuenta = 0.0

    print("¡Bienvenido a nuestro restaurante!")
    print("--- Nuestro Menú ---")

    # Mostrar el menú al cliente
    for key, item in menu.items():
        print(f"{key}. {item['nombre']}: ${item['precio']:.2f}")
    print("--------------------")

    # Tomar el pedido del cliente
    while True:
        eleccion = input("Ingresa el número del platillo que deseas (o 'fin' para terminar tu pedido): ").lower()

        if eleccion == 'fin':
            break
        elif eleccion in menu:
            while True:
                try:
                    cantidad = int(input(f"¿Cuántas unidades de '{menu[eleccion]['nombre']}' deseas? "))
                    if cantidad > 0:
                        # Añadir al pedido del cliente
                        if eleccion in orden_cliente:
                            orden_cliente[eleccion]['cantidad'] += cantidad
                        else:
                            orden_cliente[eleccion] = {"nombre": menu[eleccion]['nombre'], "precio": menu[eleccion]['precio'], "cantidad": cantidad}
                        print(f"'{menu[eleccion]['nombre']}' añadido a tu pedido.")
                        break # Sale del bucle de cantidad
                    else:
                        print("Por favor, ingresa una cantidad positiva.")
                except ValueError:
                    print("Cantidad inválida. Ingresa un número entero.")
        else:
            print("Número de platillo no válido. Por favor, elige un número del menú o escribe 'fin'.")

    # Generar la factura
    print("\n--- TU FACTURA ---")
    if not orden_cliente:
        print("No has pedido nada. ¡Vuelve pronto!")
    else:
        for key, item_ordenado in orden_cliente.items():
            subtotal = item_ordenado['precio'] * item_ordenado['cantidad']
            total_cuenta += subtotal
            print(f"{item_ordenado['nombre']} x {item_ordenado['cantidad']} = ${subtotal:.2f}")

        print(f"--------------------")
        print(f"TOTAL A PAGAR: ${total_cuenta:.2f}")
        print("¡Gracias por tu visita!")

# Ejecutar la simulación del restaurante
simular_restaurante()