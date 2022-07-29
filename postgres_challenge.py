import psycopg2

# create connection
conn = psycopg2.connect(
    database = "flights",
    user = "docker",
    password = "docker",
    host = "0.0.0.0",
    port = "5433"
)

conn.autocommit = True

# open cursor to perform database operations
cur = conn.cursor()

# create tables in db
cur.execute("""CREATE TABLE IF NOT EXISTS aerolineas (
                    ID_AEROLINEA BIGSERIAL PRIMARY KEY,
                    NOMBRE_AEROLINEA varchar(40));""")

cur.execute("""CREATE TABLE IF NOT EXISTS aeropuertos (
                    ID_AEROPUERTO BIGSERIAL PRIMARY KEY,
                    NOMBRE_AEROPUERTO varchar(40));""")

cur.execute("""CREATE TABLE IF NOT EXISTS movimientos (
                    ID_MOVIMIENTO BIGSERIAL PRIMARY KEY,
                    DESCRIPCION varchar(20));""")

cur.execute("""CREATE TABLE IF NOT EXISTS vuelos (
                    ID_AEROLINEA BIGSERIAL,
                    ID_AEROPUERTO BIGSERIAL,
                    ID_MOVIMIENTO BIGSERIAL,
                    DIA date);""")

# insert data into tables
cur.execute("""INSERT INTO aerolineas (ID_AEROLINEA, NOMBRE_AEROLINEA)
                VALUES (1, 'Volaris'), (2, 'Aeromar'), (3, 'Interjet'), (4, 'Aeromexico');""")

cur.execute("""INSERT INTO aeropuertos (ID_AEROPUERTO, NOMBRE_AEROPUERTO)
                VALUES (1, 'Benito Juarez'), (2, 'Guanajuato'), (3, 'La paz'), (4, 'Oaxaca');""")

cur.execute("""INSERT INTO movimientos (ID_MOVIMIENTO, DESCRIPCION)
                VALUES (1, 'Salida'), (2, 'Llegada');""")

cur.execute("""INSERT INTO vuelos (ID_AEROLINEA, ID_AEROPUERTO, ID_MOVIMIENTO, DIA) values 
                    (1, 1, 1, '2021-05-02'),
                    (2, 1, 1, '2021-05-02'),
                    (3, 2, 2, '2021-05-02'),
                    (4, 3, 2, '2021-05-02'),
                    (1, 3, 2, '2021-05-02'),
                    (2, 1, 1, '2021-05-02'),
                    (2, 3, 1, '2021-05-04'),
                    (3, 4, 1, '2021-05-04'),
                    (3, 4, 1, '2021-05-04')""")

# ----- 1. ¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año? ----- #
movimientos_aeropuerto_qry = """SELECT nombre_aeropuerto, COUNT(nombre_aeropuerto) AS eventos
                                    FROM vuelos v
                                    JOIN aeropuertos a ON v.id_aeropuerto = a.id_aeropuerto
                                    GROUP BY nombre_aeropuerto 
                                    HAVING COUNT(nombre_aeropuerto) = (SELECT MAX(eventos) 
                                                    FROM (SELECT id_aeropuerto, COUNT(id_aeropuerto) AS eventos 
                                                    FROM vuelos GROUP BY id_aeropuerto) AS conteo_max);"""
# fetch data
cur.execute(movimientos_aeropuerto_qry)
airports = cur.fetchall()

print("1. What is the busiest airport during the year?")
print(', '.join('{} with {}'.format(*airport) for airport in airports))

# ----- 2. ¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante el año? ----- #
movimientos_aerolineas_qry = """SELECT nombre_aerolinea, COUNT(nombre_aerolinea) AS eventos
                                    FROM vuelos v
                                    JOIN aerolineas a ON v.id_aerolinea = a.id_aerolinea
                                    GROUP BY nombre_aerolinea 
                                    HAVING COUNT(nombre_aerolinea) = (SELECT MAX(eventos) 
                                                    FROM (SELECT id_aerolinea, COUNT(id_aerolinea) AS eventos 
                                                    FROM vuelos GROUP BY id_aerolinea) AS conteo_max);"""

# fetch data
cur.execute(movimientos_aerolineas_qry)
airlines = cur.fetchall()
print("\n\n\n2. What is the airline with the highest number of flights during the year?")
print(', '.join('{} with {}'.format(*airline) for airline in airlines))

# ----- 3. ¿En qué día se han tenido mayor número de vuelos? ----- #
max_flights_qry = """SELECT dia, COUNT(dia) AS n_vuelos FROM vuelos GROUP BY dia
                        HAVING COUNT(dia) = (SELECT MAX(n_vuelos) FROM (SELECT dia, COUNT(dia) as n_vuelos 
                                            FROM vuelos GROUP BY dia) AS counts_dia);"""

# fetch data
cur.execute(max_flights_qry)
day_max_flights = cur.fetchall()
print("\n\n\n3. Which day had the highest number of flights?")
print(', '.join('{} with {}'.format(*i) for i in day_max_flights))

# ----- 4. ¿Cuáles son las aerolíneas que tienen mas de 2 vuelos por día? ----- #
many_flights = """SELECT nombre_aerolinea, MIN(n_vuelos) FROM aerolineas a
                    JOIN (SELECT id_aerolinea, dia, COUNT(dia) AS n_vuelos 
                    FROM vuelos 
                    GROUP BY id_aerolinea, dia) AS gg
                        ON a.id_aerolinea = gg.id_aerolinea GROUP BY nombre_aerolinea 
                        HAVING MIN(n_vuelos) > 2;"""

# fetch data
cur.execute(many_flights)
n_flights = cur.fetchall()
print("\n\n\n4. Which airlines have more than 2 flights per day?")


if n_flights:
    print(', '.join('{} with {} flights'.format(*i) for i in n_flights))

else:
    print("There are no airlines with more than two flights per day")

