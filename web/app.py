from flask import Flask, render_template, request

app = Flask(__name__)

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

pedidos_recibidos = []

@app.route("/")
def inicio():
    return render_template("menu.html", platos=platos, bebidas=bebidas)

@app.route("/pedido", methods=["POST"])
def pedido():
    mesa = request.form.get("mesa")

    comanda = {}
    for nombre, precio in platos + bebidas:
        try: 
            cantidad = int(request.form.get(nombre, 0))
        except:
            cantidad = 0
        if cantidad > 0:
            comanda[nombre] = cantidad

    precios = dict(platos + bebidas)
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


if __name__ == "__main__":
    app.run(debug=True)