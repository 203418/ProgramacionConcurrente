import requests
import time
import psycopg2
import concurrent.futures
import threading

# Investigar sobre la libreria threading 
threading_local = threading.local()

def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service, url)

def get_service(url):
    # Implementar request
    # Consumir un servicio que descargue por lo menos 5000 registros
    conexiones = createConexion()
    r = requests.get(url)
    data = r.json()
    features = data['features']
    for feature in features:
        write_db(conexiones, feature['properties']['place'])
    closeConexion()


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
    init_time = time.time()
    service("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-03-05&limit=10")
    end_time = time.time() - init_time
    print(end_time)

# Actividad crear una aplicación para descargar videos de 5 urls diferentes