import threading
from pytube import YouTube

mutex = threading.Lock()

def download_video(url):
    video = YouTube(url)
    download = video.streams.get_highest_resolution()
    download.download()

class Hilo(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url=url

    def run(self):
        mutex.acquire()
        download_video(self.url)
        print("valor "+str(self.url))
        mutex.release()

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
for t in threads_semaphore:
    t.start()