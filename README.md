# Sistema de Pedidos para Restaurantes

Proyecto que simula, y después implementa como app web, el flujo de pedidos de un restaurante/bar: el cliente elige platos y bebidas de un menú, indica su mesa, revisa y confirma el pedido, y este llega a una vista de cocina con el detalle y el total a pagar.

Es la primera etapa de una idea más grande: una app donde el cliente escanea un código QR en la mesa, pide desde su celular, y el pedido llega directo a cocina/mozo — sin necesidad de que el mozo tome nota a mano.

El proyecto tiene dos versiones, en carpetas separadas, que muestran la evolución del desarrollo:

## `consola/` — prototipo de terminal

La primera versión, hecha para resolver y probar toda la lógica de negocio antes de sumarle una interfaz.

**Qué hace:** muestra el menú numerado con precios, permite elegir ítems por número (validando datos inválidos), agrupa el pedido en una comanda con cantidades, y calcula el total a pagar.

**Cómo correrlo:**
```bash
cd consola
python resto_limpio.py
```

## `web/` — versión web con Flask

La misma lógica, ahora accesible desde un navegador, con un flujo completo de cliente y una vista para cocina.

**Qué hace:**
- Muestra el menú (platos y bebidas) en una página web, con precios.
- El cliente indica su mesa y elige cantidades por ítem.
- Pantalla de revisión antes de confirmar (para poder corregir mesa o cantidades).
- Al confirmar, el pedido se guarda y aparece en `/cocina`, agrupado por mesa.

**Cómo correrlo:**
```bash
cd web
python app.py
```
Después abrí `http://127.0.0.1:5000` en el navegador. La vista de cocina está en `http://127.0.0.1:5000/cocina`.

**Estructura:**
- `app.py`: rutas y lógica del servidor (`/`, `/pedido`, `/confirmar`, `/cocina`).
- `templates/menu.html`: página principal con el formulario de pedido.
- `templates/pedido.html`: pantalla de revisión antes de confirmar.
- `templates/confirmado.html`: confirmación final para el cliente.
- `templates/cocina.html`: vista con todos los pedidos recibidos.

## Próximos pasos

- Guardar el menú y los pedidos en una base de datos (en vez de listas fijas en el código).
- Panel para que el dueño del restaurante pueda cargar y editar su propio menú.
- Configuración de topes (cantidad máxima por ítem, número de mesa según el tamaño del local).

## Sobre este proyecto

Hecho como proyecto de aprendizaje, programado línea por línea a mano para afianzar los fundamentos de Python (variables, condicionales, bucles, funciones, listas, diccionarios, manejo de errores) y dar el salto a desarrollo web con Flask (rutas, templates, formularios).