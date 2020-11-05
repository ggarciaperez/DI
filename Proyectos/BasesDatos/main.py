import sqlite3 as dbapi

"""
# para ver version de la api
print(dbapi.apilevel)
# nivel de interaccion con hilos
print(dbapi.threadsafety)
# algo para las consultas pero no me quedo claro
print(dbapi.paramstyle)
# dio qmark que es el ?
"""
try:
    # si usasemos otra base de datos tendriamos que poner ip/usario y demas parametros
    bbdd = dbapi.connect("baseDatos.dat")
    # vemos que nos devuelve un objeto de connexion
    # print(bbdd)
except dbapi.StandardError as e:
    print(e)
else:
    print("Base de datos abierta")

try:
    # creamos cursor para operar en la base(similar al statement de java)
    cursor = bbdd.cursor()
    # vemos que tipo de datos es el cursor
    # print(cursor)
except dbapi.StandardError as e:
    print(e)
else:
    print("Cursor preparado")

try:
    print("esto ahora no hace nada")
    # cursor.execute(""" create table usuarios (dni text,
    #                                          nome text,
    #                                          direccion text)""")
    # cursor.execute("""insert into usuarios values ('1111-A', 'Maria', 'Canceleiro 2')""")
    # cursor.execute("""insert into usuarios values ('2222-B', 'Manuel', 'Rosalia 3')""")
    # cursor.execute("""insert into usuarios values ('3333-C', 'Ana', 'Areal 4')""")
    # bbdd.commit()
except dbapi.Error as e:
    print(e)
else:
    print("Datos insertados")

try:

    for x in (cursor.execute("select * from usuarios;")):
        print(x)
    # fetchone devuelve tupla a tupla (1 fetch 1 tupla)
    # print(cursor.fetchone())
    # fetchall devuelve todos los objetos (lista de tuplas)
    # print(cursor.fetchall())
    # fetchmany devuelve la cantidad de objetos queremos (lista de X tuplas)
    # print(cursor.fetchmany(x))
    cursor.execute("select * from usuarios;")
    for fila in cursor.fetchall():
        # print(fila)
        print ("Nombre: "+fila[1]+", con DNI: "+fila[0],"y residencia en la calle: "+fila[2])

except dbapi.Error as e:
    print(e)
else:
    print("Select correcto")


dni = input("Introduce dni: ")

try:
    consulta = ("select * from usuarios where dni='"+dni+"';")
    cursor.execute(consulta)
    print(cursor.fetchone())

except dbapi.Error as e:
    print(e)
finally:
    cursor.close()
    bbdd.close()
