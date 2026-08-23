import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

pedidos_recibidos = []


def obtener_menu():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, precio, categoria FROM menu")
    filas = cursor.fetchall()
    conexion.close()

    platos = []
    bebidas = []
    for id_item, nombre, precio, categoria in filas:
        if categoria == "plato":
            platos.append((id_item, nombre, precio))
        else:
            bebidas.append((id_item, nombre, precio))

    return platos, bebidas

@app.route("/")
def inicio():
    platos, bebidas = obtener_menu()
    return render_template("menu.html", platos=platos, bebidas=bebidas)

@app.route("/pedido", methods=["POST"])
def pedido():
    platos, bebidas = obtener_menu()
    mesa = request.form.get("mesa")

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT valor FROM configuracion WHERE clave = ?", ("tope_mesa",))
    fila = cursor.fetchone()
    conexion.close()
    tope_mesa = int(fila[0])



    try:
        mesa_numero = int(mesa)
        if mesa_numero < 1 or mesa_numero > tope_mesa:
            return "Número de mesa inválido para este restaurante"
    except:
        return "Número de mesa inválido"

    comanda = {}
    for id_item, nombre, precio in platos + bebidas:
        try: 
            cantidad = int(request.form.get(nombre, 0))
        except:
            cantidad = 0
        if cantidad > 0:
            comanda[nombre] = cantidad
        
    precios = {}
    for id_item, nombre, precio in platos + bebidas:
        precios[nombre] = precio
        

    total = 0
    detalle = []
    for nombre, cantidad in comanda.items():
        precio_unitario = precios[nombre]
        subtotal = cantidad * precio_unitario
        total = total + subtotal
        detalle.append((nombre, cantidad, subtotal))

    return render_template("pedido.html", detalle=detalle, total=total, mesa=mesa)

@app.route("/confirmar", methods=["POST"])
def confirmar():
    mesa = request.form.get("mesa")
    items_raw = request.form.getlist("item")

    detalle = []
    total = 0
    for item in items_raw:
        nombre, cantidad_texto, subtotal_texto = item.split("|")
        cantidad = int(cantidad_texto)
        subtotal = int(subtotal_texto)
        detalle.append((nombre, cantidad, subtotal))
        total = subtotal + total

    pedidos_recibidos.append({"mesa": mesa, "detalle": detalle})
    return render_template("confirmado.html", detalle=detalle, total=total, mesa=mesa)

@app.route("/cocina")
def cocina():
    return render_template("cocina.html", pedidos=pedidos_recibidos)

@app.route("/admin")
def admin():
    platos, bebidas = obtener_menu()

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT valor FROM configuracion WHERE clave = ?", ("tope_mesa",))
    fila = cursor.fetchone()
    conexion.close()
    tope_mesa = fila [0]

    return render_template("admin.html", platos=platos, bebidas=bebidas, tope_mesa=tope_mesa)

@app.route("/admin/tope", methods=["POST"])
def admin_tope():
    nuevo_tope = request.form.get("tope_mesa")

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE configuracion SET valor = ? WHERE clave = ?", (nuevo_tope, "tope_mesa"))
    conexion.commit()
    conexion.close()

    return redirect("/admin")

@app.route("/admin/agregar", methods=["POST"])
def admin_agregar():
    nombre = request.form.get("nombre")
    precio = request.form.get("precio")
    categoria = request.form.get("categoria")

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO menu (nombre, precio, categoria) VALUES (?, ?, ?)", (nombre, precio, categoria))
    conexion.commit()
    conexion.close()

    return redirect("/admin")


@app.route("/admin/borrar/<int:id_item>")
def admin_borrar(id_item):
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM menu WHERE id = ?", (id_item,))
    conexion.commit()
    conexion.close()

    return redirect("/admin")

@app.route("/admin/editar/<int:id_item>")
def admin_editar(id_item):
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, precio, categoria FROM menu WHERE id = ?", (id_item,))
    item = cursor.fetchone()
    conexion.close()

    return render_template ("editar.html", item=item)

@app.route("/admin/actualizar/<int:id_item>", methods=["POST"])
def admin_actualizar(id_item):
    nombre = request.form.get("nombre")
    precio = request.form.get("precio")
    categoria = request.form.get("categoria")

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE menu SET nombre = ?, precio = ?, categoria = ? WHERE id = ?",
        (nombre, precio, categoria, id_item)
    )
    conexion.commit()
    conexion.close()

    return redirect("/admin")

if __name__ == "__main__":
    app.run(debug=True)