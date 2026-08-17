# --- Menú del restaurante ---
# Cada plato/bebida es una tupla: (nombre, precio)
platos = [
    ("Milanesa", 35000),
    ("Fideos", 30000),
    ("Sandwich", 25000),
    ("Pizza", 20000),
    ("Empanadas", 5000),
]

bebidas = [
    ("Cerveza", 5000),
    ("vino", 5000),
    ("Gaseosa", 3000),
    ("Agua", 2500),
    ("Soda", 1000),
]


def elegir_items(lista_menu, pedido):
    """Muestra un menú y deja elegir items por número hasta que se escribe 'listo'."""
    while True:
        eleccion = input("Que queres pedir? o ('listo'): ")

        if eleccion == "listo":
            break

        try:
            indice = int(eleccion) - 1
            if indice < 0 or indice >= len(lista_menu):
                raise ValueError("fuera de rango")
            nombre_item, precio_item = lista_menu[indice]
            pedido.append(nombre_item)
        except:
            print("numero no valido, intenta de nuevo")


def mostrar_menu(lista_menu):
    """Imprime un menú numerado con precios."""
    for numero, (nombre, precio) in enumerate(lista_menu, 1):
        print(numero, nombre, "-", "$" + str(precio))


def main():
    pedido = []

    print("--- Platos ---")
    mostrar_menu(platos)
    elegir_items(platos, pedido)

    print("--- Bebidas ---")
    mostrar_menu(bebidas)
    elegir_items(bebidas, pedido)

    # Agrupar el pedido en cantidades por item
    comanda = {}
    for item in pedido:
        if item in comanda:
            comanda[item] = comanda[item] + 1
        else:
            comanda[item] = 1

    # Calcular y mostrar el total a pagar
    precios = dict(platos + bebidas)
    total = 0
    print("--- Tu pedido ---")
    for nombre, cantidad in comanda.items():
        precio_unitario = precios[nombre]
        subtotal = cantidad * precio_unitario
        total = total + subtotal
        print(cantidad, "x", nombre, "-", "$" + str(subtotal))

    print("Total a pagar: $" + str(total))


main()