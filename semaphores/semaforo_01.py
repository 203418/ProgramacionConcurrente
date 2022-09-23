from threading import Thread, Semaphore
from pytube import YouTube

semaforo = Semaphore(1) # Crea la variable semáforo

def download_video(url):
    video = YouTube(url)
    download = video.streams.get_highest_resolution()
    download.download()

class Hilo(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url=url

    def run(self):
        semaforo.acquire() #Inicializa semáforo , lo adquiere
        download_video(self.url)
        semaforo.release() #Libera un semáforo e incrementa la varibale semáforo

threads_semaphore = [
                        Hilo("https://www.youtube.com/watch?v=fmACQQZCNeM"), 
                        Hilo("https://www.youtube.com/watch?v=Op5yl-KChuc"),
                        Hilo("https://www.youtube.com/watch?v=7BYLjn96_mg"),
                        Hilo("https://www.youtube.com/watch?v=x4KsG9wKLqo"),
                        Hilo("https://www.youtube.com/watch?v=-2MyZ8c_SvU"),
                        Hilo("https://www.youtube.com/watch?v=jfpSXYKL5kk"), 
                        Hilo("https://www.youtube.com/watch?v=dONYu8lfOzw"), 
                        Hilo("https://www.youtube.com/watch?v=m6jfZa00vkY"),
                        Hilo("https://www.youtube.com/watch?v=jhvfYsYQXkc"),
                        Hilo("https://www.youtube.com/watch?v=i13yFolV-wk")
                    ]
x=1;
for t in threads_semaphore:
    t.start()