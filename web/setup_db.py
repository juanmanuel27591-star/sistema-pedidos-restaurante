import sqlite3
conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS menu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        precio INTEGER,
        categoria TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS configuracion (
        clave TEXT PRIMARY KEY,
        valor TEXT
    )
""")

platos = [
    ("Milanesa", 35000),
    ("Fideos", 30000),
    ("Sandwich", 25000),
    ("Pizza", 20000),
    ("Empanada", 5000),
]

bebidas = [
    ("Cerveza", 5000),
    ("Gaseosa", 5000),
    ("Vino", 10000),
    ("Agua", 5000),
    ("Soda", 3000),
]
for nombre, precio in platos:
    cursor.execute("INSERT into menu (nombre, precio, categoria) VALUES(?, ?, ?)", (nombre, precio, "plato"))

for nombre, precio in bebidas:
    cursor.execute("INSERT into menu (nombre, precio, categoria) VALUES(?, ?, ?)", (nombre, precio, "bebida"))

cursor.execute("INSERT INTO configuracion (clave, valor) VALUES(?, ?)", ("tope_mesa", "20"))

conexion.commit()
conexion.close()

print("Base de datos creada y cargada con exito")