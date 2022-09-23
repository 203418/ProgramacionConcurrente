import requests
import time
import psycopg2

# Investigar sobre la libreria threading 

def get_service(conexiones):
    # Implementar request
    # Consumir un servicio que descargue por lo menos 5000 registros
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-03-05&limit=5000"
    r = requests.get(url)
    data = r.json()
    features = data['features']
    for feature in features:
        write_db(conexiones, feature['properties']['place'])


def write_db(conexiones, x):
    # Escribir el response en una base de datos
    try:
        conexiones[1].execute("insert into pokemons (name) values ('"+ x +"')")
    except Exception as err:
        print('Error en la inserción: '+ err)
    else:
        conexiones[0].commit()

def createConexion():
    try:
        conexion = psycopg2.connect(database='concurrenteb', user='postgres', password='kevinDa1')
        cursor1=conexion.cursor()
        cursor1.execute('select version()')
        version=cursor1.fetchone()
    except Exception as err:
        print('Error al conecta a la base de datos')
    else:
        return [conexion, cursor1, version]

def closeConexion(conexion):
    conexion.close()

if __name__ == "__main__":
    conexiones = createConexion()
    init_time = time.time()

    get_service(conexiones)
    end_time = time.time() - init_time
    print(end_time)
    closeConexion(conexiones[0])