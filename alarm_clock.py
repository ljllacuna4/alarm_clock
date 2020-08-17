import time
from os import system

url = "https://www.youtube.com/watch?v=iNpXCzaWW1s"

def play_alarm(url):
    system(f"start chrome /incognito {url}")

if __name__ == "__main__":
    
    while True:
        # t0 = time.gmtime()
        t0 = time.time()
        print(t0)
        if t0 >= 5:
            play_alarm(url)
            break
