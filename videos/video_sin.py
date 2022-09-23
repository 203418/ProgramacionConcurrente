import time
from pytube import YouTube

def service(services):
    for service in services:
        download_video(service)

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
