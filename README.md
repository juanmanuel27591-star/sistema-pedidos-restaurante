# Sistema de Pedidos para Restaurantes (prototipo de consola)

Prototipo en Python que simula la lógica central de una app de pedidos para restaurantes/bares: el cliente elige platos y bebidas de un menú, y el sistema arma la comanda con cantidades y calcula el total a pagar.

Este proyecto es la primera etapa de una idea más grande: una app donde el cliente escanea un código QR en la mesa, pide desde su celular, y el pedido llega directo a cocina/mozo — sin necesidad de que el mozo tome nota a mano. Esta versión de consola resuelve toda la lógica de negocio antes de sumarle una interfaz web.

## Qué hace

- Muestra el menú de platos y bebidas, numerado y con precios.
- Permite ir eligiendo ítems por número, validando que el dato ingresado sea correcto (rechaza texto no numérico y números fuera de rango).
- Agrupa el pedido en una comanda con cantidades (ej: `3 x Milanesa`) en vez de mostrar ítems repetidos.
- Calcula el subtotal por ítem y el total final a pagar.

## Cómo correrlo

Requiere Python 3 instalado.

```bash
python restolimpio.py
```

Seguí las instrucciones en pantalla: elegí platos por número, escribí `listo` para pasar a las bebidas, y de nuevo `listo` al terminar para ver la comanda y el total.

## Ejemplo de uso

```
--- Platos ---
1 Milanesa - $35000
2 Fideos - $30000
3 Sandwich - $25000
4 Pizza - $20000
5 Empanadas - $5000
Que queres pedir? o ('listo'): 1
Que queres pedir? o ('listo'): 1
Que queres pedir? o ('listo'): listo
--- Bebidas ---
1 Cerveza - $5000
2 vino - $5000
...
Que queres pedir? o ('listo'): listo
--- Tu pedido ---
2 x Milanesa - $70000
Total a pagar: $70000
```

## Estructura del código

- `platos` / `bebidas`: listas del menú, cada ítem es una tupla `(nombre, precio)`.
- `mostrar_menu()`: imprime un menú numerado con precios.
- `elegir_items()`: maneja la elección de ítems del cliente, con validación de datos inválidos.
- `main()`: orquesta el flujo completo (mostrar menú, tomar pedido, armar comanda, calcular total).

## Próximos pasos

- Pasar la interfaz de consola a una app web (Flask), accesible desde un QR en la mesa.
- Persistir el menú y los pedidos en una base de datos.
- Pantalla en tiempo real para cocina/mozo.

## Sobre este proyecto

Hecho como proyecto de aprendizaje, programado línea por línea a mano para afianzar los fundamentos de Python (variables, condicionales, bucles, funciones, listas, diccionarios, manejo de errores) antes de escalar a una aplicación web completa.
