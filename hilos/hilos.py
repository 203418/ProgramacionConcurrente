from ast import arg
import requests
import concurrent.futures
import threading
import time
from pytube import YouTube
import psycopg2

threading_local = threading.local()

def service(services):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_video, services)


def download_video(url):
    video = YouTube(url)
    download = video.streams.get_highest_resolution()
    download.download()


def get_service(url):
    # Implementar request
    # Consumir un servicio que descargue por lo menos 5000 registros
    conexiones = createConexion()
    r = requests.get(url)
    data = r.json()
    features = data['features']
    for feature in features:
        write_db(conexiones, feature['properties']['place'])
    closeConexion(conexiones[0])


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

def get_services(x=0):
   response = requests.get('https://randomuser.me/api/')
   print(x)
   if response.status_code == 200:
       results = response.json().get('results')
       name = results[0].get('name').get('first')
       print(name)
 
if __name__ == '__main__':
   init_time = time.time()
   x = 0
   urls = ["https://www.youtube.com/watch?v=MI26iOSmmyU&list=RDMI26iOSmmyU&start_radio=1",
    "https://www.youtube.com/watch?v=pfI3VPZn70k&list=RDMI26iOSmmyU&index=2",
    "https://www.youtube.com/watch?v=fjbKNTnWkHs",
    "https://www.youtube.com/watch?v=2EDCpDXMowc",
    "https://www.youtube.com/watch?v=OwJPPaEyqhI"
    ]
   th1 = threading.Thread(target=service, args=[urls])
   th1.start()
   th2 = threading.Thread(target=get_service, args=["https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-03-05&limit=5000"])
   th2.start()
   for x in range(0,50):
    th3 = threading.Thread(target=get_services, args=[x])
    th3.start()
   end_time = time.time() - init_time
   print(end_time)



# Descargar 5 videos de youtube
# Escribir en base de datos por lo menos 2mil registros
# Generar una solicitud a randomuser de por lo menos 50 usuarios