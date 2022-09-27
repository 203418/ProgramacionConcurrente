from time import sleep
import requests
import threading
        
def checkUrl(url):
    status = requests.head(url)
    if status.status_code == 200:
        print(url + ', esta activo')
    else:
        print('El url '+  url  +', no esta activo')



class Hilo(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        h1 = threading.Thread(target=checkUrl, args=[self.url])
        h1.start()


while True:
    hilos = [
        Hilo('https://www.apple.com/'),
        Hilo('https://www.chase.com/'),
        Hilo('https://www.youtube.com'),
        Hilo('https://www.office.com/'),
        Hilo('https://www.yahoo.com/'),
        Hilo('https://www.amazon.com/'),
        Hilo('https://ww.amazon.com/'),
        Hilo('https://www.reddit.com/'),
        Hilo('https://www.linkedin.com/'),
        Hilo('https://www.tumblr.com/'),
        Hilo('https://www.pinterest.com/'),
        Hilo('https://www.pinterest.com/'),
        Hilo('https://www.netflix.com/'),
        Hilo('https://ww.netflix.com/'),
        Hilo('https://www.ebay.com/'),
        Hilo('https://www.microsoft.com/'),
        Hilo('https://ww.imgur.com/'),
        Hilo('https://www.imgur.com/'),
        Hilo('https://www.craigslist.org/'),
        Hilo('https://www.bing.com/'),
        Hilo('https://www.adobe.com/'),
        Hilo('https://ww.office.com/'),
        Hilo('https://www.chase.com/'),
        Hilo('https://ww.chase.com/'),
        Hilo('https://www.dropbox.com/'),
    ]
    for hilo in hilos:
        hilo.start()
    sleep(240)
    