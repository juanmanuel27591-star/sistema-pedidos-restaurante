# Sistema de Pedidos para Restaurantes

Proyecto que simula, y después implementa como app web, el flujo de pedidos de un restaurante/bar: el cliente elige platos y bebidas de un menú, indica su mesa, revisa y confirma el pedido, y este llega a una vista de cocina con el detalle y el total a pagar. Incluye además un panel de administración para que el dueño del restaurante gestione su propio menú.

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

## `web/` — versión web con Flask + SQLite

La misma lógica, ahora accesible desde un navegador, con un flujo completo de cliente, vista de cocina, y panel de administración con base de datos persistente.

**Qué hace, del lado del cliente:**
- Muestra el menú (platos y bebidas) en una página web, con precios.
- El cliente indica su mesa (validada contra un tope configurable) y elige cantidades por ítem.
- Pantalla de revisión antes de confirmar (para poder corregir mesa o cantidades).
- Al confirmar, el pedido se guarda y aparece en `/cocina`, agrupado por mesa.

**Qué hace, del lado del panel de administración (`/admin`):**
- Agregar ítems nuevos al menú (nombre, precio, categoría).
- Editar y borrar ítems existentes.
- Configurar el tope de número de mesa del local.

Todo el menú y la configuración viven en una base de datos SQLite (`restaurante.db`), en vez de estar fijos en el código — así el dueño puede modificar su carta sin tocar una línea de Python.

**Cómo correrlo:**
```bash
cd web
python setup_db.py   # solo la primera vez, crea y carga la base de datos
python app.py
```
Después abrí `http://127.0.0.1:5000` en el navegador. La vista de cocina está en `/cocina`, y el panel de administración en `/admin`.

**Estructura:**
- `app.py`: rutas y lógica del servidor.
- `setup_db.py`: script que crea la base de datos SQLite con el menú inicial y la configuración.
- `templates/menu.html`: página principal con el formulario de pedido.
- `templates/pedido.html`: pantalla de revisión antes de confirmar.
- `templates/confirmado.html`: confirmación final para el cliente.
- `templates/cocina.html`: vista con todos los pedidos recibidos.
- `templates/admin.html`: panel de administración (menú, configuración).
- `templates/editar.html`: formulario para editar un ítem existente.

## Próximos pasos

- Proteger `/admin` con usuario y contraseña.
- Tope de cantidad máxima configurable por ítem.
- Que los pedidos recibidos también persistan en la base de datos (hoy se pierden al reiniciar el servidor).

## Sobre este proyecto

Hecho como proyecto de aprendizaje, programado línea por línea a mano para afianzar los fundamentos de Python (variables, condicionales, bucles, funciones, listas, diccionarios, manejo de errores) y dar el salto a desarrollo web con Flask (rutas, templates, formularios) y bases de datos (SQLite, SQL básico).