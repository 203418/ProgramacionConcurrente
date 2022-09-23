import time
from pytube import YouTube
import concurrent.futures
import threading

threading_local = threading.local()

def service(services):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_video, services)

def download_video(url):
    video = YouTube(url)
    download = video.streams.get_highest_resolution()
    download.download()

if __name__ == "__main__":
    urls = [
        "https://www.youtube.com/watch?v=MI26iOSmmyU&list=RDMI26iOSmmyU&start_radio=1",
        "https://www.youtube.com/watch?v=pfI3VPZn70k&list=RDMI26iOSmmyU&index=2",
        "https://www.youtube.com/watch?v=fjbKNTnWkHs",
        "https://www.youtube.com/watch?v=2EDCpDXMowc",
        "https://www.youtube.com/watch?v=OwJPPaEyqhI"
    ]
    init_time = time.time()
    service(urls)
    end_time = time.time() - init_time
    print(end_time)
